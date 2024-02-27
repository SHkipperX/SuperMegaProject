from django import forms
from django.forms import ModelForm
from rating.models import SpotRating

__all__ = []


class SpotRatingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["mark"].required = False
        self.fields["images"].widget.attrs["multiple"] = True
        if not self.instance.__dict__.get("id"):
            self.fields["mark"].initial = 5

    images = forms.ImageField(
        label="Картиночки места",
        help_text="необязательно",
        required=False,
    )

    class Meta:
        model = SpotRating
        fields = (
            SpotRating.mark.field.name,
            SpotRating.comment.field.name,
        )
        widgets = {
            SpotRating.mark.field.name: forms.widgets.Select(
                attrs={
                    "class": "form-select text-center",
                    "required": False,
                },
            ),
            SpotRating.comment.field.name: forms.widgets.Select(
                attrs={
                    "class": "form-select text-center",
                    "required": False,
                },
            ),
            "images": forms.FileField(widget=forms.ClearableFileInput()),
        }
