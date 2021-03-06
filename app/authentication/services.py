from random import randint
from typing import Optional

from .models import User
from core.redis import r


def create_email_verification_code(email: str):
    code = _generate_verification_code()
    r.set(f'email:{email}', code, ex=120)


def find_user_by_email(email: str) -> Optional[User]:
    return User.objects.get(email=email)


def verify_email(email: str):
    user = find_user_by_email(email)
    user.verified = True
    user.save()


def compare_verification_code(email: str, code: str) -> bool:
    verification_code = r.get(f'email:{email}')
    return verification_code == code


def _generate_verification_code() -> str:
    return str(randint(100000, 999999))

