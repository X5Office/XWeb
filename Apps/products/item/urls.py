from django.urls import path, include
from Apps.products.item import info

urlpatterns = [
    path('', info.search)
]