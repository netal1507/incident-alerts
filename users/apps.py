from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # <- Add this
    name = 'users'

class IncidentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # <- Add this
    name = 'incidents'
