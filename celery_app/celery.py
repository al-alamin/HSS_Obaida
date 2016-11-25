from __future__ import absolute_import

from celery import Celery
from django.conf import settings  # noqa

app = Celery('MSNB',
             BROKER_URL='amqp://guest:guest@localhost:5672//',
             backend='amqp://',             
             )

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ENABLE_UTC=True,
)

# sqlite is not really capable of handling result backend. Will unlock the feature when moved to postgre
# app.conf.update(
#     CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
# )

# run celery worker from command line
# celery -A celery_app worker -l info
# celery commands
# http://docs.celeryproject.org/en/latest/userguide/monitoring.html#commands