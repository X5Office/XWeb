from django.db import models

class TGUser(models.Model):
    objects = None
    user_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    sap_number = models.CharField(max_length=50)
    is_store_admin = models.BooleanField('Пользователь является административным?', default=False)
    admin_mode = models.BooleanField('Пользователь принимает административные сообщения', default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class RequestDataMatrixLog(models.Model):
    user = models.ForeignKey(TGUser, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20) #GTIN or PLU
    in_value = models.CharField(max_length=100) # Входное значение(или штрихкод или плюшка)
    request_status = models.CharField(max_length=50)
    # Статус запроса
    # completed - datamatrix сгененрирован
    # item_not_found - товар по plu не найден

    #item =  ТУТ ДОЛЖНА БЫТЬ ПРИВЯЗА К ЛОКАЛЬНОМУ РЕЕСТРУ ТОВАРОВ
    datamatrix_count = models.IntegerField()
    request_reason = models.CharField(max_length=1000)
    requets_is_processed = models.BooleanField(default=False)