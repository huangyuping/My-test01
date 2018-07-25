import requests
import urllib.request
url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=40'
#req=urllib.request.urlopen(url).read()
req=requests.get(url)
print(req.test)