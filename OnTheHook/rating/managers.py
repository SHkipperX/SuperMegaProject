from django.db import models

__all__ = []


class RatingManager(models.Manager):
    def marks(self, spot):
        return (
            super()
            .get_queryset()
            .select_related(
                "spot",
                "user",
            )
            .filter(spot=spot)
        )

    def user_marks(self, user):
        return (
            super()
            .get_queryset()
            .select_related("spot", "user")
            .filter(user=user)
            .order_by(
                "-created_at",
                "mark",
            )
        )
