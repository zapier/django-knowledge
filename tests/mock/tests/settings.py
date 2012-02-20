from mock.tests.base import TestCase

from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from knowledge import settings
from knowledge.models import Question, Response
from knowledge.forms import QuestionForm, ResponseForm


class BasicSettingsTest(TestCase):
    def test_ALLOW_ANONYMOUS(self):
        self.assertFalse(settings.ALLOW_ANONYMOUS)

        self.assertEqual(
            None,
            QuestionForm(self.anon)
        )

        self.assertEqual(
            None,
            ResponseForm(self.anon, self.question)
        )

        ############# flip setting ##############
        settings.ALLOW_ANONYMOUS = not settings.ALLOW_ANONYMOUS
        ############# flip setting ##############

        self.assertNotEqual(
            None,
            QuestionForm(self.anon)
        )

        self.assertNotEqual(
            None,
            ResponseForm(self.anon, self.question)
        )

        # missing the name/email...
        QUESTION_POST = {
            'title': 'This is a title friend!',
            'body': 'This is the body friend!'
        }

        form = QuestionForm(self.anon, QUESTION_POST)
        self.assertFalse(form.is_valid())


        QUESTION_POST = {
            'name': 'Test Guy',
            'email': 'anonymous@example.com',
            'title': 'This is a title friend!',
            'body': 'This is the body friend!'
        }

        form = QuestionForm(self.anon, QUESTION_POST)
        self.assertTrue(form.is_valid())

        question = form.save()

        # question has no user and is public by default
        self.assertFalse(question.user)
        self.assertEquals(question.name, 'Test Guy')
        self.assertEquals(question.email, 'anonymous@example.com')
        self.assertEquals(question.status, 'public')

        ############# flip setting ##############
        settings.ALLOW_ANONYMOUS = not settings.ALLOW_ANONYMOUS
        ############# flip setting ##############


    def test_AUTO_PUBLICIZE(self):
        self.assertFalse(settings.AUTO_PUBLICIZE)

        QUESTION_POST = {
            'title': 'This is a title friend!',
            'body': 'This is the body friend!'
        }

        question = QuestionForm(self.joe, QUESTION_POST).save()
        self.assertEquals(question.status, 'private')

        ############# flip setting ##############
        settings.AUTO_PUBLICIZE = not settings.AUTO_PUBLICIZE
        ############# flip setting ##############

        question = QuestionForm(self.joe, QUESTION_POST).save()
        self.assertEquals(question.status, 'public')


        ############# flip setting ##############
        settings.AUTO_PUBLICIZE = not settings.AUTO_PUBLICIZE
        ############# flip setting ##############


    def test_FREE_RESPONSE(self):
        self.assertTrue(settings.FREE_RESPONSE)

        # joe authored the question, it is private so any user can respond...
        self.assertFalse(ResponseForm(self.anon, self.question))
        self.assertTrue(ResponseForm(self.bob, self.question))
        self.assertTrue(ResponseForm(self.joe, self.question))
        self.assertTrue(ResponseForm(self.admin, self.question))

        ############# flip setting ##############
        settings.FREE_RESPONSE = not settings.FREE_RESPONSE
        ############# flip setting ##############

        # ...now bob can't respond!
        self.assertFalse(ResponseForm(self.anon, self.question))
        self.assertFalse(ResponseForm(self.bob, self.question))
        self.assertTrue(ResponseForm(self.joe, self.question))
        self.assertTrue(ResponseForm(self.admin, self.question))

        ############# flip setting ##############
        settings.FREE_RESPONSE = not settings.FREE_RESPONSE
        ############# flip setting ##############


    def test_SLUG_URLS(self):
        self.assertTrue(settings.SLUG_URLS)

        c = Client()

        self.question.public()

        question_url = reverse('knowledge_thread', args=[self.question.id, slugify(self.question.title)])

        r = c.get(reverse('knowledge_thread', args=[self.question.id, 'a-big-long-slug']))
        self.assertEquals(r.status_code, 301)

        r = c.get(question_url)
        self.assertEquals(r.status_code, 200)

        ############# flip setting ##############
        settings.SLUG_URLS = not settings.SLUG_URLS
        ############# flip setting ##############

        r = c.get(reverse('knowledge_thread', args=[self.question.id, 'a-big-long-slug']))
        self.assertEquals(r.status_code, 301)

        r = c.get(question_url)
        self.assertEquals(r.status_code, 301)

        r = c.get(reverse('knowledge_thread_no_slug', args=[self.question.id]))
        self.assertEquals(r.status_code, 200)

        ############# flip setting ##############
        settings.SLUG_URLS = not settings.SLUG_URLS
        ############# flip setting ##############
