
from rest_framework import serializers

from apps.address.serializers import AddressSerializer
from apps.proposal.models import Proposal


class ProposalSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Proposal
        fields = "__all__"

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address_instance = address_serializer.save()

        validated_data['address'] = address_instance
        return super().create(validated_data)
