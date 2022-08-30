from django.db import models

# Create your models here.
class Student(models.Model):
    admin_id=models.CharField(max_length=30,unique=True)
    name=models.CharField(max_length=30)
    roll_no=models.CharField(max_length=30,unique=True)
    email=models.CharField(max_length=30)
    dept=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    college=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    def __str__(self):
        return self.name




    