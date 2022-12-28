from django.utils.translation import gettext_lazy as _
from django import forms
from .models import *

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'qnt']
        labels = {
            'name': _('Nome'),
            'qnt': _('Quantidade'),
        }

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['beneficiary', 'material', 'responsible']
        labels = {
            'beneficiary': _('Beneficiado'),
            'material': _('Material'),
            'responsible': _('Responsável'),
            
        }