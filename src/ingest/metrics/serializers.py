from rest_framework import serializers

from ingest.metrics.models import MetricCollection


class MetricCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricCollection
        fields = '__all__'
