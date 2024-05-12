
from rest_framework import serializers

from literals.models import Group, Location, Status


class LiteralsSerializer(serializers.Serializer):
    groups = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    statuses = serializers.SerializerMethodField()

    def get_groups(self, obj: Group):
        return Group.objects.values()

    def get_locations(self, obj: Location):
        return Location.objects.values()

    def get_statuses(self, obj: Status):
        return Status.objects.values()
