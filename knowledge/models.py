from knowledge import settings

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


class Category(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    lastchanged = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __unicode__(self):
        return self.title


class KnowledgeBase(models.Model):
    """
    The base class for Knowledge models.
    """
    is_question = False
    is_response = False

    added = models.DateTimeField(auto_now_add=True)
    lastchanged = models.DateTimeField(auto_now=True)

    user = models.ForeignKey('auth.User', blank=True,
                             null=True, db_index=True)

    # for anonymous posting, if permitted
    name = models.CharField(max_length=64, blank=True, null=True,
        help_text='Enter your first and last name.')
    email = models.EmailField(blank=True, null=True,
        help_text='Enter a valid email address.')


    #########################
    #### GENERIC GETTERS ####
    #########################

    get_name = lambda self: (self.name or '{0} {1}'.format(
        self.user.first_name, self.user.last_name))

    get_email = lambda self: self.email or self.user.email


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

    def public(self, save=True):
        self.switch('public', save)

    def private(self, save=True):
        self.switch('private', save)

    def inherit(self, save=True):
        self.switch('inherit', save)

    def internal(self, save=True):
        self.switch('internal', save)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.user and self.name and self.email\
                and not self.id: 
            # first time because no id
            self.public(save=False)

        if settings.AUTO_PUBLICIZE and not self.id:
            self.public(save=False)

        super(KnowledgeBase, self).save(*args, **kwargs)


class Question(KnowledgeBase):
    is_question = True

    title = models.CharField(max_length=255,
        verbose_name='Question',
        help_text='Enter your question or suggestion.')
    body = models.TextField(blank=True, null=True,
        verbose_name='Description',
        help_text='Please offer details. Markdown enabled.')

    status = models.CharField(
        max_length=32, choices=STATUSES,
        default='private', db_index=True)

    locked = models.BooleanField(default=False)

    categories = models.ManyToManyField('knowledge.Category')

    objects = QuestionManager()

    def inherit(self):
        pass

    def internal(self):
        pass

    def flip_lock(self, save=True):
        self.locked = not self.locked
        if save:
            self.save()

    ###################
    #### RESPONSES ####
    ###################

    def get_responses(self, user=None):
        responses = self.responses.all()
        if user:
            return [r for r in responses if r.can_view(user)]
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
        return any([r.accepted for r in self.get_responses()])
    
    def clear_accepted(self):
        self.get_responses().update(accepted=False)

    def accept(self, response=None):
        """
        Given a response, make that the one and only accepted answer.
        Similar to StackOverflow.
        """
        self.clear_accepted()

        if response and response.question == self:
            response.accepted = True
            response.save()
            return True
        else:
            return False

    def states(self):
        """
        Handy for checking for mod bar button state.
        """
        return [self.status, 'flip_lock' if self.locked else None]

    @models.permalink
    def get_absolute_url(self):
        from django.template.defaultfilters import slugify

        if settings.SLUG_URLS:
            return ('knowledge_thread', [self.id, slugify(self.title)])
        else:
            return ('knowledge_thread_no_slug', [self.id])
    
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-added']


class Response(KnowledgeBase):
    is_response = True

    question = models.ForeignKey('knowledge.Question',
        related_name='responses')

    body = models.TextField(blank=True, null=True,
        verbose_name='Response',
        help_text='Please enter your response. Markdown enabled.')
    status = models.CharField(
        max_length=32, choices=STATUSES_EXTENDED,
        default='inherit', db_index=True)
    accepted = models.BooleanField(default=False)

    objects = ResponseManager()

    def states(self):
        """
        Handy for checking for mod bar button state.
        """
        return [self.status, 'accept' if self.accepted else None]

    def accept(self):
        self.question.accept(self)
    
    def __unicode__(self):
        return self.body[0:100] + u'...'

    class Meta:
        ordering = ['added']
