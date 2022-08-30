from django.contrib import admin

from ViewSets.models import EmpSignup, Employee

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmpSignup)