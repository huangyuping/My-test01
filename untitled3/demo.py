
#美元兑换人民币
dollar = input("请输入美元：")
dollar = int(dollar)
cny=dollar*6.74
print("{}美元可以兑换{}人民币".format(dollar,cny))


var=[]
#split()函数分开一个字符串 以空格为区分分割字符串
num1,num2 = input("输入两个数字：").split( )
num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
difference= num1 - num2
profuct = num1 * num2
quotient = num1 / num2
remainder = num1 % num2

print("{}+{}={}".format(num1,num2,sum))
print("{}-{}={}".format(num1,num2,difference))
print("{}*{}={}".format(num1,num2,profuct))
print("{}/{}={}".format(num1,num2,quotient))
print("{}%{}={}".format(num1,num2,remainder))


#if语句
name = "alice "

if name =="alice":
    print("hello alice")
print("sorry")