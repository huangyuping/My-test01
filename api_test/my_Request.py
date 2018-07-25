import requests

class Req():

    def muRequest(url, request_data, method):
        #判断数据是否为空如果不为空则转换为字典
        if request_data is not None:
            request_data = eval(request_data)
        if method == 'get':
            res = requests.get(url, request_data,verify=False)
        if method == 'post':
            res = requests.post(url, request_data,verify=False)
        else:
            print("没填写url类型吧！~~")
        return res



