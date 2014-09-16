from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'releases.views.releases', name='releases'),
    url(r'^docs/$', 'releases.views.docs', name='releases_docs'),
    url(r'^latest-urls/(?P<type>\w+)/$', 'releases.views.latest_urls', name='releases_latest_urls'),
)

