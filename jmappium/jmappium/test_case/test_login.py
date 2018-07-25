import unittest
from test_case.model import myunit
from test_case.page_object.login_page import *


class LoginTest(myunit.StartEnd):

    def test_login_normal(self):
        #创建实例
        jmapp = LoginPage(self.driver)
        #调用方法
        jmapp.login_action('17610086125', '1234')
        sleep(2)

        zdgdta = self.driver.find_element_by_id('com.jiemoapp:id/tab_chat')
        self.assertTrue(zdgdta.is_displayed())

if __name__ == '__main__':
    unittest.main()
