from hashlib import md5

from django.template import Library

register = Library()

@register.simple_tag
def get_gravatar(email, size=80, rating='g', default=None):
    """Return url for a Gravatar"""
    url = 'https://secure.gravatar.com/avatar/{0}.jpg'.format(
        md5(email.strip().lower()).hexdigest())
    )
    options = {'s': size, 'r': rating}
    if default:
        options['d'] = default

    url = '%s?%s' % (url, urlencode(options))
    return url.replace('&', '&amp;')