from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .services import auth_service
from .tasks import send_email_confirmation_task


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['GET'])
    def current_user(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user = serializer.save()
        verification_code = auth_service.create_email_verification_code(
            user.email)
        send_email_confirmation_task.delay(user.email, verification_code)

    @action(url_path='verify', detail=False, methods=['POST'])
    def verify(self, request):
        email = request.user.email
        code = str(request.data.get('code'))
        success = auth_service.compare_verification_code(email=email,
                                                         code=code)
        if success:
            auth_service.verify_email(email)
        return Response({"success": success})

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]

        return super().get_permissions()
