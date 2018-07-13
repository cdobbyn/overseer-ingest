from django.apps import AppConfig


class MetricsConfig(AppConfig):
    name = 'ingest.metrics'

    def ready(self):
        pass
