from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from src.users.models import Teacher


class RegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15, required=True, 
                                         validators=[UniqueValidator(
                                             queryset=Teacher.objects.all()
                                         )])
    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    subject = serializers.CharField(max_length=150, required=True)


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15, required=True)
    password = serializers.CharField(min_length=2, max_length=20, required=True)
