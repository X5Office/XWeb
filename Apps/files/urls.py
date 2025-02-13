from django.urls import path, include
from Apps.files import main
urlpatterns = [
    # База со списком всех файлов
    path('', main.board),
    # Добавление файла
    path('upload/', main.upload),
    # Скачивание сохранённого файла
    path('download/<str:filename>', main.download)
]