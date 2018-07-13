from rest_framework.viewsets import ModelViewSet

from cpu import UnixCpuMetricPerSecond
from cpu import UnixCpuMetricPerSecondSerializer


class UnixCpuMetricViewSet(ModelViewSet):
    queryset = UnixCpuMetricPerSecond.objects.all()
    serializer_class = UnixCpuMetricPerSecondSerializer

