from django.contrib import admin

from cpu import UnixCpuMetricPerSecond, UnixCpuMetricPerMinute, UnixCpuMetricPerHour, \
    UnixCpuMetricPerFiveMinutes


class UnixCpuAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('host', 'cpu_id', 'timestamp')
        }),
        ('Metrics', {
            'fields': (
                'guest', 'guest_nice', 'idle', 'iowait', 'irq', 'nice',
                'softirq', 'steal', 'system', 'user', 'total_usage'
            )
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('uid',)
        })
    )
    readonly_fields = ('uid',)


@admin.register(UnixCpuMetricPerSecond)
class UnixCpuMetricPerSecondAdmin(UnixCpuAdmin):
    pass


@admin.register(UnixCpuMetricPerMinute)
class UnixCpuMetricPerMinuteAdmin(UnixCpuAdmin):
    pass


@admin.register(UnixCpuMetricPerFiveMinutes)
class UnixCpuMetricPerFiveMinutesAdmin(UnixCpuAdmin):
    pass


@admin.register(UnixCpuMetricPerHour)
class UnixCpuMetricPerHourAdmin(UnixCpuAdmin):
    pass
