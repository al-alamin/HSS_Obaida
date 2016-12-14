from django.conf.urls import url
from practice_test.views import GreView
from django.views.generic import TemplateView
from django.views import View

urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name="practice_test/practice_test.html"),
        name='practice_test'),
    url(r'^gre/$', GreView.as_view(), name='gre'),
]
