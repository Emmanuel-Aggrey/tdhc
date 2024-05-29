
from rest_framework import serializers
from members.models import Member


class MemberSerializer(serializers.ModelSerializer):
    status_name = serializers.StringRelatedField(source="status")
    location_name = serializers.StringRelatedField(source="location")
    group_obj = serializers.SerializerMethodField()

    class Meta:
        model = Member
        read_only_fields = ["id"]
        exclude = ["is_deleted"]

    def get_group_obj(self, obj: Member):
        return obj.group.values()
