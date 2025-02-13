from Lib.UI import render, Page, MasterMenu


def turnover(request):
    page = Page('Товары', 'Товары', 'Выполнение операций над товаром')
    menu = MasterMenu()
    menu.add('Информация о товаре', '/GK/products/items/', '/static/icon/colored/search.png')
    menu.add('Возвраты, отгрузка, перемещение товаров', '/GK/', '/static/icon/colored/logistic.png')
    menu.add('Локальная инвентаризация', '/GK/inventory/local/', '/static/icon/colored/inventory.png', '80')
    menu.add('Списания', '/GK/write-offs/', '/static/icon/colored/turnover.png', '80')
    menu.add('Уценка', '/GK/', '/static/icon/colored/low-price.png')
    menu.add('Склад', '/GK/warehouses/', '/static/icon/colored/basket.png')
    menu.add('Локальный реестр товаров', '/GK/products/localItemsRegistry', '/static/icon/colored/registry.png')
    return render(request, page, 'Core/menu_builder.html', {'menu': menu.build()})


def tools(request):
    page = Page('Инструменты', 'Инструменты', 'Обработчики для док-ов и задач')
    menu = MasterMenu()
    menu.add('Печать ценников', '/GK/', '/static/icon/colored/price-tag.png')
    menu.add('Печать этикеток (QR)', '/GK/tools/FPDD/', '/static/icon/colored/label.png')
    menu.add('Файлы', '/GK/files/', '/static/icon/colored/file-transfer.png')
    menu.add('Печать документа', '/GK/', '/static/icon/colored/print.png')
    menu.add('Доступность (Проводка)', '/GK/tools/accessibility/', '/static/icon/colored/accessibility.png', '0')
    menu.add('Сигналы УТП (Проводка)', '/GK/tools/YTP/', '/static/icon/colored/ytp.png', '6')
    return render(request, page, 'Core/menu_builder.html', {'menu': menu.build()})
    

def delivery(request):
    page = Page('Система доставки', "Доставка", 'Управление доставкой')
    menu = MasterMenu()
    menu.add('Фиктивная проводка документов доставки', '/GK/tools/fpdd/', '/static/icon/colored/storno.png')
    menu.add('Пользователи Telegram', '/GK/delivery/users/', '/static/icon/colored/telegram.png')
    menu.add('Запросы DataMatrix', '/GK/tools/fpdd/', '/static/icon/colored/qr.png' )
    return render(request, page, 'Core/menu_builder.html', {'menu': menu.build()})

def profile(request):
    page = Page('Профиль', 'Профиль', 'Настройки пользователя/системы')
    menu = MasterMenu()
    menu.add('Принтеры', '/GK/settings/',  '/static/icon/colored/printers.png')
    menu.add('WebGK AdminPanel', '/admin/', '/static/icon/colored/admin.png')
    menu.add('Выход', '', '/static/icon/colored/exit.png')

    return render(request, page, 'Core/menu_builder.html', {'menu': menu.build()})