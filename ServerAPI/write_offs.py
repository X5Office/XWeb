import requests
from Lib.BO_Checks import server_avalible, sessionCheck
from Core.config import BO_Url
from Lib import BOm
from datetime import datetime


@server_avalible('write-offs-list')
@sessionCheck
def getList(request):
    url = f'{BO_Url()}/api/write-offs'
    response = requests.get(url, headers=BOm.getHeader(request.user))
    return response.json()


@server_avalible('write-offs-docinfo')
@sessionCheck
def offsData(request, docId):
    url = f'{BO_Url()}/api/write-offs/{docId}'
    response = requests.get(url, headers=BOm.getHeader(request.user))
    return response.json()
    

@server_avalible('write-offs-positions')
@sessionCheck
def positions(request, docId):
    url = f'{BO_Url()}/api/write-offs/{docId}/positions'
    response = requests.get(url, headers=BOm.getHeader(request.user))
    return response.json()
