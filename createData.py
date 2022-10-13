# -*- coding = utf-8 -*-
# 2022/7/24 21:59
import pymysql

# 1.连接mysql
conn = pymysql.connect(host="192.168.1.108", port=3306, user="root", password="288cuiting", charset="utf8", db="unicom")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2.发送指令
# 千万不要用字符串格式化去做sql的拼接，会有安全隐患（sql注入）,应该使用execute自带的

# 插入
# sql = "insert into admin(username, password, mobile) values(%s, %s, %s)"
# cursor.execute(sql, ['cuitingting', '123456', '13403947036'])
# conn.commit()

# 查询
sql = "select * from admin"
cursor.execute(sql)
datalist = cursor.fetchall()
print(datalist)

# 3.关闭连接
cursor.close()
conn.close()