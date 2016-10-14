# signal handlers
# https://docs.djangoproject.com/en/1.10/ref/signals/
# register signal handlers upfront in __init__.py

import logging

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from social.apps.django_app.default.models import UserSocialAuth

from celery_app.background_email_constants import body_new_user
from celery_app.tasks import send_mail_async

logger = logging.getLogger(__name__)


@receiver(post_save, sender=UserSocialAuth)
def new_user_signal_handler(sender, **kwargs):
    """
    Will send mail to admin whenever new user is created via python social auth
    """
    # make sure new record is created
    if kwargs['created']:
        social_user = kwargs['instance']
        user = social_user.user  # instance of django default User model
        subject = "New user created in MSNB"

        # @Note last_name, first_name is not available in user model
        #  when UserSocialAuth instance is created
        mail_body = body_new_user.format(user.username, user.email, social_user.provider)
        to_email = [user.email, settings.SECONDARY_ADMIN_EMAIL]
        send_mail_async(subject=subject, body_email=mail_body, to_email=to_email)
