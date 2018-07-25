from appium.webdriver.common.mobileby import *
from test_case.page_object.base_page import *
import time


class LoginPage(Page):
    # 类的属性
    to_login_loc = (By.ID, "to_login")
    input_phone_number_loc = (By.ID, "input_phone_number")
    ok_loc = (By.ID, "ok")
    input_code_loc = (By.ID, "input_code")

    # 类方法
    def type_to_login(self):
        self.find_element(*self.to_login_loc).click()

    def type_input_phone_number(self, phone):
        self.find_element(*self.input_phone_number_loc).clear()
        self.find_element(*self.input_phone_number_loc).set_value(phone)

    def type_ok(self):
        self.find_element(*self.ok_loc).click()

    def type_code(self, code):
        self.find_element(*self.input_code_loc).click()
        self.find_element(*self.input_code_loc).set_value(code)

    def login_action(self, phone, code):
        time.sleep(5)
        self.type_to_login()
        time.sleep(3)
        self.type_input_phone_number(phone)
        self.type_ok()
        self.type_code(code)
        self.type_ok()
        time.sleep(3)
        self.type_ok()
        time.sleep(3)
