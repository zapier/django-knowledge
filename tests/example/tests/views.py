from example.tests.base import TestCase

from django.test.client import Client
from django.contrib.auth.models import User, AnonymousUser

from django.core.urlresolvers import reverse

from knowledge.models import Question, Response


class BasicViewTest(TestCase):
    def test_index(self):
        c = Client()

        r = c.get(reverse('knowledge_index'))
        self.assertEquals(r.status_code, 200)

    def test_list(self):
        c = Client()

        r = c.get(reverse('knowledge_list'))
        self.assertEquals(r.status_code, 200)

    def test_thread(self):
        c = Client()

        r = c.get(reverse('knowledge_thread', args=[123456, 'a-big-long-slug']))
        self.assertEquals(r.status_code, 404)

        r = c.get(reverse('knowledge_thread', args=[self.question.id, 'a-big-long-slug']))
        self.assertEquals(r.status_code, 404)

    def test_ask(self):
        c = Client()

        r = c.get(reverse('knowledge_ask'))
        self.assertEquals(r.status_code, 200)