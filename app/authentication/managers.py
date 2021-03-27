from typing import TYPE_CHECKING

from django.contrib.auth.base_user import BaseUserManager

if TYPE_CHECKING:
    from .models import User


class UserManager(BaseUserManager):
    def create_user(self, email, username, password) -> 'User':
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password) -> 'User':
        user = self.create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.verified = True
        user.save()

        return user
