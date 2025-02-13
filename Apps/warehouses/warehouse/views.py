from django.shortcuts import get_object_or_404
from WareHouse.models import Warehouse, Shelf, Product
from Lib.UI import render, redirect, Page
from django.db.models import Sum
from WareHouse.tasks import syncGlobalStock

# Список полок в складе
def shelf_list(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    shelves = Shelf.objects.filter(warehouse=warehouse)
    page = Page('Склад', warehouse.name, 'Полки в текущем складе')
    page.returnUrl('/GK/warehouses/')
    return render(request, page, 'warehouses/warehouse/shelfs.html', {'warehouse': warehouse, 'shelves': shelves})

# Создание полки
def shelf_create(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    if request.method == 'POST':
        number = request.POST.get('number')
        name = request.POST.get('name')
        if number and name:
            Shelf.objects.create(number=number, name=name, warehouse=warehouse)
            return redirect(f'/GK/warehouses/{ warehouse.id }/shelves')
    page = Page('Склад', warehouse.name, 'Создание полки в складе')
    page.returnUrl('/GK/warehouses/')
    return render(request, page,  'warehouses/warehouse/shelf_create.html', {'warehouse': warehouse})


def warehouse_products(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    shelves = Shelf.objects.filter(warehouse=warehouse)

    # Агрегация данных
    products_data = {}
    for shelf in shelves:
        products = Product.objects.filter(shelf=shelf)
        for product in products:
            if product.plu not in products_data:
                products_data[product.plu] = {
                    'name': product.name,
                    'total_quantity': 0,
                    'global_stock': 0,
                    'locations': []
                }
            products_data[product.plu]['total_quantity'] += product.stock_on_shelf
            products_data[product.plu]['global_stock'] = product.global_stock
            products_data[product.plu]['locations'].append((shelf.id, shelf.name, product.stock_on_shelf))

    # Преобразование данных в список для передачи в шаблон
    products_list = [
        {
            'plu': plu,
            'name': data['name'],
            'total_quantity': data['total_quantity'],
            'global_stock': data['global_stock'],
            'locations': [
                f"<a href='/GK/warehouses/shelf/{shelf_id}/'>{shelf_name} - {quantity}</a>"
                for shelf_id, shelf_name, quantity in data['locations']
            ]
        }
        for plu, data in products_data.items()
    ]
    page = Page('Склад', 'Реестр склада', 'Полный список товаров в складе')
    return render(request, page,  'warehouses/warehouse_products.html', {'warehouse': warehouse, 'products': products_list})


def updataGlobalStock(request, warehouse_id):
    # Создать сплеш о синхронизации(Позже)
    syncGlobalStock.delay(request, warehouse_id)