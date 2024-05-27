from django_filters import rest_framework as filters
from members.models import Member
from django.db import models


class MemberFilter(filters.FilterSet):

    marital_status = filters.ChoiceFilter(
        choices=Member.MARITAL_STATUS.CHOICES,
        required=False,
    )

    search = filters.CharFilter(
        method="filter_search",
        label="Search",
        help_text="search first_name, last_name,unique_id",
    )

    class Meta:
        model = Member
        fields = {
            'status',
            'marital_status',
            'phone_number',
            'baptismal_date',
            'digital_address',
            'location',
            'occupation',
            'place_of_work',
            # "search",

        }

    def filter_search(self, queryset, name, value):

        # Create a search query using multiple fields
        search_query = (
            models.Q(first_name__icontains=value)
            | models.Q(last_name__icontains=value)
            | models.Q(unique_id__icontains=value)
        )

        return queryset.filter(search_query)
