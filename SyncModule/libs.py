import json
import os
from datetime import datetime
from Core.config import DBSync
from SyncModule.models import ChangeLog


def generate_changes_file(FiteIter, applied_changes=[]):
    # Генерируем имя файла
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
    filename = f"{timestamp}.json"
    filepath = os.path.join(DBSync, filename)

    # Генерируем изменения
    changes = ChangeLog.objects.filter(synced=False)
    changes_data = list(changes.values('id', 'timestamp', 'app_label','model_name', 'record_id', 'change_type', 'new_state'))

    # Преобразуем объекты datetime в строки
    def datetime_handler(x):
        if isinstance(x, datetime):
            return x.isoformat()
        raise TypeError("Unknown type")

    # Добавляем блок info
    changes_json = json.dumps({
        "changes": changes_data,
        "info": {
            "type": FiteIter
        },
        "applied_changes": applied_changes
    }, indent=4, default=datetime_handler)

    # Сохраняем изменения в файл
    with open(filepath, 'w') as file:
        file.write(changes_json)

    return filepath

    
def ping_external_server():
    return True