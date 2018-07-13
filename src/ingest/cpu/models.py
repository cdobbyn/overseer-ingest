import uuid

from django.db import models


class AbstractCpuMetric(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField(max_length=255, db_index=True)
    cpu_id = models.CharField(max_length=50, db_index=True)
    timestamp = models.DateTimeField()

    class Meta:
        abstract = True


class UnixCpuMetric(AbstractCpuMetric):
    # Linux usage stats
    guest = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    guest_nice = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    idle = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    iowait = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    irq = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    nice = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    softirq = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    steal = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    system = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    user = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    total_usage = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)

    class Meta:
        abstract = True


class WindowsCpuMetric(AbstractCpuMetric):
    # Windows usage stats
    dpc = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    idle = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    interrupt = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    privileged = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    processor = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    user = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)

    class Meta:
        abstract = True


class UnixCpuMetricPerSecond(UnixCpuMetric):
    # Short lived data, lasting 4 hours, not visible to users.
    # 7,200 rows per node (60s * 60m * 2h)
    pass


class UnixCpuMetricPerMinute(UnixCpuMetric):
    # Medium lived data, lasting 7 days, visible to users.
    # 10,080 rows per node (60m * 24h * 7d)
    pass


class UnixCpuMetricPerFiveMinutes(UnixCpuMetric):
    # Medium lived data, lasting 30 days, visible to users.
    # 8,640 rows per node ((60m * 24h * 30d) / 5m)
    class Meta:
        verbose_name_plural = "Unix cpu metric per five minutes"


class UnixCpuMetricPerHour(UnixCpuMetric):
    # Long lived data, lasting 2 years, visible to users.
    # 12,288 rows per node (24h * 365d * 2y)
    pass
