from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .services import compare_verification_code, create_email_verification_code, verify_email
from .tasks import send_email_confirmation_task


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False,
            methods=['GET'],
            permission_clasess=[permissions.IsAuthenticated])
    def current_user(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
