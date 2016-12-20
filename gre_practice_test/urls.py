from django.conf.urls import url
from gre_practice_test.views import IndexView, GreSubjectTestRulesView, GreSubjectTestExamView
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', IndexView.as_view(),
        name='index'),
    # url(r'^gre/$', GreView.as_view(), name='gre'),
    url(r'^quantitative-test/(?P<id>[0-9]+)/rules$',
        GreSubjectTestRulesView.as_view(), name='rules'),
    url(r'^quantitative-test/(?P<id>[0-9]+)/exam/$',
        GreSubjectTestExamView.as_view(), name='quantitative_test_exam'),
]
