from django.conf.urls import url
from .views import download

urlpatterns = [
    url(r'^$', download, name='download'),
    url(r'^type/(?P<department_id>\d+)/$', download, name='download_search_department')
]
