from django.shortcuts import  get_object_or_404
from Lib.UI import redirect, render, Page
from WareHouse.models import Shelf, Product

def shelf_detail(request, shelf_id):
    shelf = get_object_or_404(Shelf, id=shelf_id)
    products = Product.objects.filter(shelf=shelf)
    shelves = Shelf.objects.filter(warehouse=shelf.warehouse)
    page = Page('Склад', f'Склад: {shelf.warehouse.name}', f'Полка: {shelf.name}')
    page.customMenuInit()
    page.returnUrl(f'/GK/warehouses/{shelf.warehouse.id}/shelves')
    return render(request, page, 'warehouses/warehouse/shelf_detail.html', {'shelf': shelf, 'products': products, 'shelves': shelves})