from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from cpu.views import UnixCpuMetricViewSet

router = DefaultRouter(trailing_slash=False)
router.register('metric/cpu', UnixCpuMetricViewSet)

schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('docs/', schema_view),
    path('', include(router.urls)),
]
