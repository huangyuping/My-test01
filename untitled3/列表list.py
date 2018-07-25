mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#       -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(mylist[::2])#间隔一个读取一个
#运行结果为[0, 2, 4, 6, 8]

print(mylist[-1:2:-1])#起始位置，结束为止，正序/反序
#运行结果[9, 8, 7, 6, 5, 4, 3]

print("元素的索引是：",mylist.index(1))#index定位列表元素的位置
#运行结果为 1

mylist.append("haha")#添加元素
print(mylist)
#运行结果为：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'haha']


import random
rand_num =random.randrange(1,50)#1 - 50之间的随机数
print(rand_num)

list = [5,2,3,4,1,3,8]
print(len(list))

for i in  range(0,len(list)-1):#len(list)-1 是因为长度是以1开始计算，而列表的所以是以0开始计算
    for j in  range(0,len(list)-i-1):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
print(list)



a=["abd","ccc"]
print(str(a))
