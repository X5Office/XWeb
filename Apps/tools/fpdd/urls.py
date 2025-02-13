from django.urls import path, include
from Apps.tools.fpdd import fpdd


urlpatterns = [
    # Дашбоард системы 
    path('', fpdd.main),
    # Страница информации о списании
    path('<str:id>/', fpdd.docPanel),
    
]
