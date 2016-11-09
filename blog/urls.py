from django.conf.urls import url
from .views import blog, blog_single

urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^video_blog/$', blog, kwargs={'video': True}, name='video_blog'),
    url(r'^author/(?P<author_id>\d+)/$', blog, name='blog_search_author'),
    url(r'^category/(?P<cat_id>\d+)/$', blog, name='blog_search_cat'),
    url(r'^tag/(?P<tag_id>\d+)/$', blog, name='blog_search_tag'),
    url(r'^single/(?P<post_id>\d+)/$', blog_single, name='blog_single'),

]
