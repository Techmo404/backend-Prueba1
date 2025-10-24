from django.contrib import admin

from django.contrib import admin
from .models import Visita
#permite registrar el modelo visita en el panel de administracion
# admin.site.register(Visita)

# Register your models here.
@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('nombre','rut','fecha','motivo_visita')
    list_filter = ('fecha',)
    search_fields = ('nombre','rut')
    list_editable = ('motivo_visita',)
    ordering = ('fecha',)
    readonly_fields = ('hora_entrada','hora_salida')

    fieldsets = (
        ('Persona', {'fields': ('nombre', 'rut')})
                 ,)
