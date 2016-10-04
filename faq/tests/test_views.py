from django.test import TestCase

from faq.models import Question
from common.models import Tag, Category, Type
from faq.forms import FaqSearchForm

from django.core.urlresolvers import reverse


class FaqTest(TestCase):

    def test_faq_view_renders_faq_template(self):
        response = self.client.get('/faq/')
        self.assertTemplateUsed(response, 'faq/faq.html')

    def test_faq_page_uses_faq_search_form(self):
        response = self.client.get('/faq/')
        self.assertIsInstance(
            response.context['faq_search_form'], FaqSearchForm)

    def test_faq_page_uses_question_model(self):
        response = self.client.get('/faq/')
        if (Question.objects.all().count() > 0):
            self.assertIsInstance(
                response.context['recent_q'], models.Question)
        # question = Question.objects.create(text="new question")


class TestFaqSearchResult(TestCase):

    def setUp(self):
        type = Type.objects.create(name="type")
        self.tag = Tag.objects.create(name="tag", type=type)
        self.category = Category.objects.create(name="category")
        question = Question(text="question", ans="ans")
        question.save()
        question.category.add(self.category)
        question.tag.add(self.tag)

    def test_faq_url_status_code(self):
        response = self.client.get(reverse("faq"))
        self.assertEqual(response.status_code, 200)

    def test_faq_search_cat_url_status(self):
        response = self.client.get(
            reverse("faq_search_cat", args=[self.category.id]))
        self.assertEqual(response.status_code, 200)

    def test_faq_search_tag_url_status(self):
        response = self.client.get(
            reverse("faq_search_cat", args=[self.tag.id]))
        self.assertEqual(response.status_code, 200)

    def test_faq_search_url_status(self):
        response = self.client.post(
            reverse("faq_search"), {'search_item': 'a'})
        self.assertEqual(response.status_code, 200)

    # faq search result's views is relatively complex there are lots of conditional
    # statement for get/post requests. This will make sure whatever the logic is
    # at least there is FaqSearchForm in the template
    def test_faq_page_uses_faq_search_form(self):
        response = self.client.get('/faq/')
        self.assertIsInstance(
            response.context['faq_search_form'], FaqSearchForm)
