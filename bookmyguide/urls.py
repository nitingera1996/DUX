from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from bookmyguide.views import *

urlpatterns = [

	url(r'^$', IndexView, name= 'index'),

	url(r'^login/$', LoginView, name= 'login'),

	url(r'^register/$', RegisterView, name='register'),

	]
