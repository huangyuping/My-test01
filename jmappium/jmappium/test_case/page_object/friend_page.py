from test_case.page_object.login_page import *
from base_page import *
from test_case.model import myunit

import unittest

class FriendListPage(myunit.StartEnd,Page,LoginPage):

    # 我的主页
    home_profile_icon_loc = (By.ID,'home_profile_icon')
    # 好友按钮
    my_friend_layout_loc = (By.ID,'my_friend_layout')
    # 个签
    user_personal_signal_loc = (By.ID,'user_personal_signal')
    # 搜索
    search_loc = (By.ID,'search_loc')
    # 添加好友
    new_friends_loc = (By.ID,'new_friends')
    # 关注者
    follower_layout_loc =(By.ID,'follower_layout')
    # 特别好友
    special_friend_layout_loc =(By.ID,'special_friend_layout')
    # 返回按钮
    actionbar_transparent_back_loc = (By.ID,'actionbar_transparent_back')


    # 点击我的tab
    def type_home_profile_icon(self):
        self.find_element(*self.home_profile_icon_loc).click()
    # 点击【好友】按钮
    def type_frined_layout(self):
        self.find_element(*self.my_friend_layout_loc).click()

    # 获取个签内容
    def get_motto_text(self):
        self.find_element(*self.user_personal_signal_loc).text

    def type_search(self):
        self.find_element(*self.search_loc).click()

    def type_new_friends(self):
        self.find_element(*self.new_friends_loc).click()

    def type_follower_layout(self):
        self.find_element(*self.follower_layout_loc).click()

    def type_special_friend_layout(self):
        self.find_element(*self.special_friend_layout_loc).click()

    def type_actionbar_transparent_back(self):
        self.find_element(*self.actionbar_transparent_back_loc).click()

    # 进入好友列表页面
    def friend_list_action(self):
        self.type_home_profile_icon()
        self.type_frined_layout()

#class AddFriendPage(Page):


