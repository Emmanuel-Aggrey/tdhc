
from rest_framework import routers
from members.views import MemberViewSet


app_name = "member"

router = routers.DefaultRouter()
router.register("", MemberViewSet, "member")


urlpatterns = [

]

urlpatterns += router.urls
