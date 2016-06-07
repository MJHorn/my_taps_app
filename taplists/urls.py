from django.conf.urls import url
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.tap_list, name='tap_list'),
    url(r'^(?i)VIC/$', views.tap_list, name='VIC'),
    url(r'^tapstyle/$', views.tap_style, name='tap_style'),
    url(r'^cookie/$', views.cookie, name='cookie'),
    url(r'^(?i)NSW/$', views.tap_NSW, name='NSW'),
    url(r'^(?i)QLD/$', views.tap_QLD, name='QLD'),
    url(r'^fakehome/$', views.home, name='fakehome'),
]

