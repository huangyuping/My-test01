# coding=utf-8
import unittest
from jmappium.driver import jcgn


class TestNotlogin(unittest.TestCase):

    def setUp(self):
        jcgn.get_ready(self)

    def test_not_loggin(self):
        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()




