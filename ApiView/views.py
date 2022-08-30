from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView


#local imports
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class ListStudentAPIView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class CreateStudentAPIView(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class UpdateStudentAPIView(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class DeleteStudentAPIView(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer



