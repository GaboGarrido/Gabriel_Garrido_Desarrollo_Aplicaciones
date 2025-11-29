from django import forms
from .models import Actividad


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['titulo', 'descripcion', 'completada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'completada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
