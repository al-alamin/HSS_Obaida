from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class UserMeta(models.Model):
    user = models.OneToOneField(User)
    url = models.URLField(blank=True, null=True)
    short_bio = RichTextField(max_length=400)
    long_bio = RichTextField(max_length=5000, blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    gplus_link = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/', default='images/user_default.jpg')

    def __str__(self):
        return self.user.get_full_name()
