from __future__ import absolute_import
from datetime import timedelta
import logging

from celery import shared_task
from celery_app.models import TaskList

from event.models import Registration, Event, EventEmail
from common.utils import send_mail
from MSNB.celery import app

from skype_consultancy.background_email_constants import FIRST_REMAINDER_HOUR,\
    SECOND_REMAINDER_MINUTE,\
    FEEDBACK_REMAINDER_MINUTE,\
    BODY_REMAINDER,\
    BODY_FEEDBACK,\
    SUBJECT_REMAINDER,\
    SUBJECT_FEEDBACK

logger = logging.getLogger(__name__)


@app.task
def send_mail_async(subject, body_email, to_email):
    # This is just a helper function to send email async.
    # See the output in the worker process console
    logger.info("\n\n skype_consutancy.tasks.send_mail.async method\n\n")
    return send_mail(subject, body_email, to_email)


@app.task
def send_remainder_email(event_id, is_feedback_email):
    # Change and updat the body_email make it more customized
    logger.info("\n\nGoing to send remainder email before event\n\n")
    event = Event.objects.get(id=int(event_id))
    registered_user_list = Registration.objects.filter(event=event)
    logger.info(registered_user_list)

    for reg_user in registered_user_list:
        to_email = [reg_user.attendee.email, ]
        if(is_feedback_email):
            subject = SUBJECT_FEEDBACK.format(event.title)
            body_email = BODY_FEEDBACK.format(reg_user.attendee.first_name,
                                              event.title,
                                              event.start_time,
                                              event.duration)
        else:
            subject = SUBJECT_REMAINDER.format(event.title)
            body_email = BODY_REMAINDER.format(reg_user.attendee.first_name,
                                               event.title,
                                               event.start_time,
                                               event.duration)

        send_mail(subject, body_email, to_email)


def schedule_background_email(event):
    task_name = "event_task_name " + str(event.id)

    # Deleting Previously Scheduled task in this event
    task_list = TaskList.objects.filter(task_name=task_name)
    if(task_list):
        for task in task_list:
            app.control.revoke(task.task_id)
            logger.info("\nabout to delete task_id " + str(task.task_id))
            task.delete()

    #  Scheduling first remainder email
    first_reminder_time = event.start_time - \
        timedelta(hours=FIRST_REMAINDER_HOUR)
    first_reminder_time_expire = first_reminder_time + timedelta(hours=3)

    first_remainder_id = send_remainder_email.apply_async(
        (event.id, False), eta=first_reminder_time,
        expires=first_reminder_time_expire)
    # Creating tasking so that can revoke it later
    TaskList.objects.create(
        task_name=task_name, task_id=first_remainder_id.task_id)

    # Scheduling second remainder email
    second_reminder_time = event.start_time - \
        timedelta(minutes=SECOND_REMAINDER_MINUTE)
    second_reminder_time_expire = second_reminder_time + \
        timedelta(minutes=30)
    # 30 minutes after the event
    second_remainder_id = send_remainder_email.apply_async(
        (event.id, False), eta=second_reminder_time,
        expires=second_reminder_time_expire)
    # Creating tasking so that can revoke it later
    TaskList.objects.create(
        task_name=task_name, task_id=second_remainder_id.task_id)

    # Scheduling feedback remainder Email
    feedback_reminder_time = event.end_time + \
        timedelta(minutes=FEEDBACK_REMAINDER_MINUTE)
    feedback_reminder_time_expire = feedback_reminder_time + \
        timedelta(hours=3)
    feedback_remainder_id = send_remainder_email.apply_async(
        (event.id, True), eta=feedback_reminder_time,
        expires=feedback_reminder_time_expire)

    # Creating tasking so that can revoke it later
    TaskList.objects.create(
        task_name=task_name, task_id=feedback_remainder_id.task_id)
    # True means successfully finished executing
    return True


@app.task
def skype_event_group_email(event_email_id):
    logger.info("\n\n In Skype group Email \n")
    event_email = EventEmail.objects.get(id=event_email_id)
    registered_user_list = Registration.objects.filter(event=event_email.event)
    logger.info(registered_user_list)
    for reg_user in registered_user_list:
        logger.info("\n\n group email for loop\n")
        to_email = [reg_user.attendee.email, ]
        subject = event_email.email_subject
        body_email = event_email.email_body
        send_mail(subject, body_email, to_email)

# This task is for practice purpose
# Shared tasks are not assotiated with app so they are easy to import from
# command line


@shared_task
def add(x=4, y=5):
    print("\n\n****** task add method")
    return x + y
