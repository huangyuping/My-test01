from time import sleep

class Page():
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 5

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_element_by_id(self,loc):
        return self.driver.find_element_by_id(loc)


    def find_element_by_class_name(self,loc):
        return self.driver.find_element_by_class_name(loc)

    def find_element_by_xpath(self,loc):
        return self.driver.find_element_by_xpath(loc)

    def find_element_by_android_uiautomator(self,loc):
        return  self.driver.find_element_by_android_uiautomator(loc)

    def assertIsTrue(self, value):
        self.assertTrue(value, True)

    def assertIsFalse(self, value):
        self.assertIs(value, False)

    def is_selected(self):
        return self.is_selected()
    #向左滑动的函数
    def swipe_left(self, duration):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 9 / 10, y / 2, x / 10, y / 2, duration)

    # 向上滑动函数
    def swipe_up(self, duration):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 2, y * 9 / 10, x / 2, y * 6 / 10, duration)

    # 向右滑动函数
    def swipe_right(self, duration):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 10, y / 2, x * 9 / 10, y / 2, duration)

    # 向下滑动函数
    def swipe_down(self, duration):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 2, y * 6 / 10, x / 2, y * 9 / 10, duration)

    # 当元素找不到时
    # def find_element1(self, element):
    #     self.exception = selenium.common.exceptions.NoSuchElementException
    #     try:
    #         WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, element)))
    #         return True
    #     except selenium.common.exceptions.TimeoutException:
    #         return False
    #     except self.exception:
    #         return False

    # 向上滑动列表查找元素并点击（by id）
    def swipe_up_find_element_id(self, element='加引号', keyword='加引号'):
        x = 1
        while x == 1:
            ymys = self.driver.page_source
            if keyword in ymys:
                self.driver.find_element_by_id(element).click()
                x = 2
            else:
                self.swipe_up(500)

    # 向上滑动列表查找元素并点击（by text）
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
