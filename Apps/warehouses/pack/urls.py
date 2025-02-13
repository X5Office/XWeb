from django.urls import path, include
from Apps.warehouses.pack import views

urlpatterns = [
    path('', views.pack_list),
    path('create/', views.pack_create),
    path('<int:pack_task_id>/', include('Apps.warehouses.pack.worker.urls')),
    
]
