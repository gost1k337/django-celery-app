from random import randint


def generate_verification_code() -> str:
    return str(randint(100000, 999999))


def make_email_confirmation_letter(username: str, code: str):
    return f'Hello, {username}\n' \
           f'Your confirmation code: {code}'
