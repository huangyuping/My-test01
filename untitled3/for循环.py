#1+2+3+...100
num=0
for i in range(0,101):
    num+=i
print(num)

#1-20 取模

for i in range(0,21):
    if i % 2 !=0:
        print("所取得数为：{}".format(i))



#计算利息,输入价钱然后存10年，查看每年的利息及本金

lilu=input("请输入年利率")
lilu=float(lilu)
money=input("请输入存取金额")
money =float(money)#转换为浮点型
for i in range(1,11):
    money=money+money*lilu

    print("第{}年的利息和本金为{}".format(i,round(money,2)))