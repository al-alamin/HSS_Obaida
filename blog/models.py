from django.contrib.auth.models import User
from django.db import models

from common.models import Category, Tag


class Post(models.Model):
    post_type_choices = (
        ('blog', 'blog'),
        ('news', 'news')
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    post_type = models.CharField(choices=post_type_choices, max_length=30)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    text = models.TextField(max_length=5000)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
