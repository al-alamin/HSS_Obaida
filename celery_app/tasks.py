from __future__ import absolute_import
import logging

from celery import shared_task
from celery_app.models import TaskList

from event.models import Registration, Event, EventEmail
from common.utils import send_mail
from MSNB.celery import app

from celery_app.background_email_constants import BODY_REMAINDER,\
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
    logger.info("\n\nGoing to send remainder email event\n\n")
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


def delete_previous_tasks(event, parent_task_name):
    task_list = TaskList.objects.filter(parent_task_name=parent_task_name)
    if(task_list):
        for task in task_list:
            app.control.revoke(task.celery_task_id)
            logger.info(
                "\nabout to delete task_id " + str(task.celery_task_id))
            task.delete()


def schedule_background_email(event, parent_task_name, start_timedelta,
                              expire_timedelta, is_feedback_email):

    if(is_feedback_email):
        reminder_start_time = event.end_time + start_timedelta
    else:
        reminder_start_time = event.start_time - start_timedelta

    reminder_expire_time = reminder_start_time + expire_timedelta

    remainder_task_id = send_remainder_email.apply_async(
        (event.id, is_feedback_email), eta=reminder_start_time,
        expires=reminder_expire_time)
    # Creating tasking so that can revoke it later
    TaskList.objects.create(
        parent_task_name=parent_task_name,
        celery_task_id=remainder_task_id.task_id)

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
