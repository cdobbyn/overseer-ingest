import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField


class MetricCollection(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    json = JSONField()