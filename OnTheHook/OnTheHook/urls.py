from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(
        "",
        include("homepage.urls"),
    ),
    path(
        "auth/",
        include("users.urls"),
    ),
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "",
        include("social_django.urls"),
    ),
    path(
        "catalog/",
        include("catalog.urls"),
    ),
    path(
        "moderation/",
        include("moderation.urls"),
    ),
    path(
        "map/",
        include("map.urls"),
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
