from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class AuthSerializer(ModelSerializer):
    """
    Auth Serializer to create user
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        """
        This method will create username with set password
        """

        # Create user instance
        user = User(
            email=validated_data.get("email"),
            username=validated_data.get("username"),
        )

        # Set the password and save it into database
        user.set_password(validated_data.get("password"))
        user.save()

        return validated_data
