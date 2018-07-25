import pymysql
#打开数据库链接
db = pymysql.connect("localhost","root","123456","sqltest")

#使用cursor()方法获取操作游标
cursor=db.cursor()
#sql语句插入操作
sql="insert into story_book(id,story_name,pinyin,spell,content)" \
    "VALUES(5,'草船借箭','caochuanjiejian','haha','caozujj')"

#查询操作
cursor.execute(sql)
cursor.execute("select*from story_book")
db.commit()
data = cursor.fetchall()
print(data)
db.close()
