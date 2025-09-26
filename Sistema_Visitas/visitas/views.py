from django.shortcuts import render, redirect
from .models import Visita
from .forms import VisitaForm
from datetime import date

def lista_visitas(request):
    visitas = Visita.objects.filter()
    return render(request, 'visitas/lista_visitas.html', {'visitas': visitas})

def nueva_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm()
    return render(request, 'visitas/nueva_visita.html', {'form': form})
