from rest_framework import serializers
from scan.models import Target
from uuid import uuid4


class CreateNewTargetSerializer(serializers.ModelSerializer):
    """
    Create new target serializer
    """
    class Meta:
        """
        Meta class
        """
        model = Target
        fields = ["domain"]

    def create(self, validated_data) -> dict:
        """
        Override create method to create customized object in database
        :param validated_data: retrieve validated_data from request
        """

        # Create instance and save into database
        target = Target(
            user=self.context.get("user"),
            domain=validated_data.get("domain"),
            scan_id=self.context.get("uuid")
        )
        target.save()

        return validated_data


class ViewTargetSerializer(serializers.ModelSerializer):
    """
    View target serializer
    """
    class Meta:
        """
        Meta class
        """
        model = Target
        exclude = ["user", "id", "updated_at"]

    def to_representation(self, instance) -> dict:
        """
        Override to_representation method to customize response
        :param instance: received instance object from request
        """

        # Customized response
        response_dict = dict()
        response_dict["domain"] = instance.domain
        response_dict["date"] = instance.created_at.strftime("%Y-%m-%d")
        response_dict["scan_id"] = instance.scan_id
        response_dict["status"] = instance.status

        return response_dict
