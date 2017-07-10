"""api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^drinks$', views.drink_list, name='drink-list'),
    url(r'^drinks/(?P<pk>[0-9]+)/$', views.drink_detail, name='drink-details'),
    url(r'^queues$', views.queue_list, name='queue-list'),
    url(r'^queues/(?P<pk>[0-9]+)/$', views.queue_detail, name='queue-details'),
    url(r'^cocktails$', views.cocktail_list, name='cocktail-list'),
    url(r'^cocktails/(?P<pk>[0-9]+)/$', views.cocktail_detail, name='cocktail-details'),
    url(r'^users$', views.user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail, name='user-details'),
    url(r'^commander/(?P<pk>[0-9]+)$', views.commander, name='user-commande'),
    url(r'^deleteq$', views.deleteAllQueue, name='delete-queue'),
    url(r'validecommande/(?P<uuid>[^/]+)/$', views.commandeserve, name='update-queue-t'),
    url(r'getqueu$', views.getqueueforuser, name='queue-for-user'),
    url(r'addcoin$', views.addcoin, name='add-coin'),
    url(r'createuser$', views.create_user, name='create-user'),
]