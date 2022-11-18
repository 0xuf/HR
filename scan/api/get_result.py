from rest_framework.generics import RetrieveAPIView
from scan.serializers import GetResultSerializer
from rest_framework.permissions import IsAuthenticated
from utilities.permissions import IsTargetOwner
from scan.models import Target


class GetResult(RetrieveAPIView):
    lookup_field = 'scan_id'
    permission_classes = [IsAuthenticated, IsTargetOwner]
    serializer_class = GetResultSerializer

    def get_queryset(self):
        return Target.objects.all()  # noqa
