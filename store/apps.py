from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    # for signals coming from the core app
    def ready(self) -> None:
        import store.signals.handlers
