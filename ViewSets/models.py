from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.CharField(max_length=30,unique=True)
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250,unique=True)
    phone=models.CharField(max_length=230,unique=True)
    job=models.CharField(max_length=230)
    dept=models.CharField(max_length=230)
    company=models.CharField(max_length=230)
    location=models.CharField(max_length=230)
    
    def __str__(self):
        return self.name 



class EmpSignup(models.Model):
    username=models.CharField(max_length=300,unique=True)
    email=models.EmailField(max_length=250,unique=True)
    password=models.CharField(max_length=230)

    def __str__(self):
        return self.username
  
    

