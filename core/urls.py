from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='base'),
    url(r'^bookmarks', views.addbookmark, name='bookmarks'),
]