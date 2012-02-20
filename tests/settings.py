import os

DIRNAME = os.path.dirname(__file__)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(DIRNAME, 'example.sqlite').replace('\\','/'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.markup',

    'knowledge',
    'django_coverage',
    'mock',
)

ROOT_URLCONF = 'tests.urls'

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates').replace('\\','/')
)