from django.contrib.auth.models import User
from django.db import models

# from django.core.exceptions import ValidationError


class ReviewSubmission(models.Model):

    user = models.ForeignKey(User)
    review_type = models.CharField(max_length=20)
