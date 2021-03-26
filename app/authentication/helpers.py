from random import randint


def generate_verification_code() -> str:
    return str(randint(100000, 999999))
