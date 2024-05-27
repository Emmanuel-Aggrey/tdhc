# Create your views here.

from .models import Member
from django.db.models import Count, Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
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


class MemberReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "total_members": self.get_total_members(),
            "marital_status_counts": self.get_marital_status_counts(),
            "group_counts": self.get_group_counts(),
            "gender_counts": self.get_gender_counts(),
            "status_counts": self.get_status_counts(),


        }
        return Response(data, status=status.HTTP_200_OK)

    def get_total_members(self):
        return Member.objects.count()

    def get_marital_status_counts(self):
        return list(Member.objects.values('marital_status').annotate(count=Count('marital_status')))

    def get_group_counts(self):
        return list(Member.objects.values('group__name').annotate(count=Count('group')))

    def get_gender_counts(self):
        return list(Member.objects.values('gender').annotate(count=Count('gender')))

    def get_status_counts(self):
        return list(Member.objects.values('status__name').annotate(count=Count('status')))
