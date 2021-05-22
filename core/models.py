import uuid
from django.db import models


class UUID(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uuid

    class Meta:
        ordering = ['-timestamp']