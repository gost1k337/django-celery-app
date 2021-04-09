from rest_framework import serializers

from . import services
from .models import User


class UserSerializer(serializers.ModelSerializer):
    register_date = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'register_date')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: dict) -> User:
        return services.create_user(validated_data)
