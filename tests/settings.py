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
    'desk',
    'django_coverage',
    'example',
)

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(DIRNAME, 'coverage').replace('\\','/')
