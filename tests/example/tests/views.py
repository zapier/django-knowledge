from django.test import TestCase

from django.test.client import Client
from django.contrib.auth.models import User, AnonymousUser

from django.core.urlresolvers import reverse

from desk.models import Question, Response


class BasicViewTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser('admin', 'admin@example.com', 'secret')
        self.joe = User.objects.create_user('joe', 'joe@example.com', 'secret')
        self.bob = User.objects.create_user('bob', 'bob@example.com', 'secret')
        self.anon = AnonymousUser()

        ## joe asks a question ##
        self.question = Question.objects.create(
            user = self.joe,
            title = 'What time is it?',
            body = 'Whenever I look at my watch I see the little hand at 3 and the big hand at 7.'
        )

        ## admin responds ##
        self.response = Response.objects.create(
            question = self.question,
            user = self.admin,
            body = 'The little hand at 3 means 3 pm or am, the big hand at 7 means 3:35 am or pm.'
        )


    def test_index(self):
        c = Client()

        r = c.get(reverse('desk_index'))
        self.assertEquals(r.status_code, 200)

    def test_list(self):
        c = Client()

        r = c.get(reverse('desk_list'))
        self.assertEquals(r.status_code, 200)

    def test_thread(self):
        c = Client()

        r = c.get(reverse('desk_thread', args=[123456, 'a-big-long-slug']))
        self.assertEquals(r.status_code, 404)

        r = c.get(reverse('desk_thread', args=[self.question.id, 'a-big-long-slug']))
        self.assertEquals(r.status_code, 404)

    def test_ask(self):
        c = Client()

        r = c.get(reverse('desk_ask'))
        self.assertEquals(r.status_code, 200)