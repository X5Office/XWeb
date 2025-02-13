from Lib.UI import render, Page
from TelegramBot.models import TGUser


def users(request):

    tgusers = TGUser.objects.all()

    page = Page('Пользователи', 'Пользователи', 'База зарегестрированных пользователей TG бота')
    return render(request, page, 'delivery/users/list.html', {'users': tgusers})

def dm(request):

    page = Page('Пользователи', 'Пользователи', 'База зарегестрированных пользователей TG бота')
    return render(request, page, 'test.html')