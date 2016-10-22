from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils import timezone
from django.core.exceptions import ValidationError


class Event(models.Model):
    event_type_choices = (
        ('skype_session', 'skype_session'),
        ('others', 'others')
    )
    title = models.CharField(max_length=500)
    presenter = models.ForeignKey(
        User, help_text="Presenter should have 'usermeta' data.")
    event_type = models.CharField(choices=event_type_choices, max_length=30,
                                  help_text='For skype session select "skype_session".')
    location = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    registration_limit = models.PositiveSmallIntegerField(null=True,
                                                          blank=True, default=10)
    fee = models.DecimalField(
        max_digits=255, decimal_places=2, default=0, null=True, blank=True)

    def __str__(self):
        return self.title

    """
        This clean method will be called when data is submitted from django admin
        form or any other form.
        This clean method will not be called on model's save method. 
    """

    def clean(self):

        if self.end_time < timezone.now():
            raise ValidationError('The Session has already ended')

        if self.start_time > self.end_time:
            raise ValidationError('Start date is after end date')

    @property
    def available_seats(self):
        return self.registration_limit - self.registration_set.count()

    @property
    def is_registration_open(self):
        return self.available_seats > 0 and self.start_time > now()

    @property
    def duration(self):
        time_diff = self.end_time - self.start_time
        return time_diff.total_seconds() / 60  # difference in minute

    @property
    def name_task(self):
        # for unique parent task name to manage email scheduling
        return '-'.join((type(self).__name__, str(self.id)))

    class Meta:
        ordering = ('start_time',)
        get_latest_by = 'start_time'


class Registration(models.Model):
    event = models.ForeignKey(Event)
    attendee = models.ForeignKey(User)
    skype_id = models.CharField(
        max_length=255, help_text="required for 'skype session'.")
    created = models.DateTimeField(
        auto_now_add=True, editable=False, null=True, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.attendee.username

    class Meta:
        unique_together = ["event", "attendee"]
        ordering = ('created',)


class EventEmail(models.Model):

    """
    required for sending email to all registered users from admin panel
    """
    event = models.ForeignKey(Event)
    email_subject = models.CharField(max_length=100)
    email_body = RichTextField(max_length=500)

    def __str__(self):
        return self.event.title
