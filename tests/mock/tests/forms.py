from django.contrib.auth.models import User, AnonymousUser
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from mock.tests.base import TestCase
from knowledge.models import Question, Response


class BasicFormTest(TestCase):
    pass