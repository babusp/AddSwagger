from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from ViewSets.models import EmpSignup, Employee

from ViewSets.serializers import EmpSignupSerializer, EmployeeSerializer

# Create your views here.


class EmployeeViewset(viewsets.ViewSet):

    serializer_class=EmployeeSerializer

    def get_object(self):
        user_id = self.kwargs.get("pk")
        user_obj = get_object_or_404(Employee, id=user_id)
        return user_obj

    def create(self, request, *args, **kwargs):
        """overriding for custom response"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(data=serializer.data)


    def list(self, request):
        queryset = Employee.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        emp = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(emp)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
 
        if not request.data:
            return Response("no data ")
        emp = self.get_object()
        serializer = self.serializer_class(
            emp,
            data=request.data,
            partial=True,
            context={"user": self.request.user},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        emp = self.get_object()
        emp.delete()
        return Response(data=None)



class EmpsignupAPIView(CreateAPIView):
    queryset=EmpSignup.objects.all()
    serializer_class=EmpSignupSerializer

    





# class LoginViewSet(viewsets.ViewSet):

#     serializer_class = LoginSerializer

#     def create(self, request):
#         serializer =self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             return Response(data=serializer.data["data"])
#         else:
#             return Response("no data found")

