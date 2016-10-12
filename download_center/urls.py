from django.conf.urls import url
from .views import download_center

urlpatterns = [
    url(r'^$', download_center, name='download_center'),
    url(r'^type/(?P<type_id>\d+)/$', download_center, name='download_search_type'),
    url(r'^type/(?P<department_id>\d+)/$', download_center, name='download_search_department')
]
