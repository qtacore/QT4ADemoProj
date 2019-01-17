# -*- coding: utf-8 -*-

from qt4a.andrcontrols import Window, Button, WebView
from qt4a.qpath import QPath
from qt4w.webcontrols import WebPage, WebElement
from qt4w import XPath

class HomePanel(Window):
    '''Home界面
    '''
    Activity = 'com.qta.qt4a.demo.HomeActivity'  # 主界面

    def __init__(self, demoapp):
        super(HomePanel, self).__init__(demoapp)
        self.update_locator({'进入网页视图': {'type': Button, 'root': self, 'locator': QPath('/Id="goToWebview"')},
                            })
        
class DemoWebPanel(Window):
    ''''Demo Web页面
    '''
    Activity = 'com.qta.qt4a.demo.WebViewActivity'
    Process = 'com.qta.qt4a.demo'  #此时Process不写也可以，因为跟主进程一致

    def __init__(self, demoapp):
        super(DemoWebPanel, self).__init__(demoapp)
        self.update_locator({'webview': {'type': WebView, 'root': self, 'locator': QPath('/Id="sampleWebView"')},
                            })
        
class DemoWebPage(WebPage):
    '''Demo Web页面
    '''    
    ui_map = {'标题': XPath('//h2'),
              'qt4a_source_code':{'type': WebElement,'locator': XPath('//div[@id="qt4a_code"]/a'),}
            #'qt4a_source_code':XPath('//div[@id="qt4a_code"]/a'), #如果type为WebElement也可直接简化为该写法，所以此时qt4a_source_code这么定义也可以
              }

