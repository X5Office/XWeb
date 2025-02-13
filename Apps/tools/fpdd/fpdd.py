from Lib.UI import render, Page
from ServerAPI import write_offs
from assets.models import FPDD_DocConnectED

def main(request):
    doc = write_offs.getList(request)
    page = Page('FDPP | WebGK', 'Документы списаний ЭД', 'Приемка и утилизация товаров')
    page.returnUrl('/GK/menu/tools/')
    return render(request, page, 'tools/fpdd/main.html', {"offs": doc})


def docPanel(request, id):
    context = {}
    doc = write_offs.offsData(request, id)
    context['off'] = doc
    write_offs_positions = write_offs.positions(request, doc["id"])
    context['positions'] = write_offs_positions
    if FPDD_DocConnectED.objects.filter(writeOffs=id).count() == 1:
        # Найдена запись
        dmp = FPDD_DocConnectED.objects.get(writeOffs=id)
        
        if dmp.liCreationState == 'none':
            context['eddc_e'] = 'Документ коррекции отсувствует в BO или его Id обвязки некорректен!'
        elif dmp.liCreationState == 'started':
            context['eddc_e'] = 'Документ коррекции создается в BO, ожидайте завершиния процесса'
        elif dmp.liCreationState == 'created':
            context['eddc_i'] = dmp
        elif dmp.liCreationState == 'completed':
            context['eddc_i'] = dmp
        else:
            pass
            
        context['li_positions'] = {}
        
    elif FPDD_DocConnectED.objects.filter(writeOffs=id).count() == 0:
        # Записи нет
        pass
    else:
        # Какая то хуета, более одной записи или что то ещё
        pass
    
    page = Page('ФПДЭД | WebGK', 'Списание товара доставки', f'{doc["docNumber"]}')
    page.returnUrl('/GK/tools/fpdd/')
    return render(request, page, 'tools/fpdd/doc_panel.html', context)
    
 
def createLocal(request, id):
    writeoffs = write_offs.offsData(request, id)
    WO_positions = write_offs.positions(request, id)
    order_id = writeoffs['name'].split('азу ')[1]


    #2. Создать ЛИ с определёнными данными
    li_req = localInventory.createDoc(request, f'....: {order_id}')




    #3. Добавить позиции
