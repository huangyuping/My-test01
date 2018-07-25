import DoExcel
import my_Request
import unittest
doexcel = DoExcel.DoExcel.Excel('api_test')
#print(doexcel)
req = my_Request.Req
class api_Test(unittest.TestCase):
    def demo(self,doexcel):
        for i in range(0,len(doexcel)):
            dict_all=doexcel[i]
            print(dict_all)
            url=dict_all["url"]
            request_data=dict_all["request_data"]
            method=dict_all["method"]
            expected_data=dict_all["expected_data"]
            print(url)
            print(request_data)
            print(method)
            print(type(expected_data))
            res_test=req.muRequest(url,request_data,method)
            print(type(res_test.text))
            return res_test

        try:
            self.assertIn(expected,res_data)
            print("结果比对成功，通过测试")

        except AssertionError:
            raise AssertionError
            print("结果比对失败")




a=api_Test.demo(doexcel)

