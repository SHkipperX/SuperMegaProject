from django.db import models
from django.shortcuts import redirect
from django.views import generic

from catalog.models import Spot, SpotImages

__all__ = []


class UncheckedSpotsListView(generic.ListView):
    template_name = "moderation/uncheckedspot.html"
    model = Spot
    context_object_name = "items"

    def get_queryset(self):
        return (
            Spot.objects.select_related("spot_mainimage")
            .filter(is_active=False)
            .only("name")
            .order_by("date_created")
        )


class VerifySpotView(generic.DetailView):
    template_name = "moderation/verifyspot.html"
    model = Spot
    context_object_name = "spot"
    pk_url_kwarg = "pk"

    def get_queryset(self):
        return (
            Spot.objects.filter(id=self.kwargs["pk"])
            .select_related("spot_mainimage")
            .prefetch_related(
                models.Prefetch(
                    "spot_images",
                    queryset=SpotImages.objects.only("image"),
                ),
            )
        )

    def post(self, request, pk):
        post = request.POST.get("verify")
        if post == "publick":
            Spot.objects.filter(
                id=pk,
            ).update(
                is_active=True,
            )
        elif post == "delete":
            Spot.objects.get(
                spot_id=pk,
                is_active=False,
            ).delete()
        elif post == "denied":
            ...
        else:
            ...
        return redirect("/moderation/")
