from django.urls import path, include



urlpatterns = [
    # Фиктивная проводка документов доставки
    path('fpdd/', include('Apps.tools.fpdd.urls')),
]
