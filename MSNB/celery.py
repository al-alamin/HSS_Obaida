from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings  # noqa

app = Celery('MSNB',
             BROKER_URL='amqp://guest:guest@localhost:5672//',
             backend='amqp://',
             CELERY_RESULT_BACKEND='redis://localhost:6379/0',
             )

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Oslo',
    CELERY_ENABLE_UTC=True,
)
