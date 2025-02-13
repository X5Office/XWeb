from datetime import datetime
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Warehouse, Shelf, Product, Inventory, InventoryItem


models = [Warehouse, Shelf, Product, Inventory, InventoryItem]
# Словарь для хранения состояния записи до сохранения
old_state = {}

# Универсальный обработчик для pre_save
def universal_pre_save(sender, instance, **kwargs):
    if instance.pk:  # Если запись уже существует в базе данных
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            old_state[instance.pk] = {
                field.name: getattr(old_instance, field.name)
                if not field.is_relation else getattr(old_instance, field.name).pk
                for field in old_instance._meta.fields
                if not field.is_relation or field.many_to_one
            }
            # Обработка ManyToManyField
            old_state[instance.pk].update({
                field.name: list(getattr(old_instance, field.name).values_list('pk', flat=True))
                for field in old_instance._meta.many_to_many
            })
        except sender.DoesNotExist:
            pass

# Универсальный обработчик для post_save
def universal_post_save(sender, instance, created, **kwargs):
    if getattr(instance, '_is_sync', False):
        return
    if True:
        change_type = 'create' if created else 'update'
        log = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "changes": {
                "app": sender._meta.app_label,
                "table": sender.__name__,
                "record_id": instance.id,
                "change_type": change_type,
                "old_state": old_state.pop(instance.pk, {}),
                "new_state": {
                    field.name: getattr(instance, field.name)
                    if not field.is_relation else getattr(instance, field.name).pk
                    for field in instance._meta.fields
                    if not field.is_relation or field.many_to_one
                },
                "updated_fields": []
            },
            "status": ""
        }

        # Обработка ManyToManyField
        log["changes"]["new_state"].update({
            field.name: list(getattr(instance, field.name).values_list('pk', flat=True))
            for field in instance._meta.many_to_many
        })

        # Определение измененных полей
        old_data = log["changes"]["old_state"]
        new_data = log["changes"]["new_state"]
        log["changes"]["updated_fields"] = [
            field for field in new_data
            if new_data[field] != old_data.get(field)
        ]

        # Здесь можно добавить логику для сохранения лога, например, в базу данных или файл
        print(log)

# Универсальный обработчик для post_delete
def universal_post_delete(sender, instance, **kwargs):
    if True:

        try:
            ids_rec = int(instance.id)
        except Exception:
            ids_rec = 0
        log = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "changes": {
                "app": sender._meta.app_label,
                "table": sender.__name__,
                "record_id": ids_rec,
                "change_type": "delete",
                "old_state": old_state.pop(instance.pk, {}),
                "new_state": {},
                "updated_fields": []
            },
            "status": ""
        }

        # Здесь можно добавить логику для сохранения лога, например, в базу данных или файл
        print(log)

# Подключение обработчиков к моделям

for model in models:
    pre_save.connect(universal_pre_save, sender=model)
    post_save.connect(universal_post_save, sender=model)
    post_delete.connect(universal_post_delete, sender=model)
