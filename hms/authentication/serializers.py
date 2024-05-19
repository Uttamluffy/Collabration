from rest_framework import serializers
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model, excluding password field for security.
    """

    class Meta:
        model = get_user_model()
        fields = '__all__'