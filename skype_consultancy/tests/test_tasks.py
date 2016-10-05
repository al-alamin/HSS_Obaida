from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
import logging

from skype_consultancy.tasks import send_mail_async, send_remainder_email,\
    skype_event_group_email, schedule_background_email
from event.models import Event, Registration, EventEmail

logger = logging.getLogger(__name__)
PRIMARY_ADMIN_EMAIL = settings.PRIMARY_ADMIN_EMAIL


class SendMailAsyncTest(TestCase):

    def setUp(self):
        self.subject = "Testing Email"
        self.body = "just body of testing Email"
        self.to_email = ["mdabdullahalalaminp@gmail.com"]
        self.from_email = PRIMARY_ADMIN_EMAIL

    def test_send_mail_async(self):
        response = send_mail_async.delay(
            self.subject, self.body, self.to_email)
        self.assertTrue(response)


class SendRemainderEmailTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user("alamin", "a@gmail.com")
        self.user2 = User.objects.create_user(
            "alamin2", "mdabdullahalalaminp@gmail.com")
        self.event = Event(title="test_event")
        self.event.presenter = self.user
        self.event.content_type = 'skype_session'
        self.event.start_time = timezone.now()
        self.event.end_time = timezone.now()
        self.event.save()
        Registration.objects.create(event=self.event,
                                    attendee=self.user2, skype_id="skype_id")

    def test_send_remainder_email(self):
        response = send_remainder_email.delay(self.event.id, False)
        logging.info(response)
        self.assertTrue(response)

    def test_send_remainder_email_feedback(self):
        response = send_remainder_email.delay(self.event.id, True)
        logging.info(response)
        self.assertTrue(response)


class ScheduleBackgrounEmailTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user("alamin", "a@gmail.com")
        self.user2 = User.objects.create_user(
            "alamin2", "mdabdullahalalaminp@gmail.com")
        self.event = Event(title="test_event")
        self.event.presenter = self.user
        self.event.content_type = 'skype_session'
        self.event.start_time = timezone.now()
        self.event.end_time = timezone.now()
        self.event.save()
        Registration.objects.create(event=self.event,
                                    attendee=self.user2, skype_id="skype_id")

    def test_schedule_background_email(self):
        response = schedule_background_email(self.event)
        logging.info(response)
        self.assertTrue(response)


class SkypeEventGroupEmailTest(TestCase):

    # In TDD book for every method there were a test class
    # Each TestClass created his own objects
    # So remainder email and skypegroupemail setup method same
    def setUp(self):
        self.user = User.objects.create_user("alamin", "a@gmail.com")
        self.user2 = User.objects.create_user("alamin2",
                                              "mdabdullahalalaminp@gmail.com")
        self.event = Event(title="test_event")
        self.event.presenter = self.user
        self.event.content_type = 'skype_session'
        self.event.start_time = timezone.now()
        self.event.end_time = timezone.now()
        self.event.save()

        Registration.objects.create(event=self.event,
                                    attendee=self.user2, skype_id="skype_id")
        self.event_email = EventEmail.objects.create(
            event=self.event, email_subject="Hi", email_body="body")

    def test_skype_event_group_email(self):
        logger.info("testing the skype group email")
        response = skype_event_group_email.delay(self.event_email.id)
        self.assertTrue(response)
