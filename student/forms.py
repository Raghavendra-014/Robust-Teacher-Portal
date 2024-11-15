# student/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'subject', 'marks']

    # Override the clean_marks method to ensure marks don't exceed 100
    def clean_marks(self):
        marks = self.cleaned_data.get('marks')
        if marks > 100:
            raise forms.ValidationError("Marks cannot be greater than 100.")
        return marks
