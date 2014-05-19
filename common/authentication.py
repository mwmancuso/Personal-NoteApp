"""Defines site-specific authentication views."""

from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin, ContextMixin
from ratelimit.mixins import RateLimitMixin
from authentication import models
from common.generic import CleanRequestMixin
from errors.exceptions import UserError
from errors.handlers import UserErrorHandler

# TODO Clean, secure and organize this

class RegisterView(RateLimitMixin, TemplateResponseMixin, ContextMixin,
                   CleanRequestMixin, View):
    """View for user registration."""

    ratelimit_block = True
    ratelimit_rate = '5/m'

    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        user_info = self.clean_post(request, *args, **kwargs)

        try:
            user_object = models.Users.users.create(**user_info)
        except UserError as user_error:
            handler = UserErrorHandler(user_error)

            context['register_successful'] = False
            context['error_string'] = handler.get_count_string()
            context['errors'] = handler.list_translations()

            return self.render_to_response(context)

        context['register_successful'] = True

        self.request.session['user_id'] = user_object.pk
        self.request.session.cycle_key()

        return self.render_to_response(context)

class LoginView(RateLimitMixin, TemplateResponseMixin, ContextMixin,
                CleanRequestMixin, View):
    """View for user login."""

    ratelimit_block = True
    ratelimit_rate = '20/m'

    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        user_info = self.clean_post(request, *args, **kwargs)

        try:
            user_object = models.Users.users.login_password(**user_info)
        except UserError as user_error:
            handler = UserErrorHandler(user_error)

            context['login_successful'] = False
            context['error_string'] = handler.get_count_string()
            context['errors'] = handler.list_translations()

            return self.render_to_response(context)

        context['login_successful'] = True

        self.request.session['user_id'] = user_object.pk
        self.request.session.cycle_key()

        return self.render_to_response(context)