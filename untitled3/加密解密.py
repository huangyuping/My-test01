a_list = ["a","b","c"]
#以，将字符串连接
print(",".join(a_list))
#    join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
#os.path.join()：  将多个路径组合后返回


# 提取列表中的字符串中的第一个字母
#用户输入字符串
# str = input("请输入一个字符串提取第一个字母：")
# #所有字符串转换为大写
# str = str.upper()
# #字符串进行分离放到一个list列表中
# str1 = str.split()
# #然后进行访问提取第一个字母
# for i in str1:
#     print(i[0])






#对大写字符串进行加密解密

# #输入一个字符串
# str_old = input("输入大写的字母：")
# str_new =""
# #循环读取字符串每一个字母
# for char in str_old:
#     #对字符进行加密,因为小写字母解密后，有可能为3位数，但是减去23后都会变为2位数，所以此时减去23，空格为32减去23为1位数需要特殊处理，
#     if char.isalpha():
#         str_new=str_new+str(ord(char)-23)
#     elif char.isspace():
#         str_new=str_new+str(ord(char))
#
# print(str_new)
#
# norm_string=""
# #循环读取字符串，因为大写字母是两个整数表示，所以此处一次性读取两个字符
# for i in range(0,len(str_new)-1, 2):
#     char_code=str_new[i]+str_new[i+1]
#     # 32为空格
#     if char_code != "32" :
#     #转换为字符
#         norm_string=norm_string+chr(int(char_code)+23)
#     else:
#         norm_string=norm_string+chr(int(char_code))
#
#
# print(norm_string)

class Person(object):  # 定义一个父类

    def talk(self):  # 父类中的方法
        print("person is talking....")


class Chinese(Person):  # 定义一个子类， 继承Person类

    def walk(self):  # 在子类中定义其自身的方法
        print('is walking...')

num=1
print(type(num))

c = Chinese()


#凯撒加密法

massage = input("输入个内容：")
key = input("输入偏移量-26 - 26")
key = int(key)
secret_massage=""
#变量字符
for  char in massage:
    if char.isalpha():#判断是不是字母
        char_code = ord(char)+key
        #判断是不是大写字母
        if char.isupper():
            if char_code > ord("Z"):
                char_code = char_code -26
            if char_code < ord("A"):
                char_code =char_code + 26
        #判断是不是小写字母
        if char.islower():
            if char_code > ord("z"):
                char_code-=26
            if char_code < ord("a"):
                char_code+=26

        secret_massage+=chr(char_code)
    else:
        secret_massage+=char

print("加密后的结果为：{}".format(secret_massage))