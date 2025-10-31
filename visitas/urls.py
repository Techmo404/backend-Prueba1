from django.urls import path
from . import views
# urls principales, visita y eliminar visita
urlpatterns = [
    path("", views.lista_visitas, name="lista_visitas"),
    path("nueva/", views.nueva_visita, name="nueva_visita"),
    path("eliminar/<int:visita_id>/", views.eliminar_visita, name="eliminar_visita"),
    path('detalle/<int:visita_id>/', views.detalle_visita, name='detalle_visita'),
    path('visitas/editar/<int:id>/', views.editar_visita, name='editar_visita')
]
