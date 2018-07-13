from django.contrib import admin

from ingest.metrics.models import MetricCollection


@admin.register(MetricCollection)
class MetricCollectionAdmin(admin.ModelAdmin):
    pass
