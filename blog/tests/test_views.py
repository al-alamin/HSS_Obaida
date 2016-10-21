import logging

from django.test import TestCase

from django.contrib.auth.models import User
from blog.models import BlogTag, BlogCategory, Post

from django.core.urlresolvers import reverse

logger = logging.getLogger(__name__)


class BlogTest(TestCase):

    def setUp(self):
        self.blog_tag = BlogTag.objects.create(name="tag11")
        self.blog_category = BlogCategory.objects.create(name="cat11")
        self.user = User.objects.create_user("alamin11", "a@gmail.com")
        self.post = Post(
            title="titlexyz", author=self.user, post_type="blog", text="text")
        self.post.save()
        self.post.tag.add(self.blog_tag)
        self.post.category.add(self.blog_category)
        self.post.save()

    def test_blog_view_renders_blog_template(self):
        response = self.client.get(reverse("blog"))
        self.assertTemplateUsed(response, 'blog/blog.html')
        logger.info(response.status_code)

    def test_blog_page_contains_blog(self):
        response = self.client.get(reverse("blog"))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)
        self.assertContains(response, self.blog_tag)
        self.assertContains(response, self.blog_category)

#     def test_faq_page_uses_question_model(self):
#         response = self.client.get('/faq/')
#         if (Question.objects.all().count() > 0):
#             self.assertIsInstance(
#                 response.context['recent_q'], models.Question)
#         # question = Question.objects.create(text="new question")


class TestBlogSingle(TestCase):

#     def setUp(self):
#         type = Type.objects.create(name="type")
#         self.tag = Tag.objects.create(name="tag", type=type)
#         self.category = Category.objects.create(name="category")
#         question = Question(text="question", ans="ans")
#         question.save()
#         question.category.add(self.category)
#         question.tag.add(self.tag)

    def test_faq_url_status_code(self):
        response = self.client.get(reverse("faq"))
        self.assertEqual(response.status_code, 200)

#     def test_faq_search_cat_url_status(self):
#         response = self.client.get(
#             reverse("faq_search_cat", args=[self.category.id]))
#         self.assertEqual(response.status_code, 200)

#     def test_faq_search_tag_url_status(self):
#         response = self.client.get(
#             reverse("faq_search_cat", args=[self.tag.id]))
#         self.assertEqual(response.status_code, 200)

#     def test_faq_search_url_status(self):
#         response = self.client.post(
#             reverse("faq_search"), {'search_item': 'a'})
#         self.assertEqual(response.status_code, 200)

#     # faq search result's views is relatively complex there are lots of conditional
#     # statement for get/post requests. This will make sure whatever the logic is
#     # at least there is FaqSearchForm in the template
#     def test_faq_page_uses_faq_search_form(self):
#         response = self.client.get('/faq/')
#         self.assertIsInstance(
#             response.context['faq_search_form'], FaqSearchForm)
