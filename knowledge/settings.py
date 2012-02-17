from django.conf import settings

ALLOW_ANONYMOUS = getattr(settings, 'KNOWLEDGE_ALLOW_ANONYMOUS', False)
AUTO_PUBLICIZE = getattr(settings, 'KNOWLEDGE_AUTO_PUBLICIZE', False)
FREE_RESPONSE = getattr(settings, 'KNOWLEDGE_FREE_RESPONSE', False)
ALLOW_RATING = getattr(settings, 'KNOWLEDGE_ALLOW_RATING', True)
SLUG_URLS = getattr(settings, 'KNOWLEDGE_SLUG_URLS', True)
LOAD_JQUERY = getattr(settings, 'KNOWLEDGE_LOAD_JQUERY', True)
