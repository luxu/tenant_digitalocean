from django import forms

from empresa.models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'name',
            'cnpj'
        ]
