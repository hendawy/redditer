"""redditter URL Configuration

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

from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<resource>(top|hot|favorites)?)$', views.home, name='home'),
    url(
        r'^favorite/(?P<listing_name>t[1-8]{1}_[a-z0-9]+)$',
        views.favorite, name='favorite'),
    url(
        r'^unfavorite/(?P<listing_name>t[1-8]{1}_[a-z0-9]+)$',
        views.unfavorite, name='unfavorite'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]
