from django.views.generic import View

from api.generic import ApiMixin
from errors import validators

class PasswordValidatorView(ApiMixin, View):
    """API view that validates POST 'password' against validator."""

    def post(self, request, *args, **kwargs):
        """Handles PasswordValidatorView POST API response."""

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