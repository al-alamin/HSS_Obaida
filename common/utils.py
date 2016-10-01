from django.conf import settings
from django.core.mail import EmailMessage
import logging

logger = logging.getLogger(__name__)

ADMIN_EMAILS = settings.ADMIN_EMAILS
PRIMARY_ADMIN_EMAIL = settings.PRIMARY_ADMIN_EMAIL


def send_mail(subject, body, to_email=ADMIN_EMAILS, from_email=PRIMARY_ADMIN_EMAIL, bcc=None, attachmets=None):
    email_success = False
    email = EmailMessage(subject, body, from_email, to_email, bcc)
    if attachmets is not None:
        email.attach(attachmets.name, attachmets.read(), attachmets.content_type)
    try:
        email.send()
    except Exception as e:
        msg = 'mail failed to {0}'.format(to_email)
        logger.exception(msg)
    else:
        email_success = True
        logger.info('mail sent to {0}'.format(to_email))
        
    print("\n\n ***** email has been send successfully to ")
    print(to_email)
    return email_success
