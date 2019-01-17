# -*- coding: utf-8 -*-

'''Android Demo App类
'''

from qt4a.androidapp import AndroidApp

class DemoApp(AndroidApp):
    '''安卓Demo App类
    '''
    # 包名,必须定义
    package_name = 'com.qta.qt4a.demo'
    
    def __init__(self, device=None, clear_state=True, kill_process=True, net_type='wifi', start_extra_params={}):
        '''
        :param device: 设备实例
        :type device:  Device
        '''
        super(DemoApp, self).__init__(self.package_name, device)  #第一个参数传入主进程名，在demo app中，主进程名和包名相同
        self._start(clear_state, kill_process, start_extra_params=start_extra_params)
        
    def _start(self, clear_state=True, kill_process=True, start_extra_params={}):
        '''启动Android demo apk
        '''
        if kill_process == True:
            self.device.kill_process(self.package_name)  # 杀死已有进程
        if clear_state == True:
            self.device.clear_data(self.package_name) #清除包数据
        self.device.adb.start_activity('%s/%s.MainActivity' % (self.package_name, self.package_name), extra=start_extra_params)  
            
    def login(self, acc, pwd):
        '''登录demo
        '''
        from login import LoginPanel
        login_panel = LoginPanel(self)
        login_panel.login(acc, pwd)
        