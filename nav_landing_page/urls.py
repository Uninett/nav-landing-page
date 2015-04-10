from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^$', 'nav_landing_page.views.home', name='home'),
    url(r'^releases/', include('releases.urls')),
    url(r'^install-instructions/$', 'nav_landing_page.views.install_instructions', name='install_instructions'),
    url(r'^install-instructions/$', 'nav_landing_page.views.install_instructions', name='install_instructions'),
    url(r'^404/$', 'nav_landing_page.views.handler_404', name='404'),

    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'nav_landing_page.views.handler_404'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
