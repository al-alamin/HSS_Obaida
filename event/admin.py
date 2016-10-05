from datetime import timedelta
import logging


from django.contrib import admin

from event.models import Event, Registration, EventEmail
from celery_app.tasks import schedule_background_email, add,\
    skype_event_group_email, delete_previous_tasks
from celery_app.background_email_constants import FIRST_REMAINDER_HOUR,\
    SECOND_REMAINDER_MINUTE,\
    FEEDBACK_REMAINDER_MINUTE

logger = logging.getLogger(__name__)


class RegistrationInline(admin.TabularInline):
    model = Registration


class EventAdmin(admin.ModelAdmin):
    inlines = [RegistrationInline]
    raw_id_fields = ('presenter',)

    # Here the save model is going to be overwritten. When someone creates or
    # edits a event this method is going to be called. When new event is
    # created or existing event is edited the background email scheduling is
    # going to be created or updated too. Here that background task is going
    # to be created or updated.

    def save_model(self, request, obj, form, change):
        obj.save()

        # This method will make schedule of sending email 12 hours and 30
        # minutes before the session and also send feedback email 30 minutes
        # after the session
        parent_task_name = "event_parent_task_name " + str(obj.id)
        # In case of editing the event deleting Previously scheduled tasks
        delete_previous_tasks(obj, parent_task_name)
        # Scheduling First Reminder Email
        schedule_background_email(
            event=obj,
            parent_task_name=parent_task_name,
            start_timedelta=timedelta(hours=FIRST_REMAINDER_HOUR),
            expire_timedelta=timedelta(hours=3),
            is_feedback_email=False 
            # False meaning reminder email before event
        )
        # Scheduling Second Reminder Email
        schedule_background_email(
            event=obj,
            parent_task_name=parent_task_name,
            start_timedelta=timedelta(minutes=SECOND_REMAINDER_MINUTE),
            expire_timedelta=timedelta(minutes=30),
            is_feedback_email=False
            # False meaning reminder email before event
        )
        # Scheduling Feedback Reminder Email
        schedule_background_email(
            event=obj,
            parent_task_name=parent_task_name,
            start_timedelta=timedelta(minutes=FEEDBACK_REMAINDER_MINUTE),
            expire_timedelta=timedelta(minutes=120),
            is_feedback_email=True
            # False meaning reminder email after event
        )

        # This is for testing and debug purpose can be deleted in production
        # site
        add.apply_async((15, 5), countdown=5)


class EventEmailAdmin(admin.ModelAdmin):
    raw_id_fields = ('event',)

    def save_model(self, request, obj, form, change):
        obj.save()
        # Calling this method to keep admin.py keep out of logic as much as
        # possible
        skype_event_group_email.apply_async((obj.id,))


admin.site.register(Event, EventAdmin)
admin.site.register(Registration)
admin.site.register(EventEmail, EventEmailAdmin)
