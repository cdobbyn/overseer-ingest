from rest_framework.viewsets import ModelViewSet

from ingest.metrics.models import MetricCollection
from ingest.metrics.serializers import MetricCollectionSerializer


class MetricCollectionViewSet(ModelViewSet):
    queryset = MetricCollection.objects.all()
    serializer_class = MetricCollectionSerializer

