from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import ServiceRequest, Customer
from uuid import uuid4
from django.contrib import messages

def login_page(request):
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        # Process form data and get user details
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # User is authenticated, log them in
            login(request, user)

            # Check if the username is 'staffadmin'
            if username == 'staffadmin':
                # Redirect to the staff page
                return redirect('/staffpage')
            else:
                # Redirect to dashboard
                return redirect('/dashboard')
        else:
            # Authentication failed, show error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def signup_page(request):
    return render(request,'registration.html')



def signup_view(request):
    if request.method == 'POST':
        # Process form data and get user details
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = fullname.split()[0] 
            user.last_name = ' '.join(fullname.split()[1:])  
            user.save()

            # Create a customer object
            customer = Customer.objects.create(user=user, name=fullname, email=email, username=username)
            
            # Display success message
            print("Registration successful")

            # Redirect to the home page
            return redirect('/')
        
        except IntegrityError:
            # Handle unique constraint violation (username already exists)
            return render(request, 'registration.html', {'error_message': 'Username already exists. Please choose a different username.'})
    else:
        return render(request, 'registration.html')

@login_required
def staff_page(request):
    active_requests = ServiceRequest.objects.exclude(status__in=['Completed', 'Cancelled'])
    return render(request, 'staff.html', {'active_requests': active_requests})

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            
            # Generate a unique track ID for the service request
            service_request.track_id = uuid4()
            
            try:
                service_request.customer = request.user.customer
            except Customer.DoesNotExist:
                # Handle the case where the Customer object does not exist
                pass
            service_request.save()
            return redirect('request_submitted', track_id=service_request.track_id)  # Pass the track ID to request_submitted view
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

@login_required
def request_submitted(request, track_id):
    return render(request, 'request_submitted.html', {'track_id': track_id})

@login_required
def track_request(request, track_id):
    # Retrieve the service request based on the provided track ID
    service_request = get_object_or_404(ServiceRequest, track_id=track_id)

    # Pass the service request to the template for rendering
    return render(request, 'track_request.html', {'service_request': service_request})


    
@login_required
def view_account_info(request):
    customer = request.user.customer
    return render(request, 'account_info.html', {'customer': customer})


@login_required
def logout_view(request):
    # Log the user out
    logout(request)
    
    # Redirect to the homepage or any other appropriate page
    return redirect('/')



def update_status(request):
    if request.method == 'POST':
        request_id = request.POST.get('requestId')
        new_status = request.POST.get('newStatus')

        try:
            service_request = ServiceRequest.objects.get(id=request_id)
            service_request.status = new_status
            service_request.save()
            messages.success(request, 'Status updated successfully.')
        except ServiceRequest.DoesNotExist:
            messages.error(request, 'Service request not found.')
        
        return redirect('staffpage')