from django.test import TestCase
from unittest.mock import MagicMock

from django.core.files import File
from sop.forms import SOPSubmitForm
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


class TestRelatedModels(TestCase):

    def test_sop_view_renders_sop_template(self):
        response = self.client.get(reverse("sop_review"))
        self.assertTemplateUsed(response, 'sop/sop_review.html')

    # This test will send a sop file and test if everything is okay
    def test_sop_submit(self):

        file = MagicMock(spec=File, name="file")
        file.name = "sopfile.docx"
        file.size = 10
        file.content_type = "application/msword"
        form_data = {'name': "alamin", 'email': 'abc@gmail.com',
                     'msg': 'hi', 'file': file}

        response = self.client.post("/sop/", form_data, format='multipart')
        self.assertEqual(response.status_code, 200)

