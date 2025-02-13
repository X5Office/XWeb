from django.urls import path, include
from Apps.warehouses.shelf import views

urlpatterns = [
    path('<int:shelf_id>/', views.shelf_detail),
]
