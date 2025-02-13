from Lib.UI import Page, render
from WareHouse.models import InventoryItem

def pack_list(request, warehouse_id, pack_task_id):
    items = InventoryItem.objects.filter(inventory=pack_task_id, status='pack_pending')
    page = Page('Выкладка', 'Выкладка товара в зал', 'Пройдите по списку и переместите товар')
    return render(request, page, 'warehouses/pack/worker/finish.html', {'inventory_items': items})