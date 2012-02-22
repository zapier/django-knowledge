from django.contrib.auth.models import User, AnonymousUser
from django.core import mail

from mock.tests.base import TestCase
from knowledge.models import Question, Response
from knowledge.forms import QuestionForm, ResponseForm
from knowledge import settings


class BasicSignalTest(TestCase):
    def setUp(self):
        self.assertFalse(settings.ALERTS)
        settings.ALERTS = not settings.ALERTS

        self.admin = User.objects.create_superuser('admin', 'admin@example.com', 'secret')
        self.joe = User.objects.create_user('joe', 'joedirt@example.com', 'secret')
        self.bob = User.objects.create_user('bob', 'bob@example.com', 'secret')
        self.anon = AnonymousUser()

        self.joe.first_name = 'Joe'
        self.joe.last_name = 'Dirt'
        self.joe.save()

        ## joe asks a question ##
        self.question = Question.objects.create(
            user = self.joe,
            title = 'What time is it?',
            body = 'Whenever I look at my watch I see the little hand at 3 and the big hand at 7.',
            alert = settings.ALERTS,
        )

        ## admin responds ##
        self.response = Response.objects.create(
            question = self.question,
            user = self.admin,
            body = 'The little hand at 3 means 3 pm or am, the big hand at 7 means 3:35 am or pm.',
            alert = settings.ALERTS,
        )
        mail.outbox = [] # reset


    def tearDown(self):
        self.assertTrue(settings.ALERTS)
        mail.outbox = []
        settings.ALERTS = not settings.ALERTS
        super(BasicSignalTest, self).tearDown()


    def test_sending_alerts_dedupe(self):
        """
        One question by joe, two responses by admin: bob responds.
        """
        ######## SETUP
        self.assertTrue(settings.ALERTS)

        RESPONSE_POST = {
            'body': 'This is the response body friend!',
            'status': 'inherit',
            'alert': settings.ALERTS,
        }

        # another admin response
        response = ResponseForm(self.admin, self.question, RESPONSE_POST).save()
        
        mail.outbox = [] # reset
        self.assertEqual(len(mail.outbox), 0)
        ######## TEARDOWN

        RESPONSE_POST = {
            'body': 'This is the response body friend!',
            'alert': settings.ALERTS,
        }

        # question is by joe, first response is by admin
        form = ResponseForm(self.bob, self.question, RESPONSE_POST)
        self.assertTrue(form.is_valid())
        response = form.save()

        self.assertTrue(response.alert)
        self.assertEqual(len(mail.outbox), 2) # one for joe, one for admin


    def test_sending_alerts_normal(self):
        """
        One question by joe, one response by admin: bob responds.
        """
        self.assertTrue(settings.ALERTS)
        
        self.assertEqual(len(mail.outbox), 0)

        RESPONSE_POST = {
            'body': 'This is the response body friend!',
            'alert': settings.ALERTS,
        }

        # question is by joe, first response is by admin
        form = ResponseForm(self.bob, self.question, RESPONSE_POST)
        self.assertTrue(form.is_valid())
        response = form.save()

        self.assertTrue(response.alert)
        self.assertEqual(len(mail.outbox), 2) # one for joe, one for admin


    def test_sending_alerts_remove_self(self):
        """
        One question by joe, one response by admin: joe responds.
        """
        self.assertTrue(settings.ALERTS)

        self.assertEqual(len(mail.outbox), 0)

        RESPONSE_POST = {
            'body': 'This is the response body friend!',
            'alert': settings.ALERTS,
        }

        # question is by joe, first response is by admin
        form = ResponseForm(self.joe, self.question, RESPONSE_POST)
        self.assertTrue(form.is_valid())
        response = form.save()

        self.assertTrue(response.alert)
        self.assertEqual(len(mail.outbox), 1) # one for admin (not joe!)
