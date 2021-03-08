from celery import shared_task
from core.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from .services import find_user_by_email
from .utils import make_email_confirmation_letter


@shared_task
def send_email_confirmation_task(email, verification_code):
    receiver = find_user_by_email(email)

    message = make_email_confirmation_letter(receiver.username, verification_code)
    send_mail(
        'Email Confirmation',
        message,
        EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )
