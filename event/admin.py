from datetime import timedelta

from django.contrib import admin
from event.models import Event, Registration, SkypeEmail
# from kombu.transport.django import models as kombu_models
from django.utils import timezone

from MSNB.celery import app
from common.models import TaskList
from skype_consultancy.tasks import send_skype_email_after_mintue, send_skype_email_before_hour, send_skype_email_before_mintue
from skype_consultancy.tasks import add, skype_event_group_email

# send_skype_email_before_hour
#     send_skype_email_before_mintue
# Register your models here.


class RegistrationInline(admin.TabularInline):
    model = Registration


class EventAdmin(admin.ModelAdmin):
    inlines = [RegistrationInline]
    raw_id_fields = ('presenter',)

    def save_model(self, request, obj, form, change):
        obj.save()

        # Going to delete the previously scheduled tasks on this event
        task_name = "event->" + str(obj.id)
        task_list = TaskList.objects.filter(task_name=task_name)
        if(task_list):
            for task in task_list:                
                app.control.revoke(task.task_id)
                print("\n\nabout to delete task_id " + str(task.task_id))
                task.delete()
        # Previous tasks revoked and deleted from task_list

        # Try to send email before 12 hours but for some reasons if it fails then
        # After 3 hours trying ie 9 hours before the event it will not try to send
        # any more
        time_hour = obj.start_time - timedelta(hours=12)
        time_hour_expire = time_hour + timedelta(hours=3)
        # 30 minutes before the event
        time_minute_before = obj.start_time - timedelta(minutes=30)
        time_minute_before_expire = time_minute_before + timedelta(minutes=30)
        # 30 minutes after the event
        time_minute_after = obj.end_time + timedelta(minutes=30)
        time_minute_after_expire = time_minute_after + timedelta(hours=3)

        before_hour_id = send_skype_email_before_hour.apply_async(
            (obj.id,), eta=time_hour, expires=time_hour_expire)  # event_id
        before_minute_id = send_skype_email_before_mintue.apply_async(
            (obj.id,), eta=time_minute_before, expires=time_minute_before_expire)  # event_id, minute
        after_minute_id = send_skype_email_after_mintue.apply_async(
            (obj.id,), eta=time_minute_after, expires=time_minute_after_expire)

        # # Now We'll save these 3 scheduled task id to task list DB so that we
        # # can revoke it later if the event is edited.
        TaskList.objects.create(
            task_name=task_name, task_id=before_hour_id.task_id)
        TaskList.objects.create(
            task_name=task_name, task_id=before_minute_id.task_id)
        TaskList.objects.create(
            task_name=task_name, task_id=after_minute_id.task_id)

        # send_skype_email_before_mintue.apply_async(
        #     (obj.id,), eta=timezone.now() + timedelta(minutes=2))

        add.apply_async((15, 5), countdown=5)


class SkypeEmailAdmin(admin.ModelAdmin):
    raw_id_fields = ('event',)

    def save_model(self, request, obj, form, change):
        obj.save()
        skype_event_group_email.apply_async(
            (obj.id,))


admin.site.register(Event, EventAdmin)
admin.site.register(Registration)
# admin.site.register(kombu_models.Message)
admin.site.register(SkypeEmail, SkypeEmailAdmin)
