"""Primary URL router for Notesapp."""

from django.conf.urls import patterns, include, url
from django.contrib import admin
import common.home
import common.authentication

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Notesapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # TODO Organize this somehow

    url(r'^admin/', include(admin.site.urls)),
    url(r'^backend/', include('backend.urls')),

    url(r'^$', common.home.HomeView.as_view()),
    url(r'^register', common.authentication.RegisterView.as_view()),
    url(r'^login', common.authentication.LoginView.as_view()),
)
