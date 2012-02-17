from django.conf import settings

ALLOW_ANONYMOUS = getattr(settings, 'DESK_ALLOW_ANONYMOUS', False)
AUTO_PUBLICIZE = getattr(settings, 'DESK_AUTO_PUBLICIZE', False)
FREE_RESPONSE = getattr(settings, 'DESK_FREE_RESPONSE', False)
ALLOW_RATING = getattr(settings, 'DESK_ALLOW_RATING', True)
SLUG_URLS = getattr(settings, 'DESK_SLUG_URLS', True)
LOAD_JQUERY = getattr(settings, 'DESK_LOAD_JQUERY', True)
