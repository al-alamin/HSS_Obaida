from django.contrib.auth.models import User
from django.db import models

class Type(models.Model):
    """
    It's like parent category for category and tag. eg, Visa, Higher Study
    """
    name = models.CharField(max_length=50, help_text='parent category for category and tag. eg, Visa, Higher Study')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, blank=True, null=True)

    def __str__(self):
        return self.name


# All background task_id will saved here.
# So in case any scheduled task needs to be revoked then we'll find the task_id
# in this model
class TaskList(models.Model):
    task_name = models.CharField(max_length=50)
    task_id = models.CharField(max_length=50)
