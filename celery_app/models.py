from django.db import models


# All background task_id will saved here.
# So in case any scheduled task needs to be revoked then we'll find the task_id
# in this model

class TaskList(models.Model):
    parent_task_name = models.CharField(max_length=50)
    celery_task_id = models.CharField(max_length=50)
