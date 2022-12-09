from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Electronicshop'

    def ready(self):
        print("I am starting")