from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^desk/', include('desk.urls')),
)
