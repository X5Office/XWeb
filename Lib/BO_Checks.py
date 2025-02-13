import json, requests#, termux
from WebGK.settings import BASE_DIR
from Core.config import BO_Url, LAN_WIFI_SSID
from Lib import BOm
from Core.models import User 
from ServerAPI import sessions
from datetime import datetime, timedelta

'''
def check_network(funct_name):
    def network_check(function):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt <=10:
                attempt += 1
                wifi = termux.API.generic(['termux-wifi-connectioninfo'])[1]
                if wifi != {}:
                    break
            if wifi == {'API_ERROR': 'Location needs to be enabled on the device'}:
                result = json.load(open(BASE_DIR/f'dev/respone_templates/{funct_name}.json')) 
            else: 
                lan_detected = False
                if wifi['ssid'] == LAN_WIFI_SSID:
                    lan_detected = True
                    
                if lan_detected:
                    result = function(*args, **kwargs)
                else:
                    result = json.load(open(BASE_DIR/f'dev/respone_templates/{funct_name}.json')) 
            return result
        return wrapper
    return network_check
    
'''

# НЕ ПОДДЕРЖИВАЕМЫЙ КОД(УДАЛИТСЯ СО СЛЕД РЕЛИЗОМ)
def server_avalible(funct_name):
    def server_avalible_checker(function):
        def wrapper(*args, **kwargs):
            try:
                 requests.get(f'{BO_Url()}/ping')
            except Exception:
                result = json.load(open(BASE_DIR/f'dev/respone_templates/{funct_name}.json'))
            else:
                result = function(*args, **kwargs)
            return result
        return wrapper
    return server_avalible_checker
    

def loginBO(request):
    account = User.objects.get(id=request.user.id)
    response = sessions.login(request)
    account.bearer_token = response['accessToken']['value']
    account.expirationDateTime = response['accessToken']['expirationDateTime']
    account.save()
    
# НЕ ПОДДЕРЖИВАЕМЫЙ КОД(УДАЛИТСЯ СО СЛЕД РЕЛИЗОМ)
def session_check(funct):
    def wrapper(request, *args, **kwargs):
        loginBO(request)
        result = funct(request, *args, **kwargs)
        return result
    return wrapper
    
    
def sessionCheck(funct):
    def wrapper(request, *args, **kwargs):
        
        currentDateTime = datetime.now()
        expirationDateTime = datetime.strptime(request.user.expirationDateTime, '%d.%m.%Y %H:%M:%S')
        expirationDateTime -= timedelta(seconds=10)
        if currentDateTime > expirationDateTime:
            loginBO(request)
        result = funct(request, *args, **kwargs)
        return result
    return wrapper
    
