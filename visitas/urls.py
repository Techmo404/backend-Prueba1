from django.urls import include,path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"Visita", views.VisitaViewSet)
urlpatterns = [
    path("", views.lista_visitas, name="lista_visitas"),
    path("nueva/", views.nueva_visita, name="nueva_visita"),
    path("eliminar/<int:visita_id>/", views.eliminar_visita, name="eliminar_visita"),
    path('detalle/<int:visita_id>/', views.detalle_visita, name='detalle_visita'),
    path('visitas/editar/<int:id>/', views.editar_visita, name='editar_visita')
]
