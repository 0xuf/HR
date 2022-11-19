from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from utilities.permissions import IsTargetOwner

from scan.models import Target
from scan.serializers import (
    GetResultSerializer, PagenumSerializer
)


class GetResult(RetrieveAPIView):
    model = Target
    lookup_field = 'scan_id'
    permission_classes = [IsAuthenticated, IsTargetOwner]
    serializer_class = GetResultSerializer
    page_num_serializer = PagenumSerializer
    queryset = Target.objects.all()  # noqa

    def retrieve(self, request, *args, **kwargs):
        """
        Override retrieve method to make subdomains list paginate
        """

        # get requested url and page_number
        requested_url = f"{self.request.scheme}://{self.request.META.get('HTTP_HOST')}{self.request.path}"
        page_num = self.request.GET.get("page_num", 1)

        # Serialize and check page_number validation
        serialized_page_num = self.page_num_serializer(data=dict(page_num=page_num))
        if not serialized_page_num.is_valid():
            return Response(serialized_page_num.errors)

        # get serialized data
        serialized_data = self.serializer_class(self.get_object())
        page_num = serialized_page_num.data.get("page_num")

        # Do manual paginate on subdomains
        paginated_data = manual_paginator(serialized_data.data.get("subdomains"))

        # Response dictionary
        response_dict = dict()
        response_dict["count"] = paginated_data.get("count")
        response_dict["next"] = requested_url + f"?page_num={page_num+1}" if page_num < paginated_data.get("count") \
            else None
        response_dict["previous"] = requested_url + f"?page_num={page_num-1}" if page_num > 1 else None
        response_dict["date"] = serialized_data.data.get("date")
        response_dict["subdomains"] = paginated_data.get("output")[page_num-1] if paginated_data.get("output") > 0 else 0

        return Response(response_dict, status=status.HTTP_200_OK)


def manual_paginator(list_of_data: list, paginate_num: int = 10) -> dict:
    """
    Manual function to paginate a list within a number
    :param list_of_data: list of data to do pagination on it
    :param paginate_num: pagination based on the number received
    :return: dictionary of count and paginated data
    """
    paginated_data = [list_of_data[i:i+paginate_num] for i in range(0, len(list_of_data), paginate_num)]

    return dict(count=len(paginated_data), output=paginated_data)
