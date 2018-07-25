i = 0
while i < 5:
    i=i+1
    if i==3:
        break
    print("输入的内容为："+str(i))


     #
    ###
   #####
  #######
 #########
    #
    #

# 4空格  1#
# 3空格  3#
# 2空格  5#
# 1空格  7#

height = input("树的高度为：")
height = int(height)
# 空格的个数
spaces = height-1
g=height-1
# #号的个数
hashes = 1

for j in range(height):
    for i in range(spaces):
        print(" ",end="")
    for i in range(hashes):
        print("#",end="")
    print()
    spaces -=1
    hashes+=2
    height-=1
for i in  range(g):
    print(" ",end="")
print("#")



