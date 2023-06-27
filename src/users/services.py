import random
from typing import Tuple
from django.db import transaction
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from src.users.models import Teacher
from src.common.exceptions import ObjectNotFoundException
from src.common.services import Service
from src.common.validators import validate_user_password


class TokenService:
    model = Token

    @classmethod
    def create_auth_token(cls, phone_number: str, password: str) -> Tuple[Teacher, Token, Token]:
        teacher = authenticate(phone_number=phone_number, password=password)
        if teacher:
            token, created = cls.model.objects.get_or_create(user=teacher)
            return teacher, token, created
        else:
            raise ObjectNotFoundException('User not found or not active')

    @classmethod
    def destroy_auth_token(cls, user: Teacher) -> None:
        return cls.model.objects.filter(user=user).delete()
    

class TeacherService(Service):
    model = Teacher

    @classmethod
    def create_teacher(cls, phone_number: str, password: str, conf_password: str, **kwargs):
        teacher = cls.model(phone_number=phone_number, **kwargs)
        correct_password = validate_user_password(password=password, conf_password=conf_password)
        teacher.set_password(correct_password)
        teacher.save()
        return teacher
