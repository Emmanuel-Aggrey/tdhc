
from rest_framework import serializers
from members.models import Member
from literals.models import Group


class MemberSerializer(serializers.ModelSerializer):

    groups_obj = serializers.SerializerMethodField()
    status_name = serializers.StringRelatedField(source="status")
    location_name = serializers.StringRelatedField(source="location")

    class Meta:
        model = Member
        read_only_fields = ["id"]
        exclude = ["is_deleted"]

    def get_groups_obj(self, obj: Member):
        return Group.objects.filter(pk__in=obj.group.all()).values()
