from rest_framework import serializers
from scan.models import Target
from datetime import datetime
import ast


class GetResultSerializer(serializers.ModelSerializer):
    """
    Get result of scan serializer
    """
    class Meta:
        """
        Meta class
        """
        model = Target
        fields = ["scan_id"]

    def to_representation(self, instance) -> dict:
        """
        Override to_representation to customize response
        :param instance: received instance from request
        """

        # define response dict and subdomains list
        response_dict = dict()
        subdomains = list()

        # Loop into subdomains of instance to make list from them
        for subdomain in instance.subdomains.all():
            subdomains.append(
                {
                    subdomain.subdomain: ast.literal_eval(subdomain.nuclei_result),
                    "ip": subdomain.ip_address
                }
            )
        response_dict["date"] = datetime.now().strftime("%Y-%m-%d")
        response_dict["subdomains"] = subdomains

        return response_dict


class PagenumSerializer(serializers.Serializer):  # noqa
    """
    Page number serializer
    """
    page_num = serializers.IntegerField()
