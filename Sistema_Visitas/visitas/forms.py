from django import forms
from .models import Visita
import re
# diseño y el formulario de nueva visita
class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['nombre', 'rut', 'motivo_visita', 'hora_entrada', 'hora_salida']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full border-2 border-black rounded-md p-2 mt-1 text-black'
            }),
            'rut': forms.TextInput(attrs={
                'class': 'w-full border-2 border-black rounded-md p-2 mt-1 text-black',
                'placeholder': 'Ej: 12345678-9'
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
# verifica que el rut sea valido 
    def clean_rut(self):
        rut = self.cleaned_data['rut']
        rut = rut.replace(".", "").replace("-", "").upper()
        if len(rut) < 2:
            raise forms.ValidationError("RUT demasiado corto.")

        num, dv = rut[:-1], rut[-1]

        try:
            num = int(num)
        except ValueError:
            raise forms.ValidationError("RUT inválido.")
#verifica que el rut sea real
        suma = 0
        multiplicador = 2
        for digit in reversed(str(num)):
            suma += int(digit) * multiplicador
            multiplicador += 1
            if multiplicador > 7:
                multiplicador = 2

        dv_calculado = 11 - (suma % 11)
        if dv_calculado == 11:
            dv_calculado = "0"
        elif dv_calculado == 10:
            dv_calculado = "K"
        else:
            dv_calculado = str(dv_calculado)

        if dv != dv_calculado:
            raise forms.ValidationError("RUT inválido.")

        # Devolver en formato estándar con guión
        return f"{num}-{dv}"
