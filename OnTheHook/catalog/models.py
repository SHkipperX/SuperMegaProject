import re

from ckeditor.fields import RichTextField
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import dateformat, timezone
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from catalog.validators import MaxWordsValidator

__all__ = []

REGEX = re.compile(r"[^\w]")


def spot_directory_path(instance, filename):
    return f"catalog/{instance.spot.id}/{filename}"


class Region(models.Model):
    region = models.CharField(
        verbose_name="регион",
        max_length=150,
        validators=[validators.MaxLengthValidator(150)],
        help_text="Введите регион",
        unique=True,
    )

    class Meta:
        verbose_name = "регион"
        verbose_name_plural = "регионы"

    def __str__(self):
        return self.region


class Spot(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="пользователь",
        on_delete=models.CASCADE,
    )
    region = models.ForeignKey(
        "Region",
        on_delete=models.CASCADE,
        related_name="spot_region",
        related_query_name="spot_region",
        default=None,
        blank=True,
        null=True,
        verbose_name="Регион",
        help_text="Выберите или добавьте регион",
    )
    name = models.CharField(
        verbose_name="название",
        max_length=150,
        validators=[validators.MaxLengthValidator(150)],
        help_text="Введите название",
    )
    text = RichTextField(
        verbose_name="Текст",
        help_text="Введите описание",
        validators=[MaxWordsValidator(1000)],
    )
    lat = models.FloatField(
        verbose_name="широта",
        help_text="Введите широту",
    )
    lon = models.FloatField(
        verbose_name="долгота",
        help_text="Введите долготу",
    )
    date_created = models.DateTimeField(
        verbose_name="дата создания места",
        auto_now_add=True,
    )
    status_free = models.BooleanField(
        verbose_name="платное",
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name="активный",
        null=True,
        default=False,
    )

    class Meta:
        ordering = ("region",)
        verbose_name = "объект"
        verbose_name_plural = "объекты"

    def clean(self) -> None:
        if (
            not self.id
            and Spot.objects.filter(
                lat__gt=self.lat - 0.005,
                lat__lt=self.lat + 0.005,
                lon__gt=self.lon - 0.005,
                lon__lt=self.lon + 0.005,
            ).exists()
        ):
            raise ValidationError("Объект уже существует")
        return super().clean()

    def save(
        self,
        *args,
        **kwargs,
    ):
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def forced_update(self, kwds):
        for key in kwds:
            self.__dict__[key] = kwds[key]


class SpotMainImage(models.Model):
    def upload_to(self, file_name):
        type_image = file_name.split(".")[1]
        return (
            f"reservoir/{self.spot.user.id}/{self.spot_id}/"
            f"{dateformat.format(timezone.now(), 'd_m_y_H_i', )}.{type_image}"
        )

    spot = models.OneToOneField(
        "Spot",
        on_delete=models.CASCADE,
        verbose_name="озеро",
        related_name="spot_mainimage",
        related_query_name="spot_mainimage",
    )

    image = models.ImageField(
        upload_to=upload_to,
        verbose_name="изображение",
    )

    @property
    def get_300x300px(self):
        return get_thumbnail(self.image, "300x300", crop="center", quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f"<img src=/media/{self.get_300x300px}/>",
            )
        return "Изображение не найдено/отсутсвует"

    @property
    def alter_img(self):
        if self.image:
            return f"{self.get_300x300px}"
        return None

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    fields = ["image_tmb"]

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"


class SpotImages(models.Model):
    def upload_to(self, file_name):
        type_image = file_name.split(".")[1]
        return (
            f"reservoir/{self.spot.user.id}/{self.spot_id}/"
            f"{dateformat.format(timezone.now(), 'd_m_y_H_i', )}.{type_image}"
        )

    spot = models.ForeignKey(
        "Spot",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="товар",
        related_query_name="spot_images",
        related_name="spot_images",
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

    @property
    def alter_img(self):
        if self.image:
            return f"/media/{self.get_300x300px}"
        return None

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    fields = ["image_tmb"]

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "изображения"
        verbose_name_plural = "изображения"
