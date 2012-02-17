from django.contrib.auth.models import User, AnonymousUser

from example.tests.base import TestCase
from knowledge.models import Question, Response


class BasicMangerTest(TestCase):
    def test_test(self):
        self.assertTrue(True)