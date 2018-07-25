import request_url
import re
#获取页面内容
html=request_url.open_url("http://www.hydcd.com/cy/chengyugushi.htm")
html.encoding="gb2312"
html1=html.text
#print(html1)
#获取成语链接地址
matching_all = request_url.matching_all('width=.*href="(.*.htm)">(.*?)</a></',html1)
#print(matching_all)
urlname_all=[]
for i  in  range(len(matching_all)):
    urlname = matching_all[i]
    urlname="http://www.hydcd.com/cy/"+urlname[0]
    urlname_all.append(urlname)
print(urlname_all)

# gshtml = request_url.open_url(urlname_all[82])
# gshtml.encoding="gb2312"
# gshtml=gshtml.text
# print(gshtml)
# story_content = re.findall('<font color="#10102C".*">([\s\S]+?)</font><br>', gshtml)
# story_content = story_content[0]
list_all = []
for j in range(0,len(urlname_all)-1):
    gshtml = request_url.open_url(urlname_all[j])
    gshtml.encoding="gb2312"
    gshtml=gshtml.text
    idiom_name=re.findall('【成语】：(.*)\r',gshtml)
    #idiom_name=idiom_name[0]
    idiom_pinyin=re.findall('【拼音】：(.*)\r',gshtml)
    #idiom_pinyin=idiom_pinyin[0]
    idiom_explain=re.findall('【解释】：(.*)\r',gshtml)
    #idiom_explain=idiom_explain[0]
    story_content=re.findall('<font color="#10102C".*">([\s\S]+?)</font><br>',gshtml)
    #story_content=story_content[0]
    dict_all = {}

    dict_all["成语"] = idiom_name[0]
    dict_all["拼音"] = idiom_pinyin[0]
    dict_all["解释"] = idiom_explain[0]
    dict_all["故事内容"] = story_content[0]

    list_all.append(dict_all)
    print("正在访问第{}个。。。。。。。".format(j))
#story_content=story_content.replace('\r','').replace('\n','')

print(list_all)
#for j in range(len(urlname_all)):
#    gshtml = request_url.open_url(urlname_all[j])

# lsit_d_all=[]
# for i in  range(len(matching_all)):
#     dir_all=[]
#     url_name=matching_all[i]
#     url_name=list(url_name)
#     #dir_all['url']=url_name[0]
#     #dir_all['name']=url_name[1]
#     lsit_d_all.append(url_name)
# print(lsit_d_all)


    #print(type(str(url_name)))
    #url_list,name_list=str(url_name).split(",")

    #print(url_list)
    #print(name_list)