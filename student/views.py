# student/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages


# Custom teacher login view
def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Teacher home page (student listing)
@login_required
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})
# Edit student details
@login_required
def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

# Delete student
@login_required
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('home')

@login_required
def add_or_update_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['name']
            student_subject = form.cleaned_data['subject']
            student_marks = form.cleaned_data['marks']

            # Check if a student with the same name and subject exists
            existing_student = Student.objects.filter(name=student_name, subject=student_subject).first()
            
            if existing_student:
                # If student exists, replace their marks with the new value
                existing_student.marks = student_marks
                existing_student.save()
                messages.success(request, f"Marks for {student_name} in {student_subject} have been updated.")
            else:
                # If student doesn't exist, create a new entry
                form.save()
                messages.success(request, f"New student {student_name} in {student_subject} has been added.")
                
            return redirect('home')  # Redirect to the student list after successful submission
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def student_list(request):
    # Get search query from GET parameters
    query = request.GET.get('q', '')
    
    # Start by retrieving all students
    students = Student.objects.all()

    # If there is a search query, filter students by name or subject
    if query:
        students = students.filter(Q(name__icontains=query) | Q(subject__icontains=query))

    # Pagination: Show 10 students per page
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)

    # Pass the query parameter to the template, so the search term remains in the search box
    return render(request, 'student_list.html', {'page_obj': page_obj, 'query': query})

