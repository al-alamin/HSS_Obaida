from django.contrib.auth.models import User
from django.db import models


class ReviewSubmission(models.Model):

    user = models.ForeignKey(User)
    # review type is uploading doc for what type of document review like sop, resume, mail_to_professor, others
    # check sop.forms.SOPSubmitForm review type

    review_type = models.CharField(max_length=20)

    def __str__(self):

        return self.user.username
