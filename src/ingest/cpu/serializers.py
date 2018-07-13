from rest_framework import serializers

from cpu import UnixCpuMetricPerSecond


class UnixCpuMetricPerSecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnixCpuMetricPerSecond
        fields = '__all__'
