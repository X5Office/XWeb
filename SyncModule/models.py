from django.db import models

class ChangeLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    app_label = models.CharField(max_length=50)
    model_name = models.CharField(max_length=255)
    record_id = models.IntegerField()
    change_type = models.CharField(max_length=10)  # 'insert', 'update', 'delete'
    new_state = models.JSONField()
    synced = models.BooleanField(default=False)
