from rest_framework import serializers

from ViewSets.models import EmpSignup, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:

        model=Employee
        fields="__all__"

class EmpSignupSerializer(serializers.Serializer):
    
    class Meta:
        model=EmpSignup
        fields=["username","email","password"]
