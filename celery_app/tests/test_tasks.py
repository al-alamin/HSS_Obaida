from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import logging

from celery_app.tasks import send_mail_async, send_reminder_email,\
    skype_event_group_email, schedule_background_email
from event.models import Event, Registration, EventEmail
from celery_app.background_email_constants import FIRST_REMINDER_HOUR, SECOND_REMINDER_MINUTE, FEEDBACK_REMINDER_MINUTE

logger = logging.getLogger(__name__)
PRIMARY_ADMIN_EMAIL = settings.PRIMARY_ADMIN_EMAIL


class SendMailAsyncTest(TestCase):

    def setUp(self):
        self.subject = "Testing Email"
        self.body = "just body of testing Email"
        self.to_email = ["mdabdullahalalaminp@gmail.com"]
        self.from_email = PRIMARY_ADMIN_EMAIL

    def test_send_mail_async(self):
        response = send_mail_async(
            self.subject, self.body, self.to_email)
        self.assertTrue(response)


"""
    This is a helper method that will create a new skype event
    This new skype event will be usefull to test SendReminderEmailTest &
    ScheduleBackgrounEmailTest & EventEmailTest
    return: Event obj

"""


def create_new_skype_event():

    user_presenter = User.objects.create_user("alamin", "a@gmail.com")
    user_attendee = User.objects.create_user(
        "alamin2", "mdabdullahalalaminp@gmail.com")
    event = Event(title="test_event")
    event.presenter = user_presenter
    event.content_type = 'skype_session'
    event.start_time = timezone.now() + timedelta(hours=48)
    event.end_time = event.start_time + timedelta(hours=1)
    event.save()
    Registration.objects.create(event=event,
                                attendee=user_attendee, skype_id="skype_id")

    return event


class SendReminderEmailTest(TestCase):

    def setUp(self):
        self.event = create_new_skype_event()

    def test_send_reminder_email(self):
        response = send_reminder_email.delay(self.event.id, False)
        logging.info(response)
        self.assertTrue(response)

    def test_send_reminder_email_feedback(self):
        response = send_reminder_email.delay(self.event.id, True)
        logging.info(response)
        self.assertTrue(response)


class ScheduleBackgrounEmailTest(TestCase):

    def setUp(self):
        self.event = create_new_skype_event()

    def test_schedule_first_reminder_email(self):
        start_timedelta = timedelta(hours=FIRST_REMINDER_HOUR)
        expire_timedelta = timedelta(hours=3)
        response = schedule_background_email(self.event,
                                             start_timedelta,
                                             expire_timedelta, False)

        logging.info(response)
        self.assertTrue(response)

    def test_schedule_second_reminder_email(self):
        start_timedelta = timedelta(minutes=SECOND_REMINDER_MINUTE)
        expire_timedelta = timedelta(minutes=30)
        response = schedule_background_email(self.event,
                                             start_timedelta,
                                             expire_timedelta, False)

        logging.info(response)
        self.assertTrue(response)

    def test_schedule_feedback_reminder_email(self):
        start_timedelta = timedelta(minutes=FEEDBACK_REMINDER_MINUTE)
        expire_timedelta = timedelta(minutes=120)
        response = schedule_background_email(self.event,
                                             start_timedelta,
                                             expire_timedelta, True)

        logging.info(response)
        self.assertTrue(response)


class SkypeEventGroupEmailTest(TestCase):

    def setUp(self):
        self.event = create_new_skype_event()

        self.event_email = EventEmail.objects.create(
            event=self.event, email_subject="Hi", email_body="body")

    def test_skype_event_group_email(self):
        logger.info("testing the skype group email")
        response = skype_event_group_email.delay(self.event_email.id)
        self.assertTrue(response)
