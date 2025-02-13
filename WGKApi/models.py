from django.db import models
from Core.models import User


class Files(models.Model):
    
    name = models.CharField('Наименование файла', max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.CharField('UUID', max_length=100)
    type = models.CharField('Расширение файла', max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
# Кусок кода ответственного за выбор типа категориии товара, пока не работоспособен, возможно нужно уточнить список всех возможных типов
class ProductGroup(models.Model):
 #   PRODUCT_TYPE_CHOICES = [
 #       ('FR', 'Fresh'),
 #       ('FD', 'Frozen'),
        # Добавьте другие типы товаров по мере необходимости
 #   ]

    product_type = models.CharField(max_length=2,)# choices=PRODUCT_TYPE_CHOICES)
    group_code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product_type}{self.group_code} - {self.name}"

    class Meta:
        verbose_name = 'Product Group'
        verbose_name_plural = 'Product Groups'
        ordering = ['product_type', 'group_code']

class UnitOfMeasureCode(models.Model):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=100)

class GKProduct(models.Model):
    plu = models.IntegerField(unique=True)
    shortName = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    merchendiseGroup = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    unitOfMeasureCode = models.ForeignKey(UnitOfMeasureCode, on_delete=models.CASCADE)

class Barcode(models.Model):
    code = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(GKProduct, related_name='barcodes', on_delete=models.CASCADE)