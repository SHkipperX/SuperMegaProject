from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from users.forms import CustomUserChangeForm, CustomUserCreateForm
from users.models import User


__all__ = []


class UserAdministrator(auth_admin.UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        "id",
        User.username.field.name,
        User.is_staff.field.name,
        User.is_active,
    )
    exclude = ("password",)


admin.site.register(User)
