# Create your views here.

from .models import Member
from django.db.models import Count, Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
import io

from rest_framework.permissions import IsAuthenticated
from members.models import Member
from members.serializers import MemberSerializer
from members.filters import MemberFilter
import openpyxl
from django.http import HttpResponse


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
            "total_members_baptised": self.get_total_members_baptised(),
            "total_members_with_occupation": self.get_total_members_with_occupation(),
            "active_members": self.get_active_members(),




        }
        return Response(data, status=status.HTTP_200_OK)

    def get_total_members(self):
        return Member.objects.count()

    def get_active_members(self):
        return Member.objects.filter(status__name__iexact='active').count()

    def get_total_members_baptised(self):
        return Member.objects.exclude(baptismal_date__isnull=True).count()

    def get_total_members_with_occupation(self):
        return Member.objects.exclude(occupation__isnull=True).count()

    def get_marital_status_counts(self):
        return list(Member.objects.values('marital_status').annotate(count=Count('marital_status')))

    def get_group_counts(self):
        return list(Member.objects.values('group__name').annotate(count=Count('group')))

    def get_gender_counts(self):
        return list(Member.objects.values('gender').annotate(count=Count('gender')))

    def get_status_counts(self):
        return list(Member.objects.values('status__name').annotate(count=Count('status')))


class ExportMembersToExcel(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Create a workbook and a worksheet

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'Members'

        # Define the headers
        headers = [
            'Unique ID', 'First Name', 'Last Name', 'Other Name', 'Email', 'Phone Number',
            'Secondary Phone Number', 'Marital Status', 'Gender', 'Status', 'Group',
            'Baptismal Date', 'Digital Address', 'Location', 'Occupation',
            'Place of Work',  'No.Children'
        ]
        ws.append(headers)

        search_params = request.query_params
        filters = self.apply_filters(search_params)

        members = Member.objects.filter(filters)

        for member in members:
            row = [
                member.unique_id, member.first_name, member.last_name, member.other_name,
                member.email, member.phone_number, member.secondary_phone_number,
                member.marital_status, member.gender, member.status.name if member.status else None,
                # Joining group names
                ', '.join(group.name for group in member.group.all()),
                member.baptismal_date, member.digital_address, member.location.name if member.location else None,
                member.occupation, member.place_of_work,  member.number_of_children
            ]
            ws.append(row)

        # Save the workbook to an in-memory file
        output = io.BytesIO()
        wb.save(output)
        output.seek(0)

        # Create HTTP response
        response = HttpResponse(
            output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="members.xlsx"'
        return response

    def apply_filters(self, query_params):
        filters = Q()

        occupation = query_params.get('occupation', [None])
        location = query_params.get('location', [None])
        phone_number = query_params.get('phone_number', [None])
        status = query_params.get('status', [None])
        gender = query_params.get('gender', [None])
        search = query_params.get('search', [None])

        if occupation:
            filters &= Q(occupation__icontains=occupation)
        if location:
            filters &= Q(location_id=location)
        if phone_number:
            filters &= Q(phone_number__icontains=phone_number)
        if status:
            filters &= Q(status_id=status)
        if gender:
            filters &= Q(gender=gender)
        if search:
            filters &= Q(first_name__icontains=search) | Q(
                last_name__icontains=search) | Q(other_name__icontains=search)

        return filters
