from django.urls import path, include
from Apps.delivery import main

urlpatterns = [
    # База пользователей Telegarm бота
    path('users/', main.users),
    # База пользователей Telegarm бота
    path('dm/', main.dm),
]