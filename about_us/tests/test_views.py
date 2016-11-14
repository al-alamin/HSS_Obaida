from django.test import TestCase

from django.core.urlresolvers import reverse


class AboutUsTest(TestCase):

    def test_about_us_view_renders_about_us_template(self):
        response = self.client.get(reverse("about_us"))
        self.assertTemplateUsed(response, 'about_us/about_us.html')

    def test_about_us_view_status_code(self):
        response = self.client.get(reverse("about_us"))
        self.assertEqual(response.status_code, 200)

