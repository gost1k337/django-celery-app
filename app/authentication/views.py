from rest_framework.viewsets import ViewSet

from .services import compare_verification_code, create_email_verification_code, verify_email
from .tasks import send_email_confirmation_task


class UserViewSet(ViewSet):
    pass
