"""URL router for backend version 1."""

from django.conf.urls import patterns, include, url
from backend.v1 import validator

validator_list = patterns('',
    url(r'password', validator.PasswordValidatorView.as_view()),
    url(r'username', validator.UsernameAvailabilityView.as_view()),
    url(r'email', validator.EmailAvailabilityView.as_view())
)

urlpatterns = patterns('',
    url(r'validator/', include(validator_list))
)