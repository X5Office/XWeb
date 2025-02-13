from django.urls import path, include
from Apps.warehouses.pack.worker import views,finish

urlpatterns = [
    path('', views.main_doc),
    path('collect_data', views.collect_data),
    path('packing', finish.pack_list)
    
    
]
