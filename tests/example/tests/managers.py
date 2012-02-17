from django.contrib.auth.models import User, AnonymousUser

from example.tests.base import TestCase
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
