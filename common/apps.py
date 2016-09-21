# objective: perform initialization tasks, in this case registering signals when the application first loads.
# ensure signal handlers/receivers gets imported so that your signal receivers get registered
# https://docs.djangoproject.com/en/1.8/topics/signals/#connecting-receiver-functions
# https://docs.djangoproject.com/en/1.8/ref/applications/#django.apps.AppConfig.ready
# https://chriskief.com/2014/02/28/django-1-7-signals-appconfig/

from django.apps import AppConfig


class CommonAppConfig(AppConfig):
    # make sure to set the default_app_config variable to this class  in application’s __init__.py
    name = 'common'
    verbose_name = 'common app'

    def ready(self):
        """
        Subclasses can override this method to perform initialization tasks such as registering signals.
        It is called as soon as the registry is fully populated.
        """
        import common.signals.handlers
