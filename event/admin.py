from datetime import timedelta
import logging

logger = logging.getLogger(__name__)
from django.contrib import admin

from django.utils import timezone

from MSNB.celery import app
from celery_app.models import TaskList
from skype_consultancy.tasks import send_remainder_email, send_feedback_remainder_email
from skype_consultancy.tasks import add, skype_event_group_email
from event.models import Event, Registration, EventEmail


class RegistrationInline(admin.TabularInline):
    model = Registration


class EventAdmin(admin.ModelAdmin):
    inlines = [RegistrationInline]
    raw_id_fields = ('presenter',)

    # Here the save model is going to be overwritten. When someone creates or edits
    # edits a event this method is going to be called. When new event is created or
    # existing event is edited the background email scheduling is going to be
    # created or updated too. Here that background task is going to be created
    # or updated.

    # going to make a schedule to send email before 12 hours by synchoneously
    # calling send_remainder_email
    def schedule_first_remainder_email(self, obj, task_name):

        first_reminder_time_hour_amount = 12
        first_reminder_time = obj.start_time - \
            timedelta(hours=first_reminder_time_hour_amount)
        first_reminder_time_expire = first_reminder_time + timedelta(hours=3)

        first_remainder_id = send_remainder_email.apply_async(
            (obj.id,), eta=first_reminder_time,
            expires=first_reminder_time_expire)  # event_id
        # Creating tasking so that can revoke it later
        TaskList.objects.create(
            task_name=task_name, task_id=first_remainder_id.task_id)

    def schedule_second_remainder_email(self, obj, task_name):

        second_reminder_time_minute_amount = 30
        second_reminder_time = obj.start_time - \
            timedelta(minutes=second_reminder_time_minute_amount)
        second_reminder_time_expire = second_reminder_time + \
            timedelta(minutes=30)
        # 30 minutes after the event
        second_remainder_id = send_remainder_email.apply_async(
            (obj.id,), eta=second_reminder_time,
            expires=second_reminder_time_expire)  # event_id, minute
        # Creating tasking so that can revoke it later
        TaskList.objects.create(
            task_name=task_name, task_id=second_remainder_id.task_id)

    def schedule_feedback_remainder_email(self, obj, task_name):

        feedback_reminder_time_minute_amount = 30
        feedback_reminder_time = obj.end_time + \
            timedelta(minutes=feedback_reminder_time_minute_amount)
        feedback_reminder_time_expire = feedback_reminder_time + \
            timedelta(hours=3)
        feedback_remainder_id = send_feedback_remainder_email.apply_async(
            (obj.id,), eta=feedback_reminder_time,
            expires=feedback_reminder_time_expire)

        # Creating tasking so that can revoke it later
        TaskList.objects.create(
            task_name=task_name, task_id=feedback_remainder_id.task_id)

    def save_model(self, request, obj, form, change):
        obj.save()

        # Going to delete the previously scheduled tasks on this event
        task_name = "event_task_name " + str(obj.id)
        task_list = TaskList.objects.filter(task_name=task_name)
        if(task_list):
            for task in task_list:
                app.control.revoke(task.task_id)
                logger.info("\n\nabout to delete task_id " + str(task.task_id))
                task.delete()

        # Going to make background schedule by calling these methods
        self.schedule_first_remainder_email(obj, task_name)
        self.schedule_feedback_remainder_email(obj, task_name)
        self.schedule_feedback_remainder_email(obj, task_name)

        # This is for testing and debug purpose can be deleted in production
        # site
        add.apply_async((15, 5), countdown=5)


class EventEmailAdmin(admin.ModelAdmin):
    raw_id_fields = ('event',)

    def save_model(self, request, obj, form, change):
        obj.save()
        skype_event_group_email.apply_async((obj.id,))


admin.site.register(Event, EventAdmin)
admin.site.register(Registration)
admin.site.register(EventEmail, EventEmailAdmin)
