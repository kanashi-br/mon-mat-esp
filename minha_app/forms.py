from django.utils.translation import gettext_lazy as _
from django import forms
from .models import *

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'qnt']
        