from typing import Optional

from core.redis import r

from .helpers import generate_verification_code
from .models import User


# noinspection PyMethodMayBeStatic
class AuthService:
    def find_user_by_email(self, email: str) -> Optional[User]:
        return User.objects.get(email=email)

    def create_user(self, user_data: dict) -> User:
        return User.objects.create_user(user_data)

    def create_email_verification_code(self, email: str) -> str:
        code = generate_verification_code()
        r.set(f"email:{email}", code, ex=120)
        return code

    def verify_email(self, email: str):
        user = self.find_user_by_email(email)
        user.verified = True
        user.save()

    def compare_verification_code(self, email: str, code: str) -> bool:
        verification_code = r.get(f"email:{email}")
        return verification_code == code


auth_service = AuthService()
