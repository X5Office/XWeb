from django.shortcuts import get_object_or_404
from Lib.UI import Page, render, redirect
from WareHouse.models import Warehouse, Shelf

# Список складов
def list(request):
    warehouses = Warehouse.objects.all()
    page = Page('Склад', 'Менеджер складов', 'Список существующих складов')
    page.returnUrl('/GK/menu/turnover/')
    return render(request, page, 'warehouses/list.html', {'warehouses': warehouses})
    
# Создание склада
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Warehouse.objects.create(name=name)
            return redirect('/GK/warehouses/')
            
    page = Page('Склад', 'Менеджер складов', 'Создание склада товаров')
    page.returnUrl('/GK/warehouses/')
    return render(request, page, 'warehouses/create.html')