from django.conf.urls import url
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?i)VIC/$', views.tap_list, name='VIC'),
    url(r'^cookie/$', views.cookie, name='cookie'),
    url(r'^(?i)NSW/$', views.tap_NSW, name='NSW'),
    url(r'^(?i)QLD/$', views.tap_QLD, name='QLD'),
    url(r'^(?i)ACT/$', views.tap_ACT, name='ACT'),
    url(r'^(?i)WA/$', views.tap_WA, name='WA'),
    url(r'^(?i)SA/$', views.tap_SA, name='SA'),
    url(r'^(?i)TAS/$', views.tap_TAS, name='TAS'),
    url(r'^(?i)ALL/$', views.tap_ALL, name='ALL'),
    url(r'^fakehome/$', views.home_draft, name='fakehome'),
    url(r'^stats/$', views.stats, name='stats'),
]

