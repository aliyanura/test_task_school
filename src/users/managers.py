from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, phone_number, is_superuser, is_staff, is_active,
                     password=None):
        if not phone_number:
            raise ValueError("User must have a phone_number")
        user = self.model(
            phone_number=phone_number,
            is_superuser=is_superuser,
            is_active=is_active,
            is_staff=is_staff,
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, phone_number, password=None):
        return self._create_user(
            phone_number=phone_number,
            is_superuser=False,
            is_staff=True,
            is_active=True,
            password=password,
        )

    def create_superuser(self, phone_number, password=None):
        return self._create_user(
            phone_number=phone_number,
            is_superuser=True,
            is_staff=True,
            is_active=True,
            password=password,
        )
