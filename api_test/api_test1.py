# class   People:
#
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def sum(self):
#         print("两个数之和为："+str(self.a+self.b))
#     def sub(self):
#         print("两个数之差为："+str(self.a-self.b))
#
# result=People(3,1)
# result.sum()
# result.sub()

#冒泡排序原理: 每一趟只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位, 也就是说要进行n-1趟操作(已经归位的数不用再比较)
import logging
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
logging.info("xxx")

def maopaopaixu(numb):
    for i in range(0,len(numb)-1):#循环6次
        for j in range(0,len(numb)-i-1):#比较次数
            if numb[j] < numb[j+1]:
                numb[j], numb[j+1] = numb[j+1], numb[j]
    return numb

numb= [1,2,3,2,1,6,5]

print( maopaopaixu(numb))


#选择排序法,将基准球和余下的球进行一一比较，如果比基准球小，则进行交换

def xuanzepaixu(numb):
    for b in range(0,len(numb)-1):
        smallest=b
        for c  in  range(b+1,len(numb)):
            if numb[c]<numb[smallest]:
                tmp=numb[c]
                numb[c]=numb[smallest]
                numb[smallest]=tmp
    return numb



numb= [1,2,3,2,1,6,5]
print(xuanzepaixu(numb))

#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。


def sum_recu(n):
    '''
    1 to n,The sum function
    '''
    if n > 0:
        return n + sum_recu(n - 1)
    else:

         return 0
print("递归求和：",sum_recu(100))

# import unittest
# from ddt import ddt, data, unpack
#
# c = 5
#
# list=[{"a":"1"},{"2":'c'},{"3":"d"}]
# @ddt
# class MyTestCase1(unittest.TestCase):
#     @data(*list)
#     def test_no3rmal(self,value):
#         print(value)
#
#
# if __name__ == '__main__':
#     unittest.main()
#
a=set ()
#a.add({"age":"1111"})
a.update({"age":"xxx","name":"oooo"})
print(a)
