from django.conf.urls import url

from .views import under_construction_page

urlpatterns = [
    url(r'^under_construction_page/$', under_construction_page, name='under_construction_page'),
]
