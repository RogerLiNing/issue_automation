from django.db import models


class EventPayLoad(models.Model):
    payload = models.TextField(null=True)

    def __str__(self):
        return self.payload[:10]
