from ckeditor.fields import RichTextField
from django.db import models

from common.models import Category, Tag


class Question(models.Model):
    text = models.TextField(max_length=500)
    ans = RichTextField(max_length=1500, blank=True)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    is_popular = models.BooleanField(default=False)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.text
