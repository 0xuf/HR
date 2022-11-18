from rest_framework.serializers import ModelSerializer
from scan.models import Target
from datetime import datetime
import ast


class GetResultSerializer(ModelSerializer):
    class Meta:
        model = Target
        fields = ["scan_id"]

    def to_representation(self, instance):
        response_dict = dict()
        subdomains = list()

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
