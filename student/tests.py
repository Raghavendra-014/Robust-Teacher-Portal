# student/tests.py
from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):
    def test_student_creation(self):
        student = Student.objects.create(name="John Doe", subject="Math", marks=75)
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.subject, "Math")
        self.assertEqual(student.marks, 75)

    def test_update_student_marks(self):
        student = Student.objects.create(name="Jane Doe", subject="Science", marks=80)
        student.marks += 20  # Update marks
        student.save()
        updated_student = Student.objects.get(name="Jane Doe")
        self.assertEqual(updated_student.marks, 100)
