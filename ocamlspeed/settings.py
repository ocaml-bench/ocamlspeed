# -*- coding: utf-8 -*-
# Django settings for a Codespeed project.
import os

DEBUG = True

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOPDIR = os.path.split(BASEDIR)[1]

#: The directory which should contain checked out source repositories:
REPOSITORY_BASE_PATH = os.path.join(BASEDIR, "repos")

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['DB_FILE'],
    }
}

TIME_ZONE = 'Etc/UTC'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

MEDIA_ROOT = os.path.join(BASEDIR, "media")

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

SECRET_KEY = os.environ['SECRET_KEY']

SILENCED_SYSTEM_CHECKS = [
    'admin.E408',
    'admin.E409',
    'admin.E410',
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = '{0}.urls'.format(TOPDIR)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASEDIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'codespeed',
)


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASEDIR, "sitestatic")
STATICFILES_DIRS = (
    os.path.join(BASEDIR, 'static'),
)


# Codespeed settings that can be overwritten here.
from codespeed.settings import *

WEBSITE_NAME = "ocamlspeed"
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'bench.ocamllabs.io']
USE_TZ = True

GIT_USE_COMMIT_DATE = True
GIT_USE_FIRST_PARENT = True

# default environment for Changes and Timeline views
DEF_ENVIRONMENT = 'bench.ocamllabs.io'

# Which executable + revision should be default as a baseline
# Given as the name of the executable and commitid of the revision
# Example: defaultbaseline = {'executable': 'myexe', 'revision': '21'}
DEF_BASELINE = {'executable':'vanilla', 'tag':'4.07.1'}

# used to highlight cells on the changes tab
CHANGE_THRESHOLD = 20.0
TREND_THRESHOLD = 20.0

# make comparison page default to all executables not selected
COMP_EXECUTABLES = [('','')] # NB: need empty tuple to make list evaluate

# make comparison page default to normalization
NORMALIZATION = True




