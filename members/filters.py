from django_filters import rest_framework as filters
from members.models import Member


class MemberFilter(filters.FilterSet):

    marital_status = filters.ChoiceFilter(
        choices=Member.MARITAL_STATUS.CHOICES,
        required=False,
    )

    class Meta:
        model = Member
        fields = {
            'status',
            'marital_status',
            'first_name',
            'last_name',
            'phone_number',
            'baptismal_date',
            'digital_address',
            'location',
            'occupation',
            'place_of_work',

        }
