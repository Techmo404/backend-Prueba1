from django.shortcuts import render, redirect, get_object_or_404
from .models import Visita
from .forms import VisitaForm
from datetime import date
# Obtiene los datos de visitas y lo renderiza en la variable visitas
def lista_visitas(request):
    visitas = Visita.objects.all() 
    return render(request, 'visitas/lista_visitas.html', {'visitas': visitas})
#Crea una instancia del formulario
def nueva_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm()
    return render(request, 'visitas/nueva_visita.html', {'form': form})
#Busca si el id es valido y elimina una visita
def eliminar_visita(request, visita_id):
    visita = get_object_or_404(Visita, id=visita_id)
    if request.method == "POST":
        visita.delete()
    return redirect('lista_visitas')
