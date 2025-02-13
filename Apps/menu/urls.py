from django.urls import path
from Apps.menu import menu


urlpatterns = [
    # Товарооборот
    path('turnover/', menu.turnover),
    # Инструменты
    path('tools/', menu.tools),
    # Доставка
    path('delivery/', menu.delivery),
    # Профиль/настройки
    path('profile/', menu.profile),
]
