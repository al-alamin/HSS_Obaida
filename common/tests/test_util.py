from django.test import TestCase
from django.conf import settings
import logging

from common.utils import send_mail

logger = logging.getLogger(__name__)
PRIMARY_ADMIN_EMAIL = settings.PRIMARY_ADMIN_EMAIL


class TestSendMail(TestCase):

    def setUp(self):
        self.subject = "Testing Email"
        self.body = "just body of testing Email"
        self.to_email = ["mdabdullahalalaminp@gmail.com"]
        self.from_email = PRIMARY_ADMIN_EMAIL

    def test_send_mail(self):
        response = send_mail(
            self.subject, self.body, self.to_email, self.from_email)
        logger.info("Mail has been send from test")
        self.assertTrue(response)
