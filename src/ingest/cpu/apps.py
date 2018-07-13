from django.apps import AppConfig


class CpuMetricsConfig(AppConfig):
    name = 'cpu'

    def ready(self):
        pass
