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
        fields = ['beneficiary', 'material', 'loaned_date', 'returned', 'returned_date']
        labels = {
            'beneficiary': _('Beneficiado'),
            'material': _('Material'),
            'loaned_date': _('Data do empréstimo'),
            'returned': _('Devolvido?'),
            'returned_date': _('Data de devolução')
        }
        widgets = {
            'loaned_date': forms.DateInput(
                attrs={
                    'autocomplete': 'off'
                },
            ),
            'returned_date': forms.DateInput(
                attrs={
                    'autocomplete': 'off'
                },
            )
        }