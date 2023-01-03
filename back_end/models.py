
from django.db import models

# Create your models here.
from django.db import models


class Student_information(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    grade = models.CharField(max_length=20)

