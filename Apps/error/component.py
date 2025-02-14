from Lib.UI import render, Page


def component_not_worked(request):
    error_text = 'Данный компенент не доступен. Возможно он отключен или находится в разработке.'
    page = Page('Ошибка', 'Ошибка', 'Произошла предвиденная ошибка')
    page.returnUrl(request.META.get('HTTP_REFERER'))
    return render(request, page, 'error/template.html', {'error': error_text})