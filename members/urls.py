
from rest_framework import routers
from members.views import MemberViewSet, MemberReportView, ExportMembersToExcel
from django.urls import path

app_name = "member"

router = routers.DefaultRouter()
router.register("", MemberViewSet, "member")


urlpatterns = [
    path('reports/', MemberReportView.as_view(), name='reports'),
    path('export-members/', ExportMembersToExcel.as_view(),
         name='export_members_to_excel'),

]

urlpatterns += router.urls
