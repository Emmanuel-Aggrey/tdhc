from django.urls import include
from django.urls import path


urlpatterns = [
    path("accounts/", include("account.urls")),
    path("", include("api.lead")),
    path("", include("api.farm")),
]
