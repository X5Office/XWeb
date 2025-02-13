from Lib.UI import Page, render, redirect
from WareHouse.models import InventoryItem, Inventory


def main_doc(request, warehouse_id, pack_task_id):

    packing = Inventory.objects.get(id=pack_task_id)
    page = Page('Выкладка', f'Выкладка №{pack_task_id}', f'Склад для выкладки №{warehouse_id}')
    return render(request, page, 'warehouses/pack/worker/doc_panel.html', {'packing': packing} )


def collect_data(request, warehouse_id, pack_task_id):
    if request.method == 'POST':
        for_pack_stock = int(request.POST['stock'])
        record = InventoryItem.objects.filter(status='pending', inventory=pack_task_id).first()
        record.quantity_to_display = for_pack_stock
        record.status = 'pack_pending'
        record.save()
        return redirect(request.path)
    elif request.method == 'GET':
        item = InventoryItem.objects.filter(status='pending', inventory=pack_task_id).first()
        page = Page('Проверка места в ТЗ', 'Проверка места в ТЗ', 'Найдите места размещения и проверьте')
        return render(request, page, 'warehouses/pack/worker/datacollect.html', {'item': item, 'accommodations': item.accommodations.all()})