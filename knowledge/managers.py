from django.db import models

Q = models.Q


class KnowledgeBaseManager(models.Manager):
    def can_view(self, user=None):
        qs = super(KnowledgeBaseManager, self).get_query_set()

        if user.is_staff or user.is_superuser:
            return qs.all()

        if user.is_anonymous():
            return qs.filter(status='public')
        else:
            return qs.filter(
                Q(status='public') | Q(status='private', user=user)
            )
