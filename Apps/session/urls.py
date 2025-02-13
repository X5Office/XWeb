from django.urls import path, include
from Apps.session import session
urlpatterns = [
    # Информация о товаре
    path('login/', session.login),
    
]