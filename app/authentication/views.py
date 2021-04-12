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

    @action(detail=False, methods=['GET'])
    def current_user(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user = serializer.save()
        verification_code = create_email_verification_code(user.email)
        send_email_confirmation_task.delay(user.email, verification_code)

    @action(url_path='verify', detail=False, methods=['POST'])
    def verify(self, request):
        email = request.user.email
        code = str(request.data.get('code'))
        success = compare_verification_code(email=email, code=code)
        if success:
            verify_email(email)
        return Response({"success": success})

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]

        return super().get_permissions()
