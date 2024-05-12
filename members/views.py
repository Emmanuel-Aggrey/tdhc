# Create your views here.

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from members.models import Member
from members.serializers import MemberSerializer
from members.filters import MemberFilter


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MemberSerializer
    queryset = Member.objects.order_by("id")
    filter_backends = [DjangoFilterBackend]
    filterset_class = MemberFilter
