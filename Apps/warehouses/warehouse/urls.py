from django.urls import path, include
from Apps.warehouses.warehouse import views

urlpatterns = [
    
    path('shelves/', views.shelf_list, ),
    path('shelves/create/', views.shelf_create),
    path('registry/', views.warehouse_products),
    path('update_global_stock/', views.updataGlobalStock),
    path('pack/', include('Apps.warehouses.pack.urls')),
]
