import unittest
from jmappium.runner.BSTestRunner import BSTestRunner
import time

test_dir = '../test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    report_dir='../test_report'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+'/'+now+'result.html'

    with open(report_name,'wb') as f:
        runner = BSTestRunner(stream=f,title="自动化测试报告",description="本测试报告为芥末校园项目的测试报告，目的在于遍历系统主流程的功能测试，描述系统是否符合需求。")
        runner.run(discover)
    f.close()