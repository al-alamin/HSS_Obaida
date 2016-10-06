from django.contrib import admin

from celery_app.models import TaskList
# Register your models here.


admin.site.register(TaskList)
