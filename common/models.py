from django.contrib.auth.models import User
from django.db import models


class UserMeta(models.Model):
    user = models.OneToOneField(User, related_name='meta')
    url = models.URLField(blank=True, null=True)
    short_bio = models.TextField(max_length=200, blank=True, null=True)
    long_bio = models.TextField(max_length=5000, blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    gplus_link = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/', default='images/user_default.jpg')

    def __str__(self):
        return self.user.get_full_name()


class Type(models.Model):
    """
    It's like parent category for category and tag. eg, Visa, Higher Study
    """
    name = models.CharField(max_length=50, help_text='parent category for category and tag. eg, Visa, Higher Study')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, blank=True, null=True)

    def __str__(self):
        return self.name
