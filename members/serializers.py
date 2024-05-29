
from rest_framework import serializers
from members.models import Member


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        exclude = ["is_deleted"]


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        read_only_fields = ["id"]
        exclude = ["is_deleted"]

    def to_representation(self, instance):
        serializer = BaseSerializer(instance=instance)
        serializer.Meta.model = instance.__class__
        return serializer.data if instance else {}
