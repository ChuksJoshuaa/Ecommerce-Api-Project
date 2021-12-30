from django.apps import AppConfig


class CoreCustomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self) -> None:
        import core.signals.handlers
