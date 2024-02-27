from django.contrib import messages
from django.db.models import Prefetch
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import FormMixin
from rating.forms import SpotRatingForm
from rating.models import RatingImages, SpotRating

from catalog.forms import SpotForm
from catalog.models import Region, Spot, SpotImages, SpotMainImage


__all__ = [
    "SpotListView",
    "SpotDetailView",
    "CreateFishingPlaceView",
]


class SpotListView(ListView):
    template_name = "catalog/catalog.html"

    def get(self, request):
        spots = (
            Spot.objects.select_related("spot_mainimage", "region")
            .filter(
                is_active=True,
            )
            .only("name", "region")
        )
        regions = Region.objects.only("region", "id")
        context = {"spots": spots, "regions": regions}
        return render(request, "catalog/catalog.html", context)

    def post(self, request):
        region = dict(request.POST)["region"][0]
        return redirect(f"/catalog/region/{region}")


class RegionView(ListView):
    def get(self, request, region):
        spots = (
            Spot.objects.select_related("spot_mainimage", "region")
            .filter(is_active=True, region=region)
            .only("name", "region")
        )
        regions = Region.objects.only("region", "id")
        context = {"spots": spots, "regions": regions, "region": region}
        return render(request, "catalog/region_list.html", context)

    def post(self, request, region):
        region = dict(request.POST)["region"][0]
        return redirect(f"/catalog/region/{region}")


class SpotDetailView(DetailView, FormMixin):
    model = Spot
    template_name = "catalog/detail.html"
    context_object_name = "spot_info"
    pk_url_kwarg = "pk"
    form_class = SpotRatingForm
    context = {}

    def get(self, request, pk):
        instance = None
        spot = self.model.objects.filter(id=pk)
        if not spot.first() or not spot.first().__getattribute__("is_active"):
            if not request.user.is_moderator or not request.user.is_superuser:
                return render(request, "404.html", {})
        form = SpotRatingForm(
            None,
            instance=instance,
        )
        self.context["form"] = form
        self.context["spot_info"] = (
            spot.select_related("spot_mainimage")
            .prefetch_related(
                Prefetch(
                    "spot_images",
                    queryset=SpotImages.objects.only("image"),
                ),
            )
            .first()
        )

        self.context["users_comments"] = (
            SpotRating.objects.filter(
                spot_id=pk,
            )
            .select_related("user")
            .prefetch_related(
                Prefetch(
                    "rating_images",
                    queryset=RatingImages.objects.only("image"),
                ),
            )
            .only(
                "user__username",
                "user__avatar",
                "mark",
                "comment",
                "created_at",
            )
        )

        return render(request, self.template_name, self.context)

    def post(self, request, pk):
        form = SpotRatingForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            if request.user.is_authenticated:
                if form.cleaned_data.get("mark") in (
                    5,
                    4,
                    3,
                    2,
                    1,
                ):
                    del form.cleaned_data["images"]
                    rating_spot = SpotRating.objects.update_or_create(
                        user=request.user,
                        spot_id=pk,
                        defaults=form.cleaned_data,
                    )
                    if request.FILES.get("images"):
                        RatingImages.objects.create(
                            spot=rating_spot[0],
                            image=request.FILES.get("images"),
                        )
                    messages.success(request, "Рейтинг выставлен")
                elif form.cleaned_data.get("mark") == 0:
                    SpotRating.objects.filter(
                        user=request.user,
                        spot_id=pk,
                    ).delete()
                    messages.success(request, "Рейтинг удалён")
                else:
                    messages.error(request, "Ошибка обработки формы!")
        return redirect(self.get_success_url(**self.kwargs))

    def get_success_url(self, **kwargs):
        return reverse("catalog:spot_detail", kwargs=self.kwargs)


class CreateFishingPlaceView(View, FormMixin):
    template_name = "catalog/create.html"
    model = Spot
    context = {}
    form_class = SpotForm
    success_url = "/catalog/create/"

    def get(self, request):
        self.context["form"] = self.form_class(
            None,
            instance=self.request.user,
        )

        return render(request, "catalog/create.html", self.context)

    def form_valid(self, form):
        images = self.request.FILES.getlist("images")
        if len(images) < 2:
            messages.error(self.request, "Добавьте несколько картинок места!")
            return render(self.request, "catalog/create.html", self.context)

        form_save = form.save(commit=False)
        form_save.user = self.request.user
        form_save.save()

        SpotMainImage.objects.create(spot=form_save, image=images[0])
        for image in images[1:]:
            SpotImages.objects.create(spot=form_save, image=image)
        messages.success(self.request, "Водоём добавлен!")
        return super().form_valid(form)

    def post(self, request):
        form = SpotForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        self.context["form"] = form
        messages.error(request, "Ошибка=)")
        return render(request, "catalog/create.html", self.context)


class CreatedPlace(View):
    template_name = "catalog/created_spots.html"
    context = {}
    model = Spot

    def get(self, request):
        spots = self.model.objects.filter(user=request.user)
        self.context["spots"] = spots
        return render(request, self.template_name, self.context)


class EditPalce(View):
    template_name = "catalog/edit_place.html"
    model = Spot
    form_class = SpotForm
    context = {}
    pk_url_kwarg = "pk"

    def get(self, request, pk):
        model = self.model.objects.get(id=pk, user=request.user)
        self.context["form"] = self.form_class(None, instance=model)
        return render(request, self.template_name, self.context)

    def post(self, request, pk):
        form = SpotForm(request.POST)
        form.is_valid()
        if request.user.is_authenticated:
            self.model.objects.update_or_create(
                user=request.user,
                id=pk,
                defaults=form.cleaned_data,
            )
        self.context["form"] = form
        return render(request, self.template_name, self.context)
