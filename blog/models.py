from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class BlogTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    post_type_choices = (
        ('blog', 'blog'),
        ('news', 'news'),
        ('other', 'other')
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    post_type = models.CharField(choices=post_type_choices, max_length=30)
    category = models.ManyToManyField(BlogCategory)
    tag = models.ManyToManyField(BlogTag)
    text = RichTextField(max_length=50000, config_name='basic')
    video_url = models.URLField(blank=True, null=True)
    featured_img = models.ImageField(upload_to='images/blog/', default='images/blog/my-study-notebook-blog-featured.png',
                                     help_text='This image will be used in single blog page')
    thumbnail = models.ImageField(upload_to='images/blog/', default='images/blog/my-study-notebook-blog-thumbnail.png',
                                  help_text='This image will be used in blog page or as a thumbnail in sidebar')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

