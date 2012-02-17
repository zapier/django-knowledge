import settings

from django.db import models

from knowledge.managers import QuestionManager, ResponseManager


STATUSES = (
    ('public', 'Public'),
    ('private', 'Private'),
    ('internal', 'Internal'),
)


STATUSES_EXTENDED = STATUSES + (
    ('inherit', 'Inherit'),
)


class KnowledgeBase(models.Model):
    """
    The base class for Knowledge models.
    """
    is_question = False
    is_response = False

    added = models.DateTimeField(auto_now_add=True)
    lastchanged = models.DateTimeField(auto_now=True)

    user = models.ForeignKey('auth.User', db_index=True)
    body = models.TextField(blank=True, null=True)

    points = models.PositiveIntegerField(default=0)

    ########################
    #### STATUS METHODS ####
    ########################

    def can_view(self, user):
        """
        Returns a boolean dictating if a User like instance can
        view the current Model instance.
        """

        if self.status == 'inherit' and self.is_response:
            return self.question.can_view(user)

        if self.status == 'internal' and user.is_staff:
            return True

        if self.status == 'private':
            if self.user == user or user.is_staff:
                return True
            if self.is_response and self.question.user == user:
                return True

        if self.status == 'public':
            return True

        return False

    def switch(self, status, save=True):
        self.status = status
        if save:
            self.save()

    def public(self):
        self.switch('public')

    def private(self):
        self.switch('private')

    def inherit(self):
        self.switch('inherit')

    def internal(self):
        self.switch('internal')

    class Meta:
        abstract = True


class Question(KnowledgeBase):
    is_question = True

    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=32, choices=STATUSES,
        default='private', db_index=True)

    objects = QuestionManager()

    def inherit(self):
        pass

    ###################
    #### RESPONSES ####
    ###################

    def get_responses(self, user=None):
        responses = self.responses.all()
        #if user:
        #    return [r for r in responses if r.can_view(user)]
        return responses

    def answered(self):
        """
        Returns a boolean indictating whether there any questions.
        """
        return bool(self.get_responses())

    def accepted(self):
        """
        Returns a boolean indictating whether there is a accepted answer
        or not.
        """
        for response in self.get_responses():
            if response.accepted:
                return True
        return False

    def accept(self, response=None):
        """
        Given a response, make that the one and only accepted answer.
        Similar to StackOverflow.
        """
        if response and response.question == self:
            self.get_responses().update(accepted=False)
            response.accepted = True
            response.save()
            return True
        else:
            return False


class Response(KnowledgeBase):
    is_response = True

    question = models.ForeignKey('knowledge.Question',
        related_name='responses')
    status = models.CharField(
        max_length=32, choices=STATUSES_EXTENDED,
        default='inherit', db_index=True)
    accepted = models.BooleanField(default=False)

    objects = ResponseManager()
