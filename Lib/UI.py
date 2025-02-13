import json
from django import shortcuts

def redirect(*args, **kwargs):
    return shortcuts.redirect(*args, **kwargs)
    
    
def render(request, page_config, template_name, context={}, accept_level = 'user'):
    #accept_level = user | all | guest
    context['page'] = page_config.build()
    
    if accept_level == 'user':
        if request.user.is_authenticated:
            return shortcuts.render(request, template_name, context)
        else:
            return redirect('/GK/session/login/')
    elif accept_level == 'all':
        return shortcuts.render(request, template_name, context)
    elif accept_level == 'guest':
        if request.user.is_authenticated:
            return redirect('/GK/')
        else:
            return shortcuts.render(request, template_name, context)
    else:
        # Логгировать ошибку ядра
        pass
    
    

class Page:
    def __init__(self, title, header_text_main, header_text_after = ''):
        self.title = title
        self.header = {
            'main': header_text_main,
            'after': header_text_after
        }
        self.return_enable = False
        self.custom_menu = False
        
    
    def returnUrl(self, url):
        self.return_enable = True
        self.return_url = url
    
    def customMenuInit(self):
        self.custom_menu = True
    
    def build(self):
        page = {
            'title': self.title,
            'header': self.header
        }
        if self.return_enable is True:
            page['return_url'] = self.return_url
        if self.custom_menu is False:
            page['menu'] = [
                {
                    'url' : '/GK/',
                    'icon': 'home'
                },
                {
                    'url': '/GK/menu/turnover',
                    'icon': 'grid'
                },
                {
                    'url' : '/GK/menu/tools/',
                    'icon': 'settings'
                },
                {
                    'url' : '/GK/menu/delivery/',
                    'icon': 'delivery'
                },
                {
                    'url': '/GK/menu/profile/',
                    'icon': 'profile'
                }
            ]
            
        return page


class MasterMenu:
    def __init__(self):
        self.menu = json.loads('[]')
    
    def add(self, name, link = '', icon = '', badge = ''):
        
        item = {
            'name' : name,
            'link': link,
            'icon': icon,
            'badge': badge
        }
        self.menu.append(item)
    
    def build(self):
        return self.menu