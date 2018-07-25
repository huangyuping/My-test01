import unittest
from driver.driver import mobile


class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = mobile()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    StartEnd()