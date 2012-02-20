import os

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^knowledge/', include('knowledge.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(
                os.path.dirname(__file__), '../knowledge/static'
            ).replace('\\','/')}),
)
