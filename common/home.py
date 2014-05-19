"""Defines site-specific home views."""

from django.views.generic import TemplateView
import meta.models

class HomeView(TemplateView):
    """Home view for project; AKA index."""

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        """Adds in specific data for home view."""

        context = super(HomeView, self).get_context_data(**kwargs)

        token_required = False
        token_object = meta.models.Data.objects.get(tag='new-users')

        if token_object.setting == 0 and token_object.data == 'token':
            token_required = True

        context['token_required'] = token_required

        if 'user_id' in self.request.session:
            context['user_id'] = self.request.session['user_id']

        return context