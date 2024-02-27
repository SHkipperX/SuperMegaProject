from django.db import models

__all__ = []


class ImagesManager(models.Manager):
    def spot_images(self, spot):
        return (
            self.get_queryset()
            .select_related(
                "spot",
            )
            .filter(
                spot_id=spot.pk,
            )
        )


class SpotMainImageManager(models.Manager):
    def main_image(self, spot):
        return (
            super()
            .get_queryset()
            .select_related("spot")
            .filter(spot_id=spot.pk)
            .first()
        )
