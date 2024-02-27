from django.contrib import messages
from django.contrib.auth.backends import ModelBackend

from users.models import User

__all__ = []


class ModifyLogin(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        get_user = None

        try:
            try:
                get_user = User.objects.get(username=username)
            except Exception:
                mail = User.objects.normalize_email(username)
                get_user = User.objects.by_mail(mail)
        except User.DoesNotExist:
            messages.error(request, "Неверный логин или пароль!")
            return None

        if get_user.check_password(password) and get_user.is_active:
            return get_user
        messages.error(request, "Неверный логин или пароль!")
        return None

    def get_user(self, username):
        try:
            return User.objects.get(pk=username)
        except User.DoesNotExist:
            return None
