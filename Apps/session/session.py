from Lib.UI import render, Page, redirect
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        login_s = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=login_s, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            page = Page('Авторизация WGK', '')
        return render(request, page, 'session/login.html', accept_level='guest')
    else:
        page = Page('Авторизация WGK', '')
        return render(request, page, 'session/login.html', accept_level='guest')