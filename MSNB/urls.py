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
from common.views import login
from home.views import google_custom_search

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),  # for python social auth
    url('', include('django.contrib.auth.urls', namespace='auth')),  # for django default authentication system
    url(r'^', include('home.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^sop/', include('sop.urls')),
    url(r'^common/', include('common.urls')),
    # url(r'^to_do/', include('to_do.urls')),
    url(r'^skype/', include('skype_consultancy.urls')),
    url(r'^contactus/', include('contact_us.urls')),
    url(r'^about_us/', include('about_us.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^profile/', include('user_profile.urls')),
    url(r'^download/', include('download_center.urls')),
    url(r'^gre-practice-test/', include('gre_practice_test.urls', namespace="gre_practice_test")),
    url(r'^practice-test/', include('practice_test.urls')),
    url(r'^google_search/$', google_custom_search, name='google_search'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # djangos default url for login
    url(r'^accounts/login/$', login, name='login'),
    


]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
