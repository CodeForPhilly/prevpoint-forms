from django import forms

from server.schema import form_map
from server.models import FormCompletion

FORM_CHOICES = [
    [slug, entry['title']]
    for slug, entry in form_map.items()
]

class TypeForm(forms.Form):
    title = "Select a form type"
    form_type = forms.ChoiceField(choices=FORM_CHOICES)

class UploadForm(forms.ModelForm):
    title = "Upload an image of the form"
    class Meta:
        fields = ('image',)
        model = FormCompletion
