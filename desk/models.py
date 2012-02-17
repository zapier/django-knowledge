import settings

from django.db import models


STATUSES = (
    ('public', 'Public'),
    ('private', 'Private'),
    ('inheret', 'Inheret'),
    ('internal', 'Internal'),
)

class DeskBase(models.Model):
    """
    The base class for Desk models. 
    """
    added = models.DateTimeField(auto_now_add=True)
    lastchanged = models.DateTimeField(auto_now=True)

    user = models.ForeignKey('auth.User')

    status = models.CharField(max_length=32, choices=STATUSES, default='private')
    body = models.TextField(blank=True, null=True)


    ########################
    #### STATUS METHODS ####
    ########################

    def can_view(self, user):
        return True

    def switch(self, status):
        self.status = status
        self.save()

    def public(self):
        self.switch('public')

    def private(self):
        self.switch('private')

    def inheret(self):
        self.switch('inheret')

    def internal(self):
        self.switch('internal')


    class Meta:
        abstract = True


class Question(DeskBase):
    title = models.CharField(max_length=255)

    def inheret(self):
        pass

    ###################
    #### RESPONSES ####
    ###################

    def get_responses(self):
        return self.responses.all()

    def answered(self):
        return bool(self.get_responses())

    def accepted(self):
        for response in self.get_responses():
            if response.accepted:
                return True
        return False
    
    def accept(self, response):
        if response.question == self:
            self.get_responses().update(accepted=False)
            response.accepted = True
            response.save()
            return True
        return False

    def save(self, *args, **kwargs):
        super(Question, self).save(*args, **kwargs)


class Response(DeskBase):
    question = models.ForeignKey('desk.Question', related_name='responses')
    accepted = models.BooleanField(default=False)