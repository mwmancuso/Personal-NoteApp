"""Generic mixins and view classes for project."""

class CleanRequestMixin(object):
    """Cleans up data for entry into validators."""

    def clean_post(self, request, *args, **kwargs):
        """Cleans up post data."""

        ignored_keys = ('csrfmiddlewaretoken',)
        post_data = dict()

        for key, value in dict(request.POST).items():
            if key not in ignored_keys:
                if value[0]:
                    post_data[key] = value[0]

        return post_data