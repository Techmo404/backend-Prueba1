from django.apps import AppConfig

# configura la clase visitas con campo automatico por defecto en claves primarias
class VisitasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visitas'
