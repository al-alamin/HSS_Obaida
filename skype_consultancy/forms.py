import logging

from django import forms
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from celery_app.background_email_constants import BD_TZ, time_format, body_event_registration
from celery_app.tasks import send_mail_async
from event.models import Registration

logger = logging.getLogger(__name__)

ADMIN_EMAILS = settings.ADMIN_EMAILS


class EventRegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ['skype_id', ]

    # must be called after cleaning data
    def save_and_mail(self, event, user):
        """
        Will save the registration and send mail to user and admin
        :param event: event object
        :param user: django default user model
        :return: boolean depending on registration success
        """
        skype_id = self.cleaned_data['skype_id']
        try:
            Registration.objects.create(
                attendee=user, event=event, skype_id=skype_id)
        except:
            reg_success = False
            logger.exception(
                'Registration failed for the user {0} for the event {1}'.format(user, event))
        else:
            reg_success = True
            logger.info(
                '{0} user successfully registered for the event {1}'.format(user, event))
        if reg_success:
            to_email = [user.email, settings.SECONDARY_ADMIN_EMAIL]
            event_start_time = event.start_time.astimezone(
                BD_TZ).strftime(time_format)
            subject = "Your event registration is confirmed for the event {0}".format(
                event.title)
            # if calendar invitation link is null then making it a empty string
            if(event.calendar_invitation_link):
                calendar_invitation_link = "Add to your Google Calendar: " +\
                    event.calendar_invitation_link
            else:
                calendar_invitation_link = ""
            body_email = body_event_registration.format(
                user.first_name, event.title, event_start_time, event.duration,
                calendar_invitation_link)
            # celery will send the mail asynchronously
            send_mail_async(subject, body_email, to_email)
 
        return reg_success


class EventRegistrationDeleteForm(forms.Form):
    delete = forms.BooleanField(
        required=False, label='Withdraw My Registration')
    reg_id = forms.IntegerField(widget=forms.HiddenInput())

    def del_registraion(self, user):
        delete = self.cleaned_data['delete']
        id = self.cleaned_data['reg_id']
        del_success = False
        if delete:
            try:
                reg = Registration.objects.get(id=id, attendee=user)
            except ObjectDoesNotExist:
                msg = 'Registration deletion failed for event id {0} and for user {1}'.format(
                    id, user)
                logger.exception(msg)
            else:
                reg.delete()
                del_success = True
                msg = '{0}user registration deleted from the event id {1}'.format(
                    user, id)
                logger.info(msg)

        return del_success
