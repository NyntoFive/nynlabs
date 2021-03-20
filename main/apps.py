from django.apps import AppConfig


class MainConfig(AppConfig):
    name = "main"

    # Register thumbnail signals with app @launch
    def ready(self):
        from . import signals
