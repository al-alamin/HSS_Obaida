from unittest.mock import MagicMock, patch, Mock

from django.test import TestCase
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from sop.forms import SOPSubmitForm


class MyFormTest(TestCase):

    def test_sop_submit_form(self):

        file = MagicMock(spec=File, name="file")
        file.name = "sopfile.docx"
        file.size = 10
        file.content_type = "application/msword"
        form = SOPSubmitForm(
            data={
                'name': "alamin",
                'email': "abc@gamil.com",
                'msg': "hi",
            },
            files={'file': file}
        )

        # print(form)
        # print(form.errors)
        self.assertTrue(form.is_valid())
