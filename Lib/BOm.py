def getHeader(user, logined=False):
    if logined:
        header = {
           "No-Authentication" : 'True',
           "Authorization" : f'Basic {user.backoffice_login}'
        }
    else:
        header = {
                "Authorization": f"Bearer {user.bearer_token}"
            }
    
    return header


class LI_positionsListBulder:
    def __init__(self):
        self.list = json.loads('[]')
    def add(self, plu, count):
        for items in self.list:
            if items['article'] == plu:
                pass
            else:
                item = {
                    "article" : plu,
                    "countedQuantity" : count
                        }
                self.list.append(item)
