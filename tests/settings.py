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

STATIC_URL = '/static/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.markup',

    'knowledge',
    'south',
    'django_coverage',
    'mock',
)

ROOT_URLCONF = 'tests.urls'

KNOWLEDGE_ALLOW_ANONYMOUS = True

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(DIRNAME, 'reports').replace('\\','/')

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates').replace('\\','/')
)