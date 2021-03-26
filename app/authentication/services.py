from typing import Optional

from core.redis import r

from .dto import UserDTO
from .helpers import generate_verification_code
from .models import User


def create_user(user_data: UserDTO) -> User:
    return User.objects.create_user(user_data)


def create_email_verification_code(email: str) -> str:
    code = generate_verification_code()
    r.set(f"email:{email}", code, ex=120)
    return code


def find_user_by_email(email: str) -> Optional[User]:
    return User.objects.get(email=email)


def verify_email(email: str):
    user = find_user_by_email(email)
    user.verified = True
    user.save()


def compare_verification_code(email: str, code: str) -> bool:
    verification_code = r.get(f"email:{email}")
    return verification_code == code
