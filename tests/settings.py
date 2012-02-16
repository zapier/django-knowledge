import os

DIRNAME = os.path.dirname(__file__)

DEBUG = True

DATABASE_ENGINE = 'sqlite3'

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(DIRNAME, 'coverage').replace('\\','/')

INSTALLED_APPS = (
    'desk',
    'django_coverage',
    'myapp',
)