from django.shortcuts import render
from django.urls import path 
from .views import ListStudentAPIView,CreateStudentAPIView,DeleteStudentAPIView,UpdateStudentAPIView

urlpatterns=[

    path("list/",ListStudentAPIView.as_view(),name="Student-list"),
    path("create/",CreateStudentAPIView.as_view() ,name="Student-Create"),
    path("update/<int:pk>/",UpdateStudentAPIView.as_view() ,name="Student-Update"),
    path("delete/<int:pk>/",DeleteStudentAPIView.as_view() ,name="Student-Delete"),
    

    ]