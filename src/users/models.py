from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from src.common.models import BaseModel
from src.users.managers import UserManager


class Teacher(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone_number = models.CharField(max_length=150, blank=False,
                                null=False, unique=True,
                                verbose_name=("Номер телефона"))
    password = models.CharField(max_length=128, blank=True,
                                null=True, verbose_name=("Пароль"))
    subject = models.CharField(max_length=350, verbose_name='Предмет')
    is_active = models.BooleanField(default=True,
                                    verbose_name=("Является активным"))
    is_staff = models.BooleanField(
        default=False, verbose_name=("Является сотрудником системы")
    )
    is_superuser = models.BooleanField(
        default=False, verbose_name=("Является администратором системы")
    )

    USERNAME_FIELD = "phone_number"

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    class Meta:
        db_table = "teachers"
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
        ordering = ("-created_at",)