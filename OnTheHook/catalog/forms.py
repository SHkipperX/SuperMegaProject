from ckeditor.widgets import CKEditorWidget
from django import forms

from catalog.models import Spot

__all__ = []


class SpotForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["images"].widget.attrs["multiple"] = True
        self.fields["images"].widget.attrs["required"] = False
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    images = forms.ImageField(
        label="Картинки",
        required=False,
    )

    class Meta:
        model = Spot
        exclude = (
            Spot.user.field.name,
            Spot.date_created.field.name,
            Spot.is_active.field.name,
        )

        widgets = {Spot.text.field.name: CKEditorWidget()}
