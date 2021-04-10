from typing import TYPE_CHECKING

from django.contrib.auth.base_user import BaseUserManager

if TYPE_CHECKING:
    from .models import User


class UserManager(BaseUserManager):
    def create_user(self, user_data: dict) -> 'User':
        user = self.model(email=user_data['email'],
                          username=user_data['username'])

        user.set_password(user_data['password'])
        user.save()

        return user

    def create_superuser(self, **user_data: dict) -> 'User':
        user = self.create_user(user_data)

        user.is_superuser = True
        user.is_staff = True
        user.verified = True
        user.save()

        return user
