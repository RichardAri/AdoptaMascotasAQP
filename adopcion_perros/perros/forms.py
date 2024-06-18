from django import forms
from .models import Perro

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ['nombre', 'descripcion', 'imagen', 'temperamento', 'necesidades_especiales', 'tamano']
