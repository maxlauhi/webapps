#!/usr/bin/python
#coding:utf-8

# 导入sqlalchemy模块的相关类:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''
	初始化DBSession和具体每个表的class定义
'''
# 创建对象的基类：
Base = declarative_base()

# 定义User对象：
class User(Base):
	# 表的名字：
	__tablename__ = 'user'

	# 表的结构：
	id = Column(String(20), primary_key=True)
	name = Column(String(20))

# 初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://root:B@1utiful@localhost:3306/test')

# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)


'''
	ORM后向数据库添加记录就相当与添加一个User对象
'''

# 创建session对象：
session = DBSession()
# 创建新User对象：
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库：
session.commit()
# 关闭session:
session.close()