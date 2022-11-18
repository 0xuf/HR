from rest_framework import serializers
from scan.models import Target
from uuid import uuid4


class CreateNewTargetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Target
        fields = ["domain"]

    def create(self, validated_data):

        target = Target(
            user=self.context.get("user"),
            domain=validated_data.get("domain"),
            scan_id=self.context.get("uuid")
        )
        target.save()

        return validated_data


class ViewTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        exclude = ["user", "id", "updated_at"]

    def to_representation(self, instance):
        response_dict = dict()
        response_dict["domain"] = instance.domain
        response_dict["date"] = instance.created_at.strftime("%Y-%m-%d")
        response_dict["scan_id"] = instance.scan_id
        response_dict["status"] = instance.status

        return response_dict
