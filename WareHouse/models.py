from django.db import models
from Core.models import User 
from WGKApi.models import ProductGroup

class Warehouse(models.Model):
    name = models.CharField('Наименование склада',max_length=255)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склада'

    def __str__(self):
        return self.name

class Shelf(models.Model):
    number = models.CharField('Номер полки', max_length=50)
    name = models.CharField('Наименование  полки', max_length=255)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='shelves')

    class Meta:
        verbose_name = 'Полка'
        verbose_name_plural = 'Полки'

    def __str__(self):
        return f"{self.name} (Полка № {self.number})"

class Product(models.Model):
    plu = models.CharField('PLU', max_length=50, unique=False)
    name = models.CharField('Наименованеи', max_length=255)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    stock_on_shelf = models.IntegerField('Остаток на полке')
    global_stock = models.IntegerField('Остаток в GK')
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, related_name='products')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='products')
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        unique_together = ('shelf', 'warehouse', 'plu')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    STATUS_CHOICES = [
        ('creating', 'Создается'),
        ('new', 'Создана'),
        ('collecting_data', 'Сбор данных'),
        ('pack', 'Выкладка'),
        ('close', 'Завершена')
    ]
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='inventories')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventories')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    status = models.CharField('Статус', max_length=35, choices=STATUS_CHOICES, default='open')
    class Meta:
        verbose_name = 'Выкладка'
        verbose_name_plural = 'Выкладки'

    def __str__(self):
        return f"Inventory {self.id} for {self.warehouse.name}"

class InventoryItem(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает проверки'),
        ('pack_pending', 'Ожидает выкладки'),
        ('processed', 'Обработано')
        
    ]
    plu = models.CharField('PLU', max_length=50)
    name = models.CharField('Наименование', max_length=255)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.SET_NULL, related_name='items', null=True, blank=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='items')
    quantity_to_display = models.IntegerField('Количество к выкладке', null=True, blank=True)
    status = models.CharField('Статус обработки', max_length=50, choices=STATUS_CHOICES, default='pending')
    accommodations = models.ManyToManyField(Product)
    total_stock = models.IntegerField('Суммарный остаток на складе')
    class Meta:
        verbose_name = 'Товар выкладки'
        verbose_name_plural = 'Товары выкладки'

    def __str__(self):
        return f"{self.name} (PLU: {self.plu})"
