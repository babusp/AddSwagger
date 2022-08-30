from lib2to3.pgen2 import token
import re
from .serializers import LoginSerializer,UserCreationSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.queryset.auth_toke.delete()
        return Response("logged out successfully")

class ListUserAPIview(generics.ListAPIView):
    queryset= User.objects.all()
    serializer_class = RegisterSerializer

class UserCreationrAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserCreationSerializer
  



