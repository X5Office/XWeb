from WareHouse.models import Inventory, Product, InventoryItem
from ServerAPI.items import item__info
from celery import shared_task
from django.db.models import Sum


@shared_task
def syncGlobalStock(request, warehouse_id):
    products = Product.objects.filter(warehouse=warehouse_id)

    for product in products:
        plu = product.plu
        item_info = item__info(request, plu)

        if item_info:
            product.name = item_info.get('fullName', product.name)
            product.global_stock = item_info.get('stock', -9999)
        else:
            product.global_stock = -9999

        product.save()


@shared_task
def createPackDoc(inventory_id):
    # Найти документ Inventory по переданному ID
    inventory = Inventory.objects.get(id=inventory_id)

    # Получить список всех продуктов, которые соответствуют условиям
    products = Product.objects.filter(warehouse=inventory.warehouse)

    # Сгруппировать продукты по PLU и суммировать их остатки на складе
    plu_groups = products.values('plu', 'name').annotate(total_stock=Sum('stock_on_shelf'))

    # Создать записи в модели InventoryItem
    for group in plu_groups:
        plu = group['plu']
        name = group['name']
        total_stock = group['total_stock']
     #   product_group = group['product_group']
        # Получить все записи Product для данного PLU и warehouse
        accommodations = products.filter(plu=plu)

        # Создать запись в InventoryItem
        inventory_item = InventoryItem.objects.create(
            plu=plu,
            name=name,
            inventory=inventory,
        #    product_group=product_group,
            quantity_to_display=None,
            status='pending',
            total_stock=total_stock
        )

        # Привязать все соответствующие записи Product
        inventory_item.accommodations.set(accommodations)
    inventory.status = 'new'
    inventory.save()
    return print("Inventory items created successfully.")
