# student/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.subject}'
