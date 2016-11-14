from django.test import TestCase

from contact_us.forms import ContactUsForm

from django.core.urlresolvers import reverse


class ContactUsTest(TestCase):

    def test_contact_us_view_renders_contact_us_template(self):
        response = self.client.get(reverse("contactus"))
        self.assertTemplateUsed(response, 'contact_us/contact_us.html')

    def test_contact_us_page_uses_contact_us_form(self):
        response = self.client.get(reverse("contactus"))
        self.assertIsInstance(
            response.context['form'], ContactUsForm)
