# Define database definitions to use for specific apps
app_databases = {
    'authentication': {
        'rw':   'authentication',
        'ro':   'authentication_ro'
    }
}

class AppRouter(object):
    """
    Router that routes specific apps to specific database definitions if defined.
    """
    def db_for_read(self, model, **hints):
        """
        Routes read only calls to defined read only database definition.
        """
        if model._meta.app_label in app_databases:
            return app_databases[model._meta.app_label]['ro']
        else:
            return 'default'
    
    
    def db_for_write(self, model, **hints):
        """
        Routes write calls to defined read/write database definition.
        """
        if model._meta.app_label in app_databases:
            return app_databases[model._meta.app_label]['rw']
        else:
            return 'default'