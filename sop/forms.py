from django import forms

from common.utils import send_mail

SUPPORTED_SOP_FILE_TYPES = ['application/msword',
                            'application/vnd.openxmlformats-officedocument.wordprocessingml.document']


class SOPSubmitForm(forms.Form):
    # attrs = {"class": "form-control", 'required': 'required'}
    attrs = {'required': 'false', "class": "form-control"}
    name = forms.CharField(
        max_length=50, label='Name', widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(
        max_length=30, label='Email', widget=forms.TextInput(attrs=attrs))
    msg = forms.CharField(
        max_length=500, label='Message', widget=forms.Textarea(attrs=attrs))
    # file_attrs = {'required': 'required',
    #               'onchange': "this.parentNode.nextSibling.value = this.value",
    #               }
    file_attrs = {
              'required': 'false',
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
                                    required=False,
                                    label='Select Your Review Type')

    def clean(self):
        super(SOPSubmitForm, self).clean()
        sop_file = self.cleaned_data['file']
        if sop_file.size > 5 * 1024 * 1024:
            raise forms.ValidationError("File size exceeded 5MB limit")
        if sop_file.content_type not in SUPPORTED_SOP_FILE_TYPES:
            raise forms.ValidationError(
                "Unsupported file type. Please upload either .doc or .docx file")
        # print("choice {0}".format(review_type))
        review_type = self.cleaned_data['review_type']
        print(review_type)

    def email_SOP(self, file):
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['email']
        msg = self.cleaned_data['msg']
        subject = "{0} submitted a SOP for review".format(name)
        # email_success = send_mail(
        #     subject, msg, from_email=from_email, attachment=file)
        email_success = True
        print('form is submitted corrected')
        return email_success
