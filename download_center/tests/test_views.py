import logging

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from download_center.models import Department, Type, Document

from django.core.urlresolvers import reverse

logger = logging.getLogger(__name__)


class DownloadTest(TestCase):

    def setUp(self):
        # Creating a user to log him hin
        user = User.objects.create_user("alamin", "a@gmail.com")
        user.set_password('a')
        user.save()
        self.client = Client()
        self.client.login(username='alamin', password='a')

        self.dept_cse = Department.objects.create(name="CSE")
        self.dept_eee = Department.objects.create(name="EEE")
        self.type = Type.objects.create(name="SOP")
        self.document = Document.objects.create(
            # degree_choices="Masters",
            type=self.type,
            department=self.dept_cse,
            download_link="www.abc.com"
        )

    def test_download_view_renders_download_template(self):
        response = self.client.get(reverse("download"))
        self.assertTemplateUsed(response, 'download_center/download.html')
        self.assertEqual(response.status_code, 200)

    def test_download_view_with_department_id(self):
        response = self.client.get(reverse(
            "download_search_department",
            kwargs={'department_id': self.dept_cse.id}))
        self.assertTemplateUsed(response, 'download_center/download.html')
        self.assertEqual(response.status_code, 200)
    
    # Testing if the template is loading the document
    def test_download_view_loads_template_with_department_id(self):
        response = self.client.get(reverse(
            "download_search_department",
            kwargs={'department_id': self.dept_cse.id}))
        self.assertContains(response, self.dept_cse)


    def test_download_view_redirects_for_ungistered_user(self):
        self.client.logout()
        response = self.client.get(reverse("download"))
        # status code 302 means redirects
        self.assertEqual(response.status_code, 302)


# class BlogSingleTest(TestCase):

#     def setUp(self):
#         self.post, self.blog_tag, self.blog_category = createBlog()

#     def test_blog_single_url_status_code(self):
#         response = self.client.get(
#             reverse("blog_single", kwargs={'post_id': self.post.id}))
#         self.assertEqual(response.status_code, 200)

#     def test_single_blog_page_contains_blog_info(self):
#         response = self.client.get(reverse("blog"))
#         self.assertContains(response, self.post.title)
#         self.assertContains(response, self.post.text)
#         self.assertContains(response, self.blog_tag)
#         self.assertContains(response, self.blog_category)

# # This method will create temporay blog object so that these test class use it
# def createBlog():
#     blog_tag = BlogTag.objects.create(name="tag11")
#     blog_category = BlogCategory.objects.create(name="cat11")
#     user = User.objects.create_user("alamin11", "a@gmail.com")
#     post = Post(
#         title="titlexyz", author=user, post_type="blog", text="text")
#     post.save()
#     post.tag.add(blog_tag)
#     post.category.add(blog_category)
#     post.save()
#     return post, blog_tag, blog_category
