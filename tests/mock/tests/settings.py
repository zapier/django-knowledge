from knowledge import settings

from mock.tests.base import TestCase
from django.contrib.auth.models import User

from knowledge.models import Question, Response


class BasicSettingsTest(TestCase):
    def test_ALLOW_ANONYMOUS(self):
        self.assertFalse(settings.ALLOW_ANONYMOUS)

        # run test for False

        settings.ALLOW_ANONYMOUS = not settings.ALLOW_ANONYMOUS

        # run test for True

        settings.ALLOW_ANONYMOUS = not settings.ALLOW_ANONYMOUS

    def test_AUTO_PUBLICIZE(self):
        self.assertFalse(settings.AUTO_PUBLICIZE)

        # run test for False

        settings.AUTO_PUBLICIZE = not settings.AUTO_PUBLICIZE

        # run test for True

        settings.AUTO_PUBLICIZE = not settings.AUTO_PUBLICIZE