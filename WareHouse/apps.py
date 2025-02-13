from django.apps import AppConfig


class WarehauseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WareHouse'
    verbose_name = 'Система складов'
    def ready(self):
        import WareHouse.signals