from django.db import models


# All background task_id will saved here.
# So in case any scheduled task needs to be revoked then we'll find the task_id
# in this model

class TaskList(models.Model):
    task_name = models.CharField(max_length=50)
    task_id = models.CharField(max_length=50)
