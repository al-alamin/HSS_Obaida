"""HSS_Obaida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from contact_us.views import contactus
from faq.views import faq,search_result
from home.views import home, google_custom_search, decision_making, preparation, standard_exam
from skype_consultancy.views import skype, delete_skype_registration
from sop.views import sop
from to_do.views import to_do

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),  # for python social auth
    url('', include('django.contrib.auth.urls', namespace='auth')),  # for django default authentication system
    url(r'^$', home, name='home'),
    url(r'^decision_making/$', decision_making, name='decision_making'),
    url(r'^preparation/$', preparation, name='preparation'),
    url(r'^standard_exam/$', standard_exam, name='standard_exam'),
    url(r'^faq/$', faq, name='faq'),
    url(r'^faq/search/$', search_result, name='faq_search'),
    url(r'^faq/category/(?P<cat_id>\d+)/$', search_result, name='faq_search_cat'),
    url(r'^faq/tag/(?P<tag_id>\d+)/$', search_result, name='faq_search_tag'),
    url(r'^sop/$', sop, name='sop_review'),
    url(r'^to_do/$',to_do, name='to_do'),
    url(r'^skype/$',skype, name='skype'),
    url(r'^skype/withdraw$',delete_skype_registration, name='reg_withdraw'),
    url(r'^contactus/$',contactus, name='contactus'),
    url(r'^about_us/', include('about_us.urls')),
    url(r'^google_search/$', google_custom_search, name='google_search'),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
