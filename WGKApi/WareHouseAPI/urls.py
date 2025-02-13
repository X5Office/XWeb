from django.urls import path
from . import release

urlpatterns = [
    path('shelves/<int:product_id>/delete/', release.delete_product, name='delete_product'),
    path('shelves/<int:product_id>/update_quantity/', release.update_product_quantity, name='update_product_quantity'),
    path('shelves/<int:product_id>/move/', release.move_product, name='move_product'),
    path('shelves/<int:shelf_id>/add/', release.add_product, name='add_product'),
]
