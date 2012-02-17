from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^knowledge/', include('knowledge.urls')),
)
