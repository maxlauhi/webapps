#!/usr/bin/python
#coding:utf-8

# 导入MySQL驱动：
import mysql.connector

# 建立与数据库的连接：
conn = mysql.connector.connect(user='root', password='B@1utiful',database='test', use_unicode=True)
cursor = conn.cursor()

# 可以通过cursor.execute插入SQL命令来创建表和插入数据，注意commit提交事务和关闭连接。

#查询数据：%s是占位符号
cursor.execute('select * from user where id = %s', ('1',))

# .fetchall()获取多条数据，接受全部的返回结果行。
values = cursor.fetchall()

cursor.close()
conn.close()

# 可以写成一个可以调用来连接mysql的模块。
if __name__ == '__main__':
	print values