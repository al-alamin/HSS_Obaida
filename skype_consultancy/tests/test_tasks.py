from django.test import TestCase
from django.conf import settings
import logging

from skype_consultancy.tasks import send_mail_async
# logger = logging.getLogger(__name__)
PRIMARY_ADMIN_EMAIL = settings.PRIMARY_ADMIN_EMAIL

subject = "Testing Email"
body = "just body of testing Email"
to_email = ["mdabdullahalalaminp@gmail.com"]
from_email = PRIMARY_ADMIN_EMAIL


class Test_send_mail_async(TestCase):

    # def setUp(self):
    #     self.subject = "Testing Email"
    #     self.body = "just body of testing Email"
    #     self.to_email = ["mdabdullahalalaminp@gmail.com"]
    #     self.from_email = PRIMARY_ADMIN_EMAIL
    def test_send_mail_async(self):
        response = send_mail_async.delay(subject, body, to_email)
        logging.info(response)
        self.assertTrue(response)
