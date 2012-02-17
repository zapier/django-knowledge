import settings

from django.db import models


STATUSES = (
    ('public', 'Public'),
    ('private', 'Private'),
    ('internal', 'Internal'),
)


STATUSES_EXTENDED = STATUSES + (
    ('inherit', 'Inherit'),
)


class DeskBase(models.Model):
    """
    The base class for Desk models.
    """
    is_question = False
    is_response = False

    added = models.DateTimeField(auto_now_add=True)
    lastchanged = models.DateTimeField(auto_now=True)

    user = models.ForeignKey('auth.User')
    body = models.TextField(blank=True, null=True)

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


class Question(DeskBase):
    is_question = True

    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=32, choices=STATUSES, default='private')

    def inherit(self):
        pass

    ###################
    #### RESPONSES ####
    ###################

    def get_responses(self):
        return self.responses.all()

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

        return False


class Response(DeskBase):
    is_response = True

    question = models.ForeignKey('desk.Question', related_name='responses')
    status = models.CharField(
        max_length=32, choices=STATUSES_EXTENDED, default='inherit')
    accepted = models.BooleanField(default=False)

    points = models.PositiveIntegerField(default=0)
