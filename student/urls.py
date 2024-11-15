# student/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.teacher_login, name='teacher-login'),  # Login page
    path('', views.home, name='home'),  # Teacher Portal Home
    path('add_student/', views.add_or_update_student, name='add_or_update_student'),  # Add or update student
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),  # Edit student details
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),  # Delete student
    path('', views.student_list, name='student_list'), #List student
]
