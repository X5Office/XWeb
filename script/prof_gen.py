import os

def generate_config():
    # Запрашиваем у пользователя необходимые значения
    develop_server_connect = input("Ваш сервер запущен на тестовой среде? (True/False): ").strip().lower() == 'true'
    bo_url_suffix = input("Введите номер ТОРГ (SAP) BackOffice (например, 'JH34'): ").strip()
    fs_dir_suffix = input("Введите имя для директории хранения файлов загрузок (например, 'uploads'): ").strip()
    print('Формирование типа сервера')
    remote_adress_server = input("Введите адрес удаленного от вас сервера(НЕАКТУАЛЬНО)(10.0.0.1): ").strip()
    tg_token = input("Введите токен бота:").strip()
    # Создаем директорию для хранения файлов загрузок
    fs_dir_path = os.path.join(os.getcwd(), fs_dir_suffix)
    os.makedirs(fs_dir_path, exist_ok=True)

    # Формируем содержимое файла конфигурации
    config_content = f"""from WebGK.settings import BASE_DIR
# Настройки системы WebGK

# Режим локального тестового сервера
Develop_Server_Connect = {develop_server_connect}

# Ссылка на BackOffice
BO_Urls = 'http://bo-{bo_url_suffix}.x5.ru:8096'

# Дирректория для хранения файлов загрузок
FS_DIR = BASE_DIR / '{fs_dir_suffix}'

# Дирректория для хранения файлов DBSync
DBSync = BASE_DIR / 'dbwsync'

# Дирректория для хранения файлов DBSync
DBSyncCollect = BASE_DIR / 'dbwsync' / 'collect'

# Адрес (включая порт) сервера для выгрузки
REMOTE_ADDRES_SERVER = 'http://'+'{remote_adress_server}'

# Наименование рабочей сети WiFi
LAN_WIFI_SSID = 'Dmitr.Sorokovykh'

# НАСТОЙКИ TELEGRAM БОТА

# Токен
TELEGRAM_BOT_TOKEN = '{tg_token}'

#Шаблон DataMatrix
DATAMATRIX_template = '010+215%qlDivRD===R93Ho/N'

#ДАЛЕЕ НИЧЕГО НЕ МЕНЯЕМ!!!
# Обработчики настроек
def BO_Url():
    if Develop_Server_Connect:
        return 'http://127.0.0.1:8096'
    else:
        return BO_Urls

"""

    # Записываем содержимое в файл конфигурации
    with open('Core/config.py', 'w') as config_file:
        config_file.write(config_content)

    print("Файл конфигурации успешно создан.")
    print(f"Директория для хранения файлов загрузок успешно создана: {fs_dir_path}")

# Вызываем функцию для генерации конфигурации
generate_config()
