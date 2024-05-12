from django.urls import path
from literals.views import LisLiteralsView

app_name = "literals"


urlpatterns = [
    path("all/", LisLiteralsView.as_view(), name="literals"),

]
