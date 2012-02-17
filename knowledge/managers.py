from django.db import models

class KnowledgeBaseManager(models.Manager):
    def can_view(self, user):
        return super(KnowledgeBaseManager, self).get_query_set()