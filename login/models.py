
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    """
    User Model Class
    """
    ADMIN=1
    BUSINESS_OWNER=2
    END_USER=3
   

    ROLES = (
        (ADMIN, "Admin"),
        (BUSINESS_OWNER, "Business Owner"),
        (END_USER, "EndUser"),
    
    )
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True,max_length=100, null=True, blank=True)
    phone_no = models.CharField(unique=True, max_length=17, null=True, blank=True)
    role = models.IntegerField(default=3, choices=ROLES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
   
   
