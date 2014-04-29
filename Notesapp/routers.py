# TODO Docstring
# Define database definitions to use for specific apps
app_databases = {
    'authentication': {
        'rw': 'authentication',
        'ro': 'authentication_ro',
        'relation': True,
    }
}

class AppRouter(object):
    """Routes specific apps to specific databases if app is defined."""
    def db_for_read(self, model, **hints):
        if model._meta.app_label in app_databases:
            return app_databases[model._meta.app_label]['ro']
        else:
            return 'default'


    def db_for_write(self, model, **hints):
        if model._meta.app_label in app_databases:
            return app_databases[model._meta.app_label]['rw']
        else:
            return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in app_databases or\
            obj2._meta.app_label in app_databases:
            return app_databases[obj1._meta.app_label]['relation'] or\
                app_databases[obj2._meta.app_label]['relation']
        else:
            return None