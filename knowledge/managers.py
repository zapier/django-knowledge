from django.db import models

Q = models.Q


class QuestionManager(models.Manager):
    def can_view(self, user):
        qs = super(QuestionManager, self).get_query_set()

        if user.is_staff or user.is_superuser:
            return qs.all()

        if user.is_anonymous():
            return qs.filter(status='public')
        else:
            return qs.filter(
                Q(status='public') | Q(status='private', user=user)
            )


class ResponseManager(models.Manager):
    def can_view(self, user):
        qs = super(ResponseManager, self).get_query_set()

        if user.is_staff or user.is_superuser:
            return qs.all()

        if user.is_anonymous():
            return qs.filter(status='public')
        else:
            return qs.filter(
                Q(status='public') | Q(status='private', user=user) |
                Q(
                    Q(status='inherit') &
                    Q(
                        Q(question__status__in=['public'])
                    )
                )
            )
