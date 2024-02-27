from django.contrib import admin
from rating.models import SpotRating

__all__ = []


@admin.register(SpotRating)
class SpotRatingAdmin(admin.ModelAdmin):
    readonly_fields = (
        SpotRating.user.field.name,
        SpotRating.spot.field.name,
        SpotRating.mark.field.name,
        SpotRating.created_at.field.name,
        SpotRating.comment.field.name,
    )
    list_display = (
        SpotRating.user.field.name,
        SpotRating.spot.field.name,
        SpotRating.mark.field.name,
    )
