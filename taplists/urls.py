from django.conf.urls import url
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.tap_list, name='tap_list'),
    url(r'^tapstyle/$', views.tap_style, name='tap_style'),
    url(r'^cookie/$', views.cookie, name='cookie'),
]


