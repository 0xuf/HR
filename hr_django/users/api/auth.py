from rest_framework.generics import CreateAPIView
from users.serializers import AuthSerializer
from django.contrib.auth.models import User


class CreateUserAccount(CreateAPIView):
    """
    A class to create a user using a serializer
    """
    queryset = User.objects.all()
    serializer_class = AuthSerializer
