from django import forms
from common.utils import send_mail
from celery_app.background_email_constants import SOP_RECEIVED
from celery_app.tasks import send_mail_async

SUPPORTED_SOP_FILE_TYPES = ['application/msword',
                            'application/vnd.openxmlformats-officedocument.wordprocessingml.document']

from sop.models import ReviewSubmission


class SOPSubmitForm(forms.Form):
    attrs = {"class": "form-control", 'required': 'required'}
    name = forms.CharField(
        max_length=50, label='Name', widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(
        max_length=30, label='Email', widget=forms.TextInput(attrs=attrs))
    msg = forms.CharField(
        max_length=500, label='Message', widget=forms.Textarea(attrs=attrs))
    file_attrs = {'required': 'required',
                  'onchange': "this.parentNode.nextSibling.value = this.value",
                  }

    file = forms.FileField(widget=forms.FileInput(attrs=file_attrs))

    department = forms.CharField(
        max_length=50, label='Department Name', widget=forms.TextInput(attrs=attrs))

    REVIEW_CHOICES = (
        ("sop", "SOP"),
        ("resume", "Resume"),
        ("mail_to_professor", "Mail to Professor"),
        ("others", "Others")
    )
    review_type = forms.ChoiceField(choices=REVIEW_CHOICES,
                                    required='required',
                                    label='Select Your Review Type')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(SOPSubmitForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(SOPSubmitForm, self).clean()
        sop_file = self.cleaned_data['file']
        if sop_file.size > 5 * 1024 * 1024:
            raise forms.ValidationError("File size exceeded 5MB limit")
        if sop_file.content_type not in SUPPORTED_SOP_FILE_TYPES:
            raise forms.ValidationError(
                "Unsupported file type. Please upload either .doc or .docx file")
        review_type = self.cleaned_data['review_type']
        previous_submission = ReviewSubmission.objects.filter(user=self.user,
                                                              review_type=review_type)

        # This means user has already submitted a review form in this category
        if(previous_submission):
            error_msg = "You can only submit one file to review from each category.\
             You have already sumiited one file on {0} category. Please select another\
             or email us at aaa@gmail.com".format(self.cleaned_data['review_type'])

            raise forms.ValidationError(error_msg)

    def email_SOP(self, file):
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['email']
        msg = self.cleaned_data['msg']
        subject = "{0} submitted a SOP for review".format(name)

        email_success = True


        # email_success = send_mail(subject, msg, from_email=from_email, attachment=file)

        # if email_success:
        #     # confirmation mail to submitter
        #     subject = "We have received your document"
        #     send_mail_async(subject, SOP_RECEIVED.format(name), to_email=[from_email, ])

        return email_success
