# Gas Utility Consumer Services Django Application

## Problem Statement
A gas utility company is facing challenges with a high volume of customer service requests, leading to long wait times and poor service. The current system is unable to handle the volume efficiently. The company requires a Django application to streamline consumer services, enabling customers to submit requests online, track their status, and access account information. Additionally, the application should empower customer support representatives to manage requests effectively.

## Features
### 1. Service Requests
   - Customers can submit service requests online.
   - Options to select the type of service request.
   - Ability to provide request details and attach files.

### 2. Request Tracking
   - Customers can track the status of their service requests.
   - View status, submission date & time, and resolution date & time.

## User Credentials
- **Superuser ID:** admin
  - **Password:** gasadmin@123
- Note: To access the staff dashboard, log in with the staff ID and password.
- **Staff ID:** staffadmin
  - **Password:** admin@1703

## Components
The application consists of the following components:
- `models.py`: Defines database models for customers and service requests.
- `forms.py`: Contains form definitions for service request submission.
- `views.py`: Implements logic for handling requests and rendering templates.
- `urls.py`: Maps URLs to view functions.
- `templates/`: Contains HTML templates for rendering user interfaces.
- `static/`: Stores static files like CSS and JavaScript.
- `media/`: Directory for storing uploaded files.

## Getting Started
1. Clone the repository:
```bash
https://github.com/atharvt17/Gas-Utility-Consumer-Services-Application
'''
2. Go to the Project Directory
```bash
cd gas_utility_consumer_services
'''
3. Perform database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
'''
4.Run the development server:
```bash
python manage.py runserver
'''
5.Access the application in your web browser:
'''bash
http://localhost:8000/
'''
