import unittest
from test_case.model import myunit
from page_object.friend_page import *


class FriendList(myunit.StartEnd):
    def test_flip_friend_list(self):
        # 创建实例
        jmapp = FriendListPage(self.driver)
        # 调用方法
        jmapp.login_action('17610086125', '1234')
        jmapp.friend_list_action()
        jmapp.swipe_up_find_element_text('周小猴子')

        t1 = self.driver.find_element_by_id("user_personal_signal").text
        print(t1)
        self.assertEqual(t1, '自动化测试专用签名')


if __name__ == '__main__':
    unittest.main()
