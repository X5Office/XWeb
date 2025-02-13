from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from Lib.serializations import model_to_dict
from SyncModule.models import ChangeLog
from WGKApi.models import ProductGroup, UnitOfMeasureCode, GKProduct, Barcode

app_label = 'WGKApi'

@receiver(post_save, sender=ProductGroup)
@receiver(post_save, sender=UnitOfMeasureCode)
@receiver(post_save, sender=GKProduct)
@receiver(post_save, sender=Barcode)
def log_change(sender, instance, created, **kwargs):
    if getattr(instance, '_is_local_sync', False):
        return

    change_type = 'insert' if created else 'update'
    new_state = model_to_dict(instance)
    ChangeLog.objects.create(
        app_label=app_label,
        model_name=sender.__name__,
        record_id=instance.id,
        change_type=change_type,
        new_state=new_state
    )

@receiver(post_save, sender=ProductGroup)
@receiver(post_save, sender=UnitOfMeasureCode)
@receiver(post_save, sender=GKProduct)
@receiver(post_save, sender=Barcode)
def log_delete(sender, instance, **kwargs):
    if getattr(instance, '_is_local_sync', False):
        return

    ChangeLog.objects.create(
        app_label=app_label,
        model_name=sender.__name__,
        record_id=instance.id,
        change_type='delete',
        new_state={}
    )


