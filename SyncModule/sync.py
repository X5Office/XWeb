from Lib.UI import redirect
from SyncModule.tasks import InitSyncProcedure, AcceptanceOfChanges
import os
from Core.config import DBSyncCollect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def InitSync(request):
    InitSyncProcedure.delay()
    return redirect('/')


@csrf_exempt
def receive_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        filename = file.name
        filepath = os.path.join(DBSyncCollect, filename)

        # Сохраняем файл
        with open(filepath, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Запускаем Celery-задачу для обработки файла
        AcceptanceOfChanges.delay(filepath)

        return JsonResponse({"message": "Файл успешно получен и сохранен", "status": "success"})
    else:
        return JsonResponse({"message": "Метод не поддерживается", "status": "error"})
