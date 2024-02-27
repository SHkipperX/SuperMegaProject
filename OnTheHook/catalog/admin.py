from django.contrib import admin

import catalog.models

__all__ = []


class ImageInline(admin.TabularInline):
    model = catalog.models.SpotMainImage
    readonly_fields = (
        "id",
        catalog.models.SpotMainImage.image_tmb,
    )
    extra = 1


class ImagesInline(admin.TabularInline):
    model = catalog.models.SpotImages
    readonly_fields = (
        "id",
        catalog.models.SpotImages.image_tmb,
    )


@admin.register(catalog.models.Spot)
class SpotAdmin(admin.ModelAdmin):
    inlines = (
        ImageInline,
        ImagesInline,
    )
    fields = (
        catalog.models.Spot.name.field.name,
        catalog.models.Spot.is_active.field.name,
        catalog.models.Spot.text.field.name,
        catalog.models.Spot.lat.field.name,
        catalog.models.Spot.lon.field.name,
        catalog.models.Spot.region.field.name,
        catalog.models.Spot.status_free.field.name,
        catalog.models.Spot.date_created.field.name,
    )
    readonly_fields = (catalog.models.Spot.date_created.field.name,)

    list_display = (
        catalog.models.Spot.name.field.name,
        catalog.models.Spot.is_active.field.name,
        catalog.models.Spot.text.field.name,
        catalog.models.Spot.lat.field.name,
        catalog.models.Spot.lon.field.name,
        catalog.models.Spot.region.field.name,
        catalog.models.Spot.date_created.field.name,
        catalog.models.Spot.status_free.field.name,
    )
    list_display_links = (catalog.models.Spot.name.field.name,)

    def save_model(
        self,
        request,
        obj,
        form,
        change,
    ):
        form_save = form.save(commit=False)
        form_save.user = request.user
        form_save.save()

        return super().save_model(request, obj, form, change)


admin.site.register(catalog.models.Region)
