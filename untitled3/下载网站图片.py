import urllib.request
import requests
import urllib.request
import re
#打开网页
url = "http://616pic.com/png/?sem=7&sem_kid=27&ks=4941"
#url = "https://www.baidu.com"


#获取网页信息
html1=requests.get(url).text

#正则匹配
image=re.findall('<img class="lazy" data-original="(.*)">',html1)
name=re.findall('<a href=".*.html" target="_blank" class=\'btitle\'>(.*)</a>',html1)
#print(type(image))
#print(name)
print(len(image))
print(len(name))
for j in  range(len(image)):
    try:
        urllib.request.urlretrieve(image[j],'/Users/xiaolongxia/Documents/image/%s.jpg'%name[j])
        print("正在下载：{}张".format(j))
    except:
        print("重新下载中...")
        urllib.request.urlcleanup()
        urllib.request.urlretrieve(image[j],'/Users/xiaolongxia/Documents/image/%s.jpg'%name[j])


#html = urllib.request.urlopen(url).read()
#print(html)
#res=html1.text
#print(html1)

#取出网页中的图片名字和url


#下载图片并且保存到本地文件夹
#findname = "/Users/xiaolongxia/Documents/image/1.jpg"
#image="http://pic.616pic.com/ys_img/00/68/24/cLyMHI7CyE.jpg"
#urllib.request.urlretrieve(image,findname)






#筛选出需要的信息

#保存到对应的到地方