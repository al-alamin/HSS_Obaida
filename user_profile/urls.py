from django.conf.urls import url
from .views import user_profile

urlpatterns = [
    url(r'^(?P<user_id>\d+)/$', user_profile, name='user_profile')
]
