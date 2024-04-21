from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('register/', views.signup_page, name='signup'),  
    path('signup_view/', views.signup_view, name='signup_view'),
    path('login_view', views.login_view, name='login_view'), 
    path('dashboard/',views.dashboard,name='dashboard'),
    path('request-submitted/<str:track_id>', views.request_submitted, name='request_submitted'),  
    path('submit-request', views.submit_request, name='submit_request'),
    path('track/<str:track_id>/', views.track_request, name='track_request'),
    path('update-status/', views.update_status, name='update_status'),
    path('staffpage',views.staff_page,name='staffpage'),
    path('account-info', views.view_account_info, name='account_info'),  
    path('logout/', views.logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
