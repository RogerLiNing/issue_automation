from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import EventPayLoad


@shared_task()
def handle_event(data):
    event = EventPayLoad(payload=data)
    event.save()

