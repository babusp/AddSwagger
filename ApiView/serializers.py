from pyexpat import model
from rest_framework import serializers

from ApiView.models import Student



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"