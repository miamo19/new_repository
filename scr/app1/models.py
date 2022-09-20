from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    gender     = models.CharField(max_length=25)
    email      = models.EmailField(null=True)
    def __str__(self):
        return self.last_name