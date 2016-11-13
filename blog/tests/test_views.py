import logging

from django.test import TestCase

from django.contrib.auth.models import User
from blog.models import BlogTag, BlogCategory, Post

from django.core.urlresolvers import reverse

logger = logging.getLogger(__name__)


class BlogTest(TestCase):

    def setUp(self):
        self.post, self.blog_tag, self.blog_category = createBlog()

    def test_blog_view_renders_blog_template(self):
        response = self.client.get(reverse("blog"))
        self.assertTemplateUsed(response, 'blog/blog.html')

    # This test'll try to make sure if the template is loaded properly
    def test_blog_page_contains_blog(self):
        response = self.client.get(reverse("blog"))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)
        self.assertContains(response, self.blog_tag)
        self.assertContains(response, self.blog_category)


class BlogSingleTest(TestCase):

    def setUp(self):
        self.post, self.blog_tag, self.blog_category = createBlog()

    def test_blog_single_url_status_code(self):
        response = self.client.get(
            reverse("blog_single", kwargs={'post_id': self.post.id}))
        self.assertEqual(response.status_code, 200)

    def test_single_blog_page_contains_blog_info(self):
        response = self.client.get(reverse("blog"))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)
        self.assertContains(response, self.blog_tag)
        self.assertContains(response, self.blog_category)

# This method will create temporay blog object so that these test class use it
def createBlog():
    blog_tag = BlogTag.objects.create(name="tag11")
    blog_category = BlogCategory.objects.create(name="cat11")
    user = User.objects.create_user("alamin11", "a@gmail.com")
    post = Post(
        title="titlexyz", author=user, post_type="blog", text="text")
    post.save()
    post.tag.add(blog_tag)
    post.category.add(blog_category)
    post.save()
    return post, blog_tag, blog_category
