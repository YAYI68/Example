from django.db import models
from django.urls import reverse

# Create your models here.
class  School(models.Model):
    name = models.CharField(max_length=64)
    principal = models.CharField(max_length=64)
    location = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse("student")

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=64)
    age = models.CharField(max_length=64)
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def get_absolute_url(self):
        return reverse("school:list")

    def __str__(self):
        return self.name
