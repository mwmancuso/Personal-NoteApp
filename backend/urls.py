from django.conf.urls import patterns, include, url
from backend import validator

validator_list = patterns('',
    url(r'password', validator.PasswordValidatorView.as_view()),
)

urlpatterns = patterns('',
    url(r'validator/', include(validator_list))
)