from django.apps import AppConfig

__all__ = []


class ModerationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "moderation"
    verbose_name = "модерация"
