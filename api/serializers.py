from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
            }