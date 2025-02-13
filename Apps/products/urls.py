from django.urls import path, include

urlpatterns = [
    # Информация о товаре
    path('items/', include('Apps.products.item.urls'))
]