from enum import auto
from random import choices
from sre_constants import CHCODES
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
   
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            id=validated_data["id"],
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user





class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token



class UserCreationSerializer(serializers.ModelSerializer):

    ADMIN=1
    BUSINESS_OWNER=2
    END_USER=3
    STAFF_USER=4

    ROLES = (
        (ADMIN, "Admin"),
        (BUSINESS_OWNER, "Business Owner"),
        (END_USER, "EndUser"),
        (STAFF_USER, "StaffUser"),
    ) 

    phone_no = serializers.CharField( max_length=17)
    role = serializers.ChoiceField( default=3, choices=ROLES)

    class Meta:

        model=User
        fields=["username","password","first_name","last_name","email","phone_no","role"]
    

    # def create(self, validated_data):
    #     user = User.objects.create(
    #        # id=validate_password['id'],
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         phone_no=validated_data['phone_no'],
    #         role=validated_data['role']
    #     ) 
    #     user.set_password(validated_data['password'])
    #     user.save()





