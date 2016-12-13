from django.conf.urls import url
from .views import practice_test

urlpatterns = [
    url(r'^$', practice_test, name='practice_test'),
]
