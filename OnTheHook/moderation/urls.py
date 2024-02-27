from django.urls import path
from moderation import views

app_name = "moderation"

urlpatterns = [
    path(
        "",
        views.UncheckedSpotsListView.as_view(),
        name="unchecked_spots",
    ),
    path(
        "verify/<int:pk>/",
        views.VerifySpotView.as_view(),
        name="verify_spot",
    ),
]
