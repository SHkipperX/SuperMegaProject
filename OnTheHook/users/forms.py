from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm

from users.models import User


__all__ = [
    "CustomUserCreateForm",
    "CustomUserChangeForm",
]


class CustomUserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
        self.fields["location"].required = False

    class Meta:
        model = User
        fields = (
            User.username.field.name,
            User.email.field.name,
            User.location.field.name,
            "password1",
            "password2",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude = (
            User.avatar.field.name,
            User.password.field.name,
        )


class EditProfile(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
        self.fields["avatar"].required = False
        self.fields["location"].required = False

    class Meta:
        model = User
        fields = (
            User.first_name.field.name,
            User.last_name.field.name,
            User.email.field.name,
            User.location.field.name,
            User.avatar.field.name,
            User.birthday.field.name,
        )
