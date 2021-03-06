from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    UserModel = get_user_model()

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = self.UserModel.objects.get(email=email)
        except self.UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return self.UserModel.objects.get(pk=user_id)
        except self.UserModel.DoesNotExist:
            return None
