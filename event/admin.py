import logging
from datetime import timedelta

from django.contrib import admin

from celery_app.background_email_constants import FIRST_REMINDER_HOUR, SECOND_REMINDER_MINUTE, FEEDBACK_REMINDER_MINUTE
from celery_app.tasks import schedule_background_email, skype_event_group_email, delete_previous_tasks
from event.models import Event, Registration, EventEmail

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
        """
        This method will make schedule of sending email 12 hours and 30
        minutes before the session and also send feedback email 30 minutes
        after the session
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """

        obj.save()
        # In case of editing the event deleting Previously scheduled tasks
        delete_previous_tasks(obj)

        # Scheduling First Reminder Email
        schedule_background_email(
            event=obj,
            start_timedelta=timedelta(hours=FIRST_REMINDER_HOUR),
            expire_timedelta=timedelta(hours=3),
            is_feedback_email=False
            # False meaning reminder email before event
        )

        # Scheduling Second Reminder Email
        schedule_background_email(
            event=obj,
            start_timedelta=timedelta(minutes=SECOND_REMINDER_MINUTE),
            expire_timedelta=timedelta(minutes=30),
            is_feedback_email=False
            # False meaning reminder email before event
        )

        # Scheduling Feedback Reminder Email
        schedule_background_email(
            event=obj,
            start_timedelta=timedelta(minutes=FEEDBACK_REMINDER_MINUTE),
            expire_timedelta=timedelta(minutes=120),
            is_feedback_email=True
            # False meaning reminder email after event
        )


class EventEmailAdmin(admin.ModelAdmin):
    raw_id_fields = ('event',)

    def save_model(self, request, obj, form, change):
        """
        Calling this method to keep admin.py keep out of logic as much as possible
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        obj.save()
        skype_event_group_email.apply_async((obj.id,))


admin.site.register(Event, EventAdmin)
admin.site.register(Registration)
admin.site.register(EventEmail, EventEmailAdmin)
