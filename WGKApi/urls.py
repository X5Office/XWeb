from django.urls import path, include


urlpatterns = [
    # Менеджер товаров склада 
    path('warehouses/', include('WGKApi.WareHouseAPI.urls'))
]
