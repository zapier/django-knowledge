from django.test.client import RequestFactory

from mock.tests.base import TestCase

from knowledge.templatetags.knowledge_tags import get_gravatar, page_query


class BasicTemplateTagTest(TestCase):
    def test_gravatar(self):
        self.assertEquals(
            'https://secure.gravatar.com/avatar/883955996dbb79f38d8814dbfb336885.jpg?s=60&amp;r=g&amp;d=retro', 
            get_gravatar('bryan@bryanhelmig.com', 60, 'g', 'retro')
        )

    def test_page_query(self):
        request = RequestFactory().get('/faker/?something=extra&page=123')
        self.assertEquals('something=extra&amp;page=666', page_query(request, 666))

        request = RequestFactory().get('/faker/?something=extra')
        self.assertEquals('something=extra&amp;page=666', page_query(request, 666))