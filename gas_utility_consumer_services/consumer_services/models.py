from django.db import models
from django.contrib.auth.models import User
import uuid

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    account_number = models.CharField(max_length=20, unique=True, editable=False)  # Auto-generated account number

    def save(self, *args, **kwargs):
        if not self.account_number:
            # Generate a unique account number
            self.account_number = uuid.uuid4().hex[:10].upper()  # Generate a random UUID and truncate it to 10 characters
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class ServiceRequest(models.Model):
    CATEGORIES = [
        ('service_issue', 'Service Issue'),
        ('billing_inquiry', 'Billing Inquiry'),
        ('other', 'Other')
    ]
    customer = models.ForeignKey('consumer_services.Customer', on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    details = models.TextField()
    files = models.FileField(upload_to='service_request_files/')
    status = models.CharField(max_length=20, default='Submitted')  # Set default status to 'submitted'
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True)
    track_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return str(self.track_id)