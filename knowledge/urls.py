from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('knowledge.views',
    url(r'^$', 'knowledge_index', name='knowledge_index'),
    url(r'^questions/$', 'knowledge_list', name='knowledge_list'),
    url(r'^questions/(?P<tags>[a-z-]+)/$', 'knowledge_list', name='knowledge_list_tags'),
    url(r'^questions/(?P<question_id>\d+)/(?P<slug>[a-z0-9-]+)/$',
        'knowledge_thread', name='knowledge_thread'),
    url(r'^ask/$', 'knowledge_ask', name='knowledge_ask'),
)
