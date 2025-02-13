from django.urls import path, include
from Apps import root


urlpatterns = [
    # Дашбоард системы 
    path('', root.dashboard),
    # Меню
    path('menu/', include('Apps.menu.urls')),
    # Товарооборот и товары
    path('products/', include('Apps.products.urls')),
    # Сессии и пользователи
    path('session/', include('Apps.session.urls')),
    # Файлы и файловый обмен
    path('files/', include('Apps.files.urls')),
    # Инструменты
    path('tools/', include('Apps.tools.urls')),
    # Доставка
    path('delivery/', include('Apps.delivery.urls')),
    # Склад 
    path('warehouses/', include('Apps.warehouses.urls')),
    
    
]
