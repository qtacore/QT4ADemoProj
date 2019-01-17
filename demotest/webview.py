# -*- coding: utf-8 -*-

'''示例Web自动化测试用例
'''

from demolib.demotestbase import DemoTestBase
from demolib.demoapp import DemoApp
from demolib.main import DemoWebPage, DemoWebPanel, HomePanel

class WebViewTest(DemoTestBase):
    '''示例Web自动化测试用例
    '''
    owner = "Administrator"
    timeout = 5
    priority = DemoTestBase.EnumPriority.High
    status = DemoTestBase.EnumStatus.Ready
    
    def run_test(self):
        #--------------------------
        self.start_step('1、登录Android demo,进入网页视图')
        #--------------------------
        acc = "admin"
        pwd = "admin"
        device = self.acquire_device()
        app = DemoApp(device)
        app.login(acc, pwd)
        self.log_info("登录完成")
        home_panel = HomePanel(app)
        home_panel.Controls["进入网页视图"].click()
        
        #--------------------------
        self.start_step('2、检查网页标题')
        #--------------------------
        demo_webpanel = DemoWebPanel(app)
        demo_webpage = DemoWebPage(demo_webpanel.Controls["webview"])
        self.assert_equal("标题应该是WebView Demo", demo_webpage.control("标题").inner_text , "WebView Demo")
      
        #--------------------------
        self.start_step('3、点击链接，检查页面已跳转')
        #--------------------------
        demo_webpage.control("qt4a_source_code").click()
        self.wait_for_equal('页面发生跳转，url变为https://github.com/Tencent/QT4A', demo_webpage, 'url', 'https://github.com/Tencent/QT4A')

if __name__ == '__main__':
    WebViewTest().debug_run()

