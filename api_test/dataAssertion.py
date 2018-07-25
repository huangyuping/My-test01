import unittest
class Ass(unittest.TestCase):

    def test_one(self):
        a = 111
        b = 111
        try:
            self.assertIn(a,b)
            print("dui")
        except AssertionError:
            raise AssertionError

            print("c")

#  @classmethod

#     def ass(self,expected,res_data):
#         try:
#             self.assertIn(expected,res_data)
#             print("结果比对成功，通过测试")
#
#         except AssertionError:
#             raise AssertionError
#             print("结果比对失败")
#
#
# Ass.ass("sss","fff")