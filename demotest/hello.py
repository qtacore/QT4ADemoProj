# -*- coding: utf-8 -*-

'''示例登录测试用例
'''

from demolib.demotestbase import DemoTestBase
from demolib.demoapp import DemoApp

class HelloTest(DemoTestBase):
    '''示例登录测试用例
    '''
    owner = "Administrator"
    timeout = 5
    priority = DemoTestBase.EnumPriority.High
    status = DemoTestBase.EnumStatus.Design
    
    def run_test(self):
        #--------------------------
        self.start_step('1、登录Android demo')
        #--------------------------
        acc = "admin"
        pwd = "admin"
        device = self.acquire_device()
        app = DemoApp(device)
        app.login(acc, pwd)
        self.waitForEqual('当前Activity为：com.qta.qt4a.demo.HomeActivity', app.device, 'current_activity', 'com.qta.qt4a.demo.HomeActivity')

    
if __name__ == '__main__':
    HelloTest().debug_run()

