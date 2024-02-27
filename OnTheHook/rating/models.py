from ckeditor.fields import RichTextField
from django.db import models
from django.utils import dateformat, timezone
from django.utils.safestring import mark_safe
from rating.managers import RatingManager
from sorl.thumbnail import get_thumbnail

from catalog.models import Spot
from users.models import User


__all__ = [
    "SpotRating",
    "RatingChoices",
]


class RatingChoices:
    choice = (
        (5, "Любовь"),
        (4, "Обожание"),
        (3, "Нейтрально"),
        (2, "Неприязнь"),
        (1, "Ненависть"),
        (0, "Удалить"),
    )


class SpotRating(models.Model):
    objects = RatingManager()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
    )
    spot = models.ForeignKey(
        Spot,
        on_delete=models.CASCADE,
        verbose_name="товар",
    )
    mark = models.SmallIntegerField(
        verbose_name="оценка",
        choices=RatingChoices.choice,
    )
    created_at = models.DateTimeField(
        verbose_name="дата отзыва",
        auto_now=True,
    )
    comment = RichTextField(
        verbose_name="Комментарий",
        help_text="Оставьте комментарий",
    )

    class Meta:
        verbose_name = "рэйтинг"
        verbose_name_plural = "рэйтинги"

    def __str__(self) -> str:
        return f"Оценка {self.mark}!"


class RatingImages(models.Model):
    def upload_to(self, file_name):
        type_image = file_name.split(".")[1]
        return (
            f"rating/{self.spot.spot_id}/"
            f"{self.spot.user.id}/"
            f"{dateformat.format(timezone.now(), 'd_m_y_H_i',)}.{type_image}"
        )

    spot = models.ForeignKey(
        "SpotRating",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="товар",
        related_query_name="rating_images",
        related_name="rating_images",
    )

    image = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True,
        verbose_name="изображение",
    )

    @property
    def get_300x300px(self):
        return get_thumbnail(
            self.image,
            "300x300",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f"<img src=/media/{self.get_300x300px}/>",
            )
        return "Изображение не найдено/отсутсвует"

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    fields = ["image_tmb"]

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "изображения"
        verbose_name_plural = "изображения"
