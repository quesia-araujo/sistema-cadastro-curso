from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = "Módulo geral" # visualização no painel administrativo
    name = 'base'
