from django import forms
from .models import Link

class FormLinks(forms.ModelForm):
    class Meta:
        required_css_class = 'input'
        model = Link
        fields = "__all__"

