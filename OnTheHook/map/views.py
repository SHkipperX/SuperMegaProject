from django.views.generic import TemplateView

__all__ = []


class MapView(TemplateView):
    template_name = "map/map.html"
