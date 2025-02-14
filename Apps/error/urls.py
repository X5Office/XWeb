from django.urls import path, include
from Apps.error import component
urlpatterns = [
    # Ошибка об отсувствии компонента
    path('component_not_found/', component.component_not_worked),

]