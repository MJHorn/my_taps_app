from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tap_list, name='tap_list'),
]


