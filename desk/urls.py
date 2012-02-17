from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('desk.views',
    url(r'^$', 'desk_index', name='desk_index'),
    url(r'^questions/$', 'desk_list', name='desk_list'),
    url(r'^questions/(?P<tags>[a-z-]+)/$', 'desk_list', name='desk_list_tags'),
    url(r'^questions/(?P<question_id>\d+)/(?P<slug>[a-z0-9-]+)/$', 'desk_thread', name='desk_thread'),
    url(r'^ask/$', 'desk_ask', name='desk_ask'),
)
