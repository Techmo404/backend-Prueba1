from django import forms
from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['nombre', 'rut', 'motivo_visita', 'hora_entrada', 'hora_salida']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full border-2 border-black rounded-md p-2 mt-1 text-black'
            }),
            'rut': forms.TextInput(attrs={
                'class': 'w-full border-2 border-black rounded-md p-2 mt-1 text-black'
            }),
            'motivo_visita': forms.Textarea(attrs={
                'class': 'w-full border-2 border-black rounded-md p-2 mt-1 text-black',
                'rows': 4,
                'placeholder': 'Ingrese el motivo de la visita...'
            }),
            'hora_entrada': forms.TimeInput(attrs={
                'class': 'w-full border-2 border-black rounded-md p-2 mt-1 text-black', 
                'type': 'time'
            }),
            'hora_salida': forms.TimeInput(attrs={
                'class': 'w-full border-2 border-black rounded-md p-2 mt-1 text-black',
                'type': 'time'
            }),
        }
