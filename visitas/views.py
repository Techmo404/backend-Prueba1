from django.shortcuts import render, redirect, get_object_or_404
from .models import Visita
from .forms import VisitaForm
from datetime import date
from django.contrib import messages
# Obtiene los datos de visitas y lo renderiza en la variable visitas
def lista_visitas(request):
    visitas = Visita.objects.all() 
    return render(request, 'lista_visitas.html', {'visitas': visitas})
#Crea una instancia del formulario
def nueva_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm()
    return render(request, 'nueva_visita.html', {'form': form})

#Busca si el id es valido y elimina una visita
def eliminar_visita(request, visita_id):
    visita = get_object_or_404(Visita, id=visita_id)
    if request.method == "POST":
        visita.delete()
    return redirect('lista_visitas')

def detalle_visita(request, visita_id):
    visita = get_object_or_404(Visita, pk=visita_id)
    return render(request, 'detalle_visita.html', {'visita': visita})


def editar_visita(request, id):
    # Obtener la visita o devolver 404 si no existe
    visita = get_object_or_404(Visita, id=id)

    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ La visita se actualizó correctamente.")
            return redirect('lista_visitas')
        else:
            messages.error(request, "❌ Hubo un error al actualizar la visita. Revisa los campos e inténtalo nuevamente.")
    else:
        form = VisitaForm(instance=visita)

    # Enviar el formulario y el objeto visita al template
    return render(request, 'editar_visita.html', {
        'form': form,
        'visita': visita
    })