from django.test import TestCase


class TestRelatedModels(TestCase):

    def test_sop_view_renders_sop_template(self):
        response = self.client.get('/sop/')
        self.assertTemplateUsed(response, 'sop/sop_review.html')

    
