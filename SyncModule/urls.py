from django.contrib import admin
from django.urls import path, include
from SyncModule.sync import InitSync, receive_file

urlpatterns = [
    path('syncInit/', InitSync),
    path('file_acceptance/', receive_file)
    ]
