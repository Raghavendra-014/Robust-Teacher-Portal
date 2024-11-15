Teacher Portal with Django
Overview
The Teacher Portal is a Django-based web application that provides a secure login system for teachers and a portal to manage student details. Teachers can:

Log in to access the portal using secure authentication.
View, edit, and delete student details.
Add new students and update existing student marks.
Search and filter students based on name, subject, or marks.
Add pagination to the student list for easy navigation.
Reset passwords using a built-in password reset mechanism.

Features
Login and Authentication: Teachers can log in to the portal using their credentials.
Student Management: Teachers can view, add, update, or delete student records.
Pagination: The student list is paginated for easy navigation.
Search and Filter: Teachers can search and filter students by name, subject, and marks.
Forgot Password: Teachers can reset their password using their email address.
Installation
To get started with the project, follow the steps below:

Prerequisites

Python 3.10.12
Django 5.0.6
A database like SQLite

Step 1: Install Dependencies
Make sure you have pip installed and then run:
pip install -r requirements.txt

Step 2: Set Up Database
Run the following command to apply the migrations:

python manage.py migrate

Step 3: Create a Superuser
You can create an admin superuser to log in to the portal:

python manage.py createsuperuser

Follow the prompts to create a superuser account.

Step 4: Start the Development Server

python manage.py runserver
You can now access the application at http://127.0.0.1:8000/.


How to Use
1. Login as a Teacher
Go to http://127.0.0.1:8000/login/ to log in.
Enter your username and password.
If successful, you'll be redirected to the Teacher Portal's homepage where you can manage student records.
2. Managing Students
Once logged in, you can:

View Student List: A list of students with their names, subjects, and marks.
Add New Students: Click "Add New Student" to add a new student's details. If a student with the same name and subject exists, the marks will be updated.
Edit Student Details: You can edit student details inline and save the changes.
Delete Students: Remove students from the list by clicking the delete button.

Testing
To run the tests, use the following command:

bash
Copy code
python manage.py test
This will run the test suite and ensure the app functions correctly.

Technologies Used
Django: Python web framework for building the application.
SQLite: Default database (can be switched to PostgreSQL in settings).
Bootstrap 5: Frontend framework for responsive design.
HTML & CSS: Markup and styles for the frontend.
JavaScript: For form interactions and modal handling.
