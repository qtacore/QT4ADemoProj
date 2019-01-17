# -*- coding: utf-8 -*-

from qt4a.andrcontrols import Window, Button, EditText
from qt4a.qpath import QPath

class LoginPanel(Window):
    '''登录界面
    '''
    Activity = 'com.qta.qt4a.demo.MainActivity'  # 登录界面

    def __init__(self, demoapp):
        super(LoginPanel, self).__init__(demoapp)
        self.update_locator({'帐号': {'type': EditText, 'root': self, 'locator': QPath('/Id="editAcc"')},
                            '密码': {'type': EditText, 'root': self, 'locator': QPath('/Id="editPwd"')},
                            '登录': {'type': Button, 'root': self, 'locator': QPath('/Id="btnLogin"')},
                      
                            })

    def login(self, acc, pwd):
        '''登录界面
        '''
        self.wait_for_exist()
        self.Controls["帐号"].text = acc
        self.Controls["密码"].text = pwd
        self.Controls["登录"].click()



