from __future__ import absolute_import
import logging

logger = logging.getLogger(__name__)
from celery import shared_task

from event.models import Registration, Event, EventEmail
from common.utils import send_mail
from MSNB.celery import app


@app.task
def send_mail_async(subject, body_email, to_email):
    # This is just a helper function to send email async.
    # See the output in the worker process console
    logger.info("\n\n Goint to send email asynconously\n\n")
    return send_mail(subject, body_email, to_email)


@app.task
def send_remainder_email(event_id):
    # Change and updat the body_email make it more customized
    logger.info("\n\nGoing to send remainder email before ")
    event = Event.objects.get(id=int(event_id))
    registered_user_list = Registration.objects.filter(event=event)
    logger.info(registered_user_list)
    for reg_user in registered_user_list:
        to_email = [reg_user.attendee.email, ]
        subject = "Your event registration Remainder for the event {0}".format(
            event.title)

        body_email = """
                     Hi {0},
                     Your Remainder for the event {1}.
                     The event will be held on {2} Bangladesh time.
                     The event duration is {3} hour/ hours.
                     Our Skype ID is 'MSNB'.
                     For any query please email at support@mystudynotebook.com.
                     Please don't forget to receive video call from our Skype account at the mentioned time.

                     Thanks,
                     Support Team
                     My Study Notebook
                     """.format(reg_user.attendee.first_name, event.title,
                                event.start_time, event.duration)
        send_mail(subject, body_email, to_email)


# Remainder Email and Feedback remainder's emails subject body will be
# significantly different. Thats why there are two methods to edit and
# customize these two type email

@app.task
def send_feedback_remainder_email(event_id):
    logger.info("\n\nGoing to send feedback remainder email ")
    event = Event.objects.get(id=int(event_id))
    registered_user_list = Registration.objects.filter(event=event)
    logger.info(registered_user_list)
    for reg_user in registered_user_list:
        to_email = [reg_user.attendee.email, ]
        subject = "Your Feedback Remainder for the event {0}".format(
            event.title)
        body_email = """
                     Hi {0},
                     Congratulation for participation on the event {1}.
                     The event was held on {2} Bangladesh time.
                     The event duration is {3} hour/ hours.
                     Our Skype ID is 'MSNB'.
                     For any query please email at support@mystudynotebook.com.
                     Please don't forget to receive video call from our Skype account at the mentioned time.
                     Thanks for Joing our sessiong.
                     Give us your feed back.
                     Thanks,
                     Support Team
                     My Study Notebook
                     """.format(reg_user.attendee.first_name, event.title,
                                event.start_time, event.duration)
        send_mail(subject, body_email, to_email)


@app.task
def skype_event_group_email(event_email_id):
    logger.info("\n\n In Skype group Email \n")
    event_email = EventEmail.objects.get(id=event_email_id)
    registered_user_list = Registration.objects.filter(event=event_email.event)
    print(registered_user_list)
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
