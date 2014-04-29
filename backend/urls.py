# TODO Docstring
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'v1.0.0/', include('backend.v1_0_0.urls'))
)