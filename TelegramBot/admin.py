from django.contrib import admin
from TelegramBot.models import TGUser, RequestDataMatrixLog

# Register your models here.
admin.site.register(TGUser)
admin.site.register(RequestDataMatrixLog)