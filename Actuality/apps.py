from django.apps import AppConfig


class ActualityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Actuality'
    
    def ready(self):
        import Actuality.signals
