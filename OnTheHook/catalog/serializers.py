from rest_framework import serializers

from catalog import models

__all__ = []


class CatalogSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(source="spot_mainimage.image")

    class Meta:
        model = models.Spot
        fields = [
            "id",
            "name",
            "text",
            "region",
            "lat",
            "lon",
            "date_created",
            "status_free",
            "user",
            "img",
        ]


class MainImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SpotMainImage
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = "__all__"
