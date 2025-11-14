from django.urls import include,path
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r"Visita", views.VisitaViewSet)
urlpatterns = [
    path("", views.lista_visitas, name="lista_visitas"),
    path("nueva/", views.nueva_visita, name="nueva_visita"),
    path("eliminar/<int:visita_id>/", views.eliminar_visita, name="eliminar_visita"),
    path('detalle/<int:visita_id>/', views.detalle_visita, name='detalle_visita'),
    path('visitas/editar/<int:id>/', views.editar_visita, name='editar_visita'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
