from django.conf.urls import url
from .views import home, decision_making, preparation, standard_exam, application

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^decision_making/$', decision_making, name='decision_making'),
    url(r'^preparation/$', preparation, name='preparation'),
    url(r'^standard_exam/$', standard_exam, name='standard_exam'),
    url(r'^application/$', application, name='application'),
]
