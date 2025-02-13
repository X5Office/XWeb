import requests
from Lib import BOm
from Core.config import BO_Url

def login(request):
    url = f'{BO_Url()}/api/login'
    
    response = requests.get(url, headers=BOm.getHeader(request.user, True))
        
    if response.status_code == 200:
        return response.json()
    else:
     #   Log.register(f'При запросе к "{url}" произошла ошибка с кодом {response.status_code}')
        pass