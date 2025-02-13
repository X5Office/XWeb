from Lib.UI import render, Page, redirect
from WareHouse.models import Warehouse, Inventory
from django.shortcuts import get_object_or_404
from WareHouse.tasks import createPackDoc

def pack_list(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    inventories = Inventory.objects.filter(warehouse=warehouse)
    page = Page('Выкладка склада', 'Выкладка склада', 'Задания на чистку складов')
    page.returnUrl(f'/GK/warehouses/{ warehouse_id }/shelves/')
    return render(request, page,  'warehouses/pack/list.html', {'warehouse': warehouse, 'inventories': inventories})
    
    
def pack_create(request, warehouse_id):
    doc = Inventory(warehouse=get_object_or_404(Warehouse, id=warehouse_id), author=request.user, status='creating')
    doc.save()
    createPackDoc.delay(doc.id)
    return redirect(f'/GK/warehouses/{warehouse_id}/pack')
    
    
    
def doc_info(request, warehouse_id,  pack_task_id):
    page = Page('Выкладка', f'Выкладка №{pack_task_id}', 'Информация о задании выкладки')
    return render(request, page, 'warehouses/pack/doc_info.html')