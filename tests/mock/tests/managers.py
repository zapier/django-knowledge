from django.contrib.auth.models import User, AnonymousUser

from mock.tests.base import TestCase
from knowledge.models import Question, Response

Q = Question.objects
R = Response.objects


class BasicMangerTest(TestCase):
    def test_question_qs(self):
        # the auto generated question tests are private by default
        self.assertEquals(0, Q.can_view(self.anon).count())
        self.assertEquals(0, Q.can_view(self.bob).count())

        self.assertEquals(1, Q.can_view(self.joe).count())
        self.assertEquals(1, Q.can_view(self.admin).count())


        ## someone comes along and publicizes this question ##
        self.question.public()

        # everyone can see
        self.assertEquals(1, Q.can_view(self.anon).count())
        self.assertEquals(1, Q.can_view(self.bob).count())
        self.assertEquals(1, Q.can_view(self.joe).count())
        self.assertEquals(1, Q.can_view(self.admin).count())


        ## someone comes along and internalizes this question ##
        self.question.internal()

        # only admin can see
        self.assertEquals(0, Q.can_view(self.anon).count())
        self.assertEquals(0, Q.can_view(self.bob).count())
        self.assertEquals(0, Q.can_view(self.joe).count())

        self.assertEquals(1, Q.can_view(self.admin).count())


        ## someone comes along and privatizes this question ##
        self.question.private()

        self.assertEquals(0, Q.can_view(self.anon).count())
        self.assertEquals(0, Q.can_view(self.bob).count())

        self.assertEquals(1, Q.can_view(self.joe).count())
        self.assertEquals(1, Q.can_view(self.admin).count())

    def test_generic_response_qs(self):
        # the auto generated response tests are inherit 
        # (private by question's status) by default
        self.assertEquals(0, R.can_view(self.anon).count())
        self.assertEquals(0, R.can_view(self.bob).count())

        self.assertEquals(1, R.can_view(self.joe).count())
        self.assertEquals(1, R.can_view(self.admin).count())


        ## someone comes along and publicizes this response ##
        self.response.public()

        # everyone can see
        self.assertEquals(1, R.can_view(self.anon).count())
        self.assertEquals(1, R.can_view(self.bob).count())
        self.assertEquals(1, R.can_view(self.joe).count())
        self.assertEquals(1, R.can_view(self.admin).count())


        ## someone comes along and internalizes this response ##
        self.response.internal()

        # only admin can see
        self.assertEquals(0, R.can_view(self.anon).count())
        self.assertEquals(0, R.can_view(self.bob).count())
        self.assertEquals(0, R.can_view(self.joe).count())

        self.assertEquals(1, R.can_view(self.admin).count())


        ## someone comes along and privatizes this response ##
        self.response.private()
        
        self.assertEquals(0, R.can_view(self.anon).count())
        self.assertEquals(0, R.can_view(self.bob).count())

        self.assertEquals(1, R.can_view(self.joe).count())
        self.assertEquals(1, R.can_view(self.admin).count())