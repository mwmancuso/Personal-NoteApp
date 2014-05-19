"""Validator backend, handles client-side validation."""

from django.views.generic import View
import authentication.models

from backend.v1.generic import BackendApiMixin
from errors import validators
from ratelimit.mixins import RateLimitMixin

class PasswordValidatorView(BackendApiMixin, View):
    """Backend view that validates POST 'password' against validator."""

    def post(self, request, *args, **kwargs):

        test_password = request.POST.get('password')

        if not test_password:
            self.message = 'No password given.'
            self.status = 404
            return self.json_response(request, *args, **kwargs)

        try:
            validators.Password(test_password)
        except ValueError:
            self.message = 'Invalid password.'
            self.status = 404
            return self.json_response(request, *args, **kwargs)

        self.message = 'Good password.'
        return self.json_response(request, *args, **kwargs)


class UsernameAvailabilityView(RateLimitMixin, BackendApiMixin, View):
    """Backend view that checks to see if username is available."""

    ratelimit_block = True
    ratelimit_rate = '1/s'

    def post(self, request, *args, **kwargs):

        test_username = request.POST.get('username')

        if not test_username:
            self.message = 'No username given.'
            self.status = 404
            return self.json_response(request, *args, **kwargs)

        if authentication.models.Users.users.user_exists(
                username=test_username):
            self.message = 'Username taken.'
            self.status = 404
            return self.json_response(request, *args, **kwargs)

        self.message = 'Username available.'
        return self.json_response(request, *args, **kwargs)


class EmailAvailabilityView(RateLimitMixin, BackendApiMixin, View):
    """Backend view that checks to see if username is available."""

    ratelimit_block = True
    ratelimit_rate = '1/s'

    def post(self, request, *args, **kwargs):

        test_email = request.POST.get('email')

        if not test_email:
            self.message = 'No email given.'
            self.status = 404
            return self.json_response(request, *args, **kwargs)

        if authentication.models.Users.users.email_exists(email=test_email):
            self.message = 'Email taken.'
            self.status = 404
            return self.json_response(request, *args, **kwargs)

        self.message = 'Email available.'
        return self.json_response(request, *args, **kwargs)