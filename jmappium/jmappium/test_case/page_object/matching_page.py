from test_case.page_object.login_page import *

from base_page import *
class MatchingSettingPage(Page,LoginPage):

#兴趣相投设置里边的属性

    #兴趣相投icon
    home_rss_icon_loc=(By.ID,'home_rss_icon')
    #筛选按钮
    筛选_loc=('new UiSelector().text("筛选")')
    #只看女生
    button1_loc=(By.ID,'button1')
    # 只看男生
    button2_loc = (By.ID, 'button2')
    # 查看全部
    button3_loc = (By.ID, 'button3')
    #x按钮
    close_loc=(By.ID,'close')


#测试数据
    write_state_loc=(By.ID,'write_state')
    edit_loc=(By.ID,'edit')
    actionbar_compose_loc=(By.ID,'actionbar_compose')


#兴趣相投设置里边的方法
    #点击兴趣相投tab

    # def type_write_state_loc(self):
    #     self.find_element(*self.write_state_loc).click()
    # def type_edit_loc(self):
    #     a=self.find_element(*self.edit_loc)
    #     a.click()
    #     a.set_value("123")
    # def type_actionbar_compose(self):
    #     self.find_element(*self.actionbar_compose_loc).click()
    #def type(self,type1):
       # self.find_element(type)

    def type_home_rss_icon(self):
        self.find_element(*self.home_rss_icon_loc).click()
    #点击筛选按钮
    def type_筛选(self):
        self.find_element_by_android_uiautomator(self.筛选_loc).click()
    #点击只看女生
    def type_button1(self):
        a=self.find_element(*self.button1_loc)
        a.click()
    #点击只看男生
    def type_button2(self):
        self.find_element(*self.button2_loc).click()
    #点击查看全部
    def type_button3(self):
        self.find_element(*self.button3_loc).click()
    #点击x按钮
    def type_close(self):
        self.find_element(*self.close_loc).click()
    #调用
    def matching_setting_action(self):
        self.type_home_rss_icon()
        self.type_筛选()
        self.type_button1()
        self.assertIsTrue(self.find_element(*self.button1_loc).is_selected())
        self.type_button2()
        self.type_button3()
        self.type_close()


def swipe_up_find_element_text(self, keyword='加引号'):
    x = 1
    while x == 1:
        ymys = self.driver.page_source
        if keyword in ymys:
            sleep(2)
            want = self.driver.find_element_by_android_uiautomator('new UiSelector().text("周小猴子")')
            want.click()
            x = 2
        else:
            self.swipe_up(500)


#兴趣相关里边的属性方法及调用
class MatchingInterestPage(Page,LoginPage):
    #兴趣按钮
    兴趣_loc = (By.ID, 'button2')
    #兴趣页面x按钮
    close_loc=(By.ID,'close')



#超级喜欢部分

#兴趣展示页
    #超级喜欢搜索框
    search_super_like_loc=(By.ID,'search_super_like')

    #超级喜欢编辑按钮
    edit_super_like_loc=(By.ID,'edit_super_like')

    #超级喜欢编辑按钮整个显示框分为123
    super_edit_loc=('android.widget.LinearLayout')

    #超级喜欢点击添加超级喜欢文案处
    like_interest_loc=('new UiSelector().text("点击添加超级喜欢")')

    #超级喜欢引导按钮
    super_like_guide=('com.jiemoapp:id/super_like_guide')

    #超级喜欢引导提示'我知道了'
    i_know=('com.jiemoapp:id/i_know')

#超级喜欢编辑页面

    #超级喜欢编辑页面删除按钮
    click_remove=('com.jiemoapp: id / click_remove')

    #超级喜欢编辑页面排序按钮
    drag_handle=('com.jiemoapp: id / drag_handle')

    #超级喜欢编辑页面返回按钮
    actionbar_transparent_back=('com.jiemoapp: id / actionbar_transparent_back')

    #超级喜欢编辑页面删除提示框取消
    parentPanel_loc=('new UiSelector().text("取消")')

    # 超级喜欢编辑页面删除提示框删除
    parentPanel1_loc = ('new UiSelector().text("删除")')

#超级喜欢添加及搜索

    #点击搜索输入框
    search=('com.jiemoapp:id/search')

    #超级喜欢搜索结果页
    super_search_list=('android:id/list')

    #超级喜欢搜索结果页列表框(单独的一个选择框)
    super_search_list_relativelayout=('android.widget.RelativeLayout')

    #超级喜欢搜索结果页头像
    intrest_pic=('com.jiemoapp: id / intrest_pic')

    #超级喜欢搜索结果页显示区域
    layout_loc=('com.jiemoapp: id / layout')

    #超级喜欢搜索结果页添加按钮
    add_intrest_text=('com.jiemoapp: id / add_intrest_text')

    #编辑超级喜欢页面取消按钮
    actionbar_compose=('com.jiemoapp: id / actionbar_compose')

    #编辑超级喜欢页面完成按钮
    actionbar_btn_text=('com.jiemoapp: id / actionbar_btn_text')

    #编辑超级喜欢页面完成后点击提示框中我再想想
    actionbar_ninterest_loc=('new UiSelector().text("我再想想")')

    # 编辑超级喜欢页面完成后点击提示框中确认添加
    actionbar_interest_loc = ('new UiSelector().text("确认添加")')


    #编辑超级喜欢页面描述框
    super_like_interest_desc=('com.jiemoapp: id / super_like_interest_desc')

    #编辑超级喜欢页面兴趣名称处
    super_like_interest_name=('com.jiemoapp: id / super_like_interest_name')

#兴趣列表页
    #兴趣列表页添加按钮
    add_interest_tv=('com.jiemoapp: id / add_interest_tv')

    #兴趣列表页返回按钮
    actionbar_transparent_back=('com.jiemoapp: id / actionbar_transparent_back')

    #兴趣列表页title
    actionbar_transparent_title=('com.jiemoapp: id / actionbar_transparent_title')

    #兴趣列表页点击超级喜欢
    button1=('com.jiemoapp: id / button1')

    #兴趣列表页点击普通兴趣
    button2=('com.jiemoapp: id / button2')








    def type_home_rss_icon(self):
        self.find_element(*self.home_rss_icon_loc).click()
    def type_兴趣_loc(self):
        self.find_element(*self.兴趣_loc).click()
    def typ_ead_loc(self):
        self.find_element(*self.ead_loc).click
    def matchint_interest_action(self):
        self.type_home_rss_icon()
        self.type_兴趣_loc()
        self.typ_ead_loc()

#普通兴趣部分
    # 普通兴趣搜索框
    search_more_interest_loc = (By.ID, 'search_more_interest')

    #普通兴趣编辑按钮
    edit_interest_loc=(By.ID,'edit_interest')

    #







