from django.db.models.signals import pre_save
from django.dispatch import receiver

from cpu import UnixCpuMetricPerSecond, UnixCpuMetricPerMinute, UnixCpuMetricPerHour, \
    UnixCpuMetricPerFiveMinutes


@receiver(pre_save, sender=UnixCpuMetricPerSecond)
@receiver(pre_save, sender=UnixCpuMetricPerMinute)
@receiver(pre_save, sender=UnixCpuMetricPerFiveMinutes)
@receiver(pre_save, sender=UnixCpuMetricPerHour)
def calculate_unix_total_callback(sender, instance, *args, **kwargs):
    cpu_time = sum((
        instance.user, instance.nice, instance.system,
        instance.idle, instance.iowait, instance.irq,
        instance.softirq, instance.steal))
    idle_time = sum((
        instance.idle, instance.iowait
    ))
    instance.total_usage = cpu_time - idle_time

