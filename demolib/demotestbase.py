# -*- coding: utf-8 -*-
'''示例测试基类
'''

from qt4a.device import Device
from qt4a.androidtestbase import AndroidTestBase

class DemoTestBase(AndroidTestBase):
    '''demo测试用例基类
    '''

    def post_test(self):
        '''清理测试用例
        '''
        from qt4a.androiddriver.util import logger
        logger.info('post_test run')
        super(DemoTestBase, self).post_test()
        Device.release_all_device()  # 释放所有设备
        logger.info('postTest complete')
    
    def acquire_device(self, type='Android', device_id='', **kwds):
        '''申请设备
        
        :param type: 申请的设备类型，目前尚未使用
        :type type:  string
        :param device_id: 申请的设备ID，默认不指定设备ID
        :type device_id:  string
        '''
        device = super(DemoTestBase, self).acquire_device(device_id, **kwds)
        device.adb.start_logcat([])
        return device
