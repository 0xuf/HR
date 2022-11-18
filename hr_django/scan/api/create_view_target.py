from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from scan.serializers import (CreateNewTargetSerializer, ViewTargetSerializer)
from scan.models import Target
from uuid import uuid4
from scan.tasks import scan_target


class CreateViewTarget(ListCreateAPIView):
    """
    Create new target api class
    """
    serializer_class = ViewTargetSerializer
    create_target_serializer = CreateNewTargetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Target.objects.filter(user=self.request.user)  # noqa

    def create(self, request, *args, **kwargs) -> Response:
        """
        Create method to create target in database using CreateNewTargetSerializer
        """
        # Define _uuid variable
        _uuid = uuid4()

        # Pass data into create target serializer
        serialized_data = self.create_target_serializer(data=dict(
            domain=self.request.POST.get("domain")
        ),
            context=dict(
                user=self.request.user,
                uuid=_uuid
            )
        )

        # Check if the values are valid, return a response with a status code of 201, and if it is wrong, 400
        if serialized_data.is_valid():
            serialized_data.save()
            # Start scan in background
            scan_target.delay(serialized_data.data.get("domain"))

            return Response({"scan_id": _uuid}, status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
