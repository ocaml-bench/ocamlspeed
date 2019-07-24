# -*- coding: utf-8 -*-

from django.conf import settings
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path(r'', include('codespeed.urls')),
    path(r'admin/', admin.site.urls)
]

if settings.DEBUG:
    # needed for development server
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
