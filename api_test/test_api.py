import DoExcel
import my_Request
import unittest
import ddt
import re
import logging


de=DoExcel.DoExcel('/Users/xiaolongxia/PycharmProjects/api_test/text.xlsx')
doexcel=de.Excel_api_test()
#设置空字典表
global_vars={}

@ddt.ddt
class Test_Api(unittest.TestCase):
    #修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    @classmethod
    def setUp(self):
        de.modify_phone()
        de.save_excelFile()
    def tearDown(self):
        pass


    @ddt.data(*doexcel)
    def test_api(self,case_data):
        logging.info("开始执行")
        global global_vars  #设置全局变量
        #动态替换，判断请求参数中是否有需要替换全局变量的值
        if len(global_vars) > 0 and case_data['request_data'] is not None:
            for key,value in global_vars.items():
                if case_data['request_data'].find(key)!=-1:
                    case_data['request_data']=case_data['request_data'].replace(key,value)

#Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
#Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
#Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

        res=my_Request.Req.muRequest(case_data['url'],case_data['request_data'],case_data['method'])
        print("。。。。。。。。。。。")

        #正则匹配响应结果的值，放置在全局变量中
        if 'related_exp' in case_data.keys():
            temp=case_data['related_exp'].split("=")
            tem=re.findall(temp[1],res.text)
            print("提取的p为："+str(tem))
            #print(temp[0])
            #print(tem[0])
            global_vars[temp[0]]=tem[0]
            #print(global_vars)
#Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
#正则 re.findall  的简单用法（返回string中所有与pattern相匹配的全部字串，返回形式为数组）,findall(pattern, string, flags=0)




        #响应断言
        try:
            self.assertIn(case_data['expected_data'],res.text)
            print("匹配成功")
        except AssertionError:
            print("匹配失败")
            raise  AssertionError


#__name__ 只当前py文件调用方式的方法
if __name__ == '__main__':
    unittest.main()


