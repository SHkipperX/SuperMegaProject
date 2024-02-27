from rest_framework import permissions, viewsets

from catalog import models, serializers

__all__ = []


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = models.Spot.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CatalogSerializer


class MainImageViewSet(viewsets.ModelViewSet):
    queryset = models.SpotMainImage.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.MainImageSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = models.Region.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.RegionSerializer
