from django.conf import settings

ALLOW_ANONYMOUS = getattr(settings, 'KNOWLEDGE_ALLOW_ANONYMOUS', False)
AUTO_PUBLICIZE = getattr(settings, 'KNOWLEDGE_AUTO_PUBLICIZE', False)
FREE_RESPONSE = getattr(settings, 'KNOWLEDGE_FREE_RESPONSE', True)
SLUG_URLS = getattr(settings, 'KNOWLEDGE_SLUG_URLS', True)
DELIVER_JSON = getattr(settings, 'KNOWLEDGE_DELIVER_JSON', False)

BASE_TEMPLATE = getattr(settings, 'KNOWLEDGE_BASE_TEMPLATE',
    'django_knowledge/base.html')
