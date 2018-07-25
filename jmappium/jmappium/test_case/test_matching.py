import unittest
from test_case.model import myunit
from page_object.matching_page import *

class MatchingSetting(myunit.StartEnd):
    def test_matching_list(self):
        # 创建实例
        jmapp = MatchingSettingPage(self.driver)
        # 调用方法
        jmapp.login_action('18701692876', '1234')
        jmapp.matching_setting_action()
        #a=self.driver.find_element_by_id('com.jiemoapp:id/button3')
        #is_selected()这个是判断某个元素是否被选中
        #isDisplayed()这个函数用于判断某个元素是否存在页面上
        #isEnable()存储input、select等元素的可编辑状态，可以编辑返回true，否则返回false
        #b=a.is_selected()
        #self.assertEqual(b,'true')
        #self.assertTrue('err',a)


if __name__ == '__main__':
    unittest.main()
