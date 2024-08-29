
from rest_framework import serializers
from members.models import Member, Location


class MemberSerializer(serializers.ModelSerializer):
    status_name = serializers.StringRelatedField(source="status")
    location_name = serializers.StringRelatedField(source="location")
    group_obj = serializers.SerializerMethodField()
    location = serializers.CharField()

    class Meta:
        model = Member
        read_only_fields = ["id"]
        exclude = ["is_deleted"]

    def get_group_obj(self, obj: Member):
        return obj.group.values()

    def create(self, validated_data):

        location_data = validated_data.pop('location', None)

        if location_data:
            location = self.get_or_create_location(location_data)
            validated_data['location'] = location

        return super().create(validated_data)

    def update(self, instance: Member, validated_data):
        location_data = validated_data.pop('location', None)

        if location_data:
            location = self.get_or_create_location(location_data)
            validated_data['location'] = location

        return super().update(instance, validated_data)

    def get_or_create_location(self, location_data):

        location, _ = Location.objects.update_or_create(
            name=location_data,
            defaults={}
        )
        return location
