from django.contrib import admin
from .models import Visita


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista principal
    list_display = ('nombre', 'rut', 'fecha', 'motivo_visita', 'motivo_corto', 'hora_entrada', 'hora_salida')
    
    # Campo editable directamente desde la lista
    list_editable = ('motivo_visita',)
    
    # Campos de búsqueda
    search_fields = ('nombre', 'rut', 'motivo_visita')
    
    # Filtros laterales
    list_filter = ('fecha',)
    
    # Orden de registros
    ordering = ('-fecha', 'hora_entrada')
    
    # Campos de solo lectura
    readonly_fields = ('hora_entrada', 'hora_salida')
    
    # Paginación
    list_per_page = 25

    # Secciones del formulario
    fieldsets = (
        ('Datos personales', {
            'fields': ('nombre', 'rut')
        }),
        ('Detalles de la visita', {
            'fields': ('motivo_visita', 'fecha', 'hora_entrada', 'hora_salida'),
            'classes': ('collapse',)
        }),
    )

    # Muestra abreviada del motivo
    @admin.display(description='Motivo (Resumen)')
    def motivo_corto(self, obj):
        return (obj.motivo_visita[:40] + '...') if len(obj.motivo_visita) > 40 else obj.motivo_visita
