import DoExcel
import requests
import ddt
import  my_Request
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
import test_api
import time
#定义一个测试套件
s=unittest.TestSuite()
#将test_api 模块放在测试套件s上并运行
ul=unittest.TestLoader()
s.addTest(ul.loadTestsFromModule(test_api))

#拼接测试报告
now = time.strftime('%Y_%m_%d_%H_%M_%S')
html_report_path = '/Users/xiaolongxia/PycharmProjects/api_test/HtmlTestReport' + '/' + now + '.html'

# wb：以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
fp = open(html_report_path,'wb')
runner = HTMLTestRunner(fp,title='API 测试报告')
runner.run(s)



# exec = DoExcel.DoExcel.Excel('api_test')
# print(len(exec))
# for i in range(0,len(exec)):
#     dict=exec[i]
#
#     print(type(dict))
#     print("......")
# print(dict["url"])
# dicts=eval(dict["request_data"])
# print((dict["request_data"]))
# print("6666")
#
# print(str(exec[1])+"ccc")
# result = requests.post("https://api.jiemoapp.com/api/"+dict["api"], dicts, verify=False)
# print(result.url)
# print(result.text)



# result = requests.get(dict["api"],dict["canshu"],verify=False)
# print(result)

# api_test=api_test1.Req(dict["api"],dict["canshu"])
# print(api_test1)
# print(api_test.post())
