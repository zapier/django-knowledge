from django.db import models
from django.db.models import Q


class QuestionManager(models.Manager):
    # def get_query_set(self, *args, **kwargs):
    #     return super(QuestionManager, self).get_query_set(*args, **kwargs)

    def can_view(self, user):
        qs = super(QuestionManager, self).get_query_set()\
                                         .select_related('user')

        if user.is_staff or user.is_superuser:
            return qs.all()

        if user.is_anonymous():
            return qs.filter(status='public')

        return qs.filter(
            Q(status='public') | Q(status='private', user=user)
        )


class ResponseManager(models.Manager):
    # def all(self, *args, **kwargs):
    #     return super(ResponseManager, self).all(*args, **kwargs)\
    #                                        .select_related('question', 'user')

    def can_view(self, user):
        qs = super(ResponseManager, self).get_query_set()\
                                         .select_related('question', 'user')

        if user.is_staff or user.is_superuser:
            return qs.all()

        if user.is_anonymous():
            return qs.filter(
                Q(status='public') |
                Q(status='inherit', question__status='public')
            )

        # ooooh boy this is crazy!
        return qs.filter(
            Q(status='public') |
            Q(  # respect private parent user/status
                Q(status='private') &
                Q(
                    Q(user=user) |
                    Q(question__user=user)
                )
            ) |
            Q(  # follow inherited status/users
                Q(status='inherit') &
                Q(
                    Q(question__status='public') |
                    Q(question__status='private', question__user=user)
                )
            )
        )
