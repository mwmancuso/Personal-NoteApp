"""Default URL router for backend."""

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'v1/', include('backend.v1.urls'))
)