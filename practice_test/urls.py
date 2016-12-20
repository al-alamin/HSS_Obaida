from django.conf.urls import url
# from practice_test.views import GreView, GreSubjectTestRulesView, GreSubjectTestExamView
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name="practice_test/practice_test.html"),
        name='practice_test'),
    # url(r'^gre/$', GreView.as_view(), name='gre'),
    # url(r'^gre/subject_test/(?P<id>[0-9]+)/rules$',
    #     GreSubjectTestRulesView.as_view(), name='gre_subject_test_rules'),
    # url(r'^gre/subject_test/(?P<id>[0-9]+)/exam/$',
    #     GreSubjectTestExamView.as_view(), name='gre_subject_test_exam'),
]
