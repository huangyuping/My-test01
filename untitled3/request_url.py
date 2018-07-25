import requests
import re
def open_url(url):
    res=requests.get(url)
    return res


def matching_all(matching,url):
    matching_all = re.findall(matching,url)
    return matching_all