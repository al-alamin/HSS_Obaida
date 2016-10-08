from __future__ import absolute_import

import logging

from celery import shared_task

from celery_app.background_email_constants import (BODY_REMINDER, BODY_FEEDBACK, SUBJECT_REMINDER, SUBJECT_FEEDBACK,
                                                   BD_TZ, time_format)
from celery_app.celery import app
from celery_app.models import TaskList
from common.utils import send_mail
from event.models import Registration, Event, EventEmail

logger = logging.getLogger(__name__)


@app.task
def send_mail_async(subject, body_email, to_email):
    # This is just a helper function to send email async.
    # See the output in the worker process console
    return send_mail(subject, body_email, to_email)


@app.task
def send_reminder_email(event_id, is_feedback_email):
    """

    :param event_id:
    :param is_feedback_email:
    :return:
    """
    # Change and update the body_email make it more customized

    event = Event.objects.get(id=int(event_id))
    registered_user_list = Registration.objects.filter(event=event)

    for reg_user in registered_user_list:
        to_email = [reg_user.attendee.email, ]

        if is_feedback_email:
            subject = SUBJECT_FEEDBACK
            body_email = BODY_FEEDBACK.format(reg_user.attendee.first_name, event.title)
        else:
            event_start_time = event.start_time.astimezone(BD_TZ).strftime(time_format)
            subject = SUBJECT_REMINDER.format(event.title)
            body_email = BODY_REMINDER.format(reg_user.attendee.first_name, event.title,
                                              event_start_time, event.duration)

        send_mail(subject, body_email, to_email)


def delete_previous_tasks(event):
    """

    :param parent_task_name:
    :return:
    """
    task_list = TaskList.objects.filter(parent_task_name=event.name_task)
    if task_list:
        for task in task_list:
            app.control.revoke(task.celery_task_id)
            task.delete()
            logger.info("Deleted task {0} of parent task{1}".format(task.celery_task_id, event.name_task))


def schedule_background_email(event, start_timedelta, expire_timedelta, is_feedback_email):
    """

    :param event:
    :param start_timedelta:
    :param expire_timedelta:
    :param is_feedback_email:
    :return:
    """
    reminder_start_time = event.end_time + start_timedelta if is_feedback_email else event.start_time - start_timedelta
    reminder_expire_time = reminder_start_time + expire_timedelta

    reminder_task_id = send_reminder_email.apply_async((event.id, is_feedback_email), eta=reminder_start_time,
                                                       expires=reminder_expire_time)
    # Creating tasking so that can revoke it later
    TaskList.objects.create(parent_task_name=event.name_task, celery_task_id=reminder_task_id.task_id)

    return True


@app.task
def skype_event_group_email(event_email_id):
    """

    :param event_email_id:
    :return:
    """
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
