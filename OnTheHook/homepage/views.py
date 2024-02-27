from django.views.generic import TemplateView

__all__ = []


class HomepageView(TemplateView):
    template_name = "homepage/index.html"
