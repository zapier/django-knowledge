from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('knowledge.views',
    url(r'^$', 'knowledge_index', name='knowledge_index'),

    url(r'^questions/$', 'knowledge_list', name='knowledge_list'),

    url(r'^questions/(?P<category_slug>[a-z-]+)/$', 'knowledge_list',
        name='knowledge_list_category'),

    url(r'^questions/(?P<question_id>\d+)/$',
        'knowledge_thread', name='knowledge_thread_no_slug'),

    url(r'^questions/(?P<question_id>\d+)/(?P<slug>[a-z0-9-]+)/$',
        'knowledge_thread', name='knowledge_thread'),

    url(r'^moderate/(?P<model>[a-z]+)/'
        r'(?P<lookup_id>\d+)/(?P<mod>[a-zA-Z0-9_]+)/$',
        'knowledge_moderate', name='knowledge_moderate'),

    url(r'^ask/$', 'knowledge_ask', name='knowledge_ask'),
)
