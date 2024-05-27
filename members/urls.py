
from rest_framework import routers
from members.views import MemberViewSet, MemberReportView
from django.urls import path

app_name = "member"

router = routers.DefaultRouter()
router.register("", MemberViewSet, "member")


urlpatterns = [
    path('reports/', MemberReportView.as_view(), name='reports'),
]

urlpatterns += router.urls
