from django.urls import path, include
from Apps.warehouses import views

urlpatterns = [
    path('', views.list),
    path('create/', views.create),
    path('shelf/', include('Apps.warehouses.shelf.urls')),
    path('<int:warehouse_id>/', include('Apps.warehouses.warehouse.urls')),
]
