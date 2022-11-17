from rest_framework.generics import CreateAPIView
from users.serializers import AuthSerializer


class CreateUserAccount(CreateAPIView):
    """
    A class to create a user using a serializer
    """
    serializer_class = AuthSerializer
