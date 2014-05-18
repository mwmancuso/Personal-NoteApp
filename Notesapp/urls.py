"""Primary URL router for Notesapp."""

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Notesapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # TODO Organize this somehow

    url(r'^admin/', include(admin.site.urls)),
    url(r'^backend/', include('backend.urls')),

    url(r'^$', 'common.views.index', name='index'),
)
