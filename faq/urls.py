from django.conf.urls import url
from .views import search_result, faq

urlpatterns = [
    url(r'^$', faq, name='faq'),
    url(r'^search/$', search_result, name='faq_search'),
    url(r'^category/(?P<cat_id>\d+)/$', search_result, name='faq_search_cat'),
    url(r'^single/(?P<question_id>\d+)/$', search_result, name='faq_search_single'),
    url(r'^tag/(?P<tag_id>\d+)/$', search_result, name='faq_search_tag'),
]
