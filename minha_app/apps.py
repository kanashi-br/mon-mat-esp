from django.apps import AppConfig


class MinhaAppConfig(AppConfig):
    name = 'minha_app'
    def ready(self):
        import minha_app.signals