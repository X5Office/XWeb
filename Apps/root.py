from Lib.UI import render, Page

def dashboard(request):
    page = Page('Дашбоард WGK', 'Дашбоард', 'Ваш рабочий стол')
    return render(request, page, 'root/dashboard.html')