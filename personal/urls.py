from django.urls import re_path
from .views import index, about, contact
#url for app
urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^about', about, name='about'),
    re_path(r'^contact', contact, name='contact'),
]
