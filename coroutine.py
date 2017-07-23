#!/usr/bin/python
#coding:utf-8

'''生产一个跳到消费者手上，给消费者消费，
消费完后把消息告诉生产者，生产者接收到消费者消费完的消息，打印出来后继续生产
问题：要把生产者生产和消费者消费两个子程序放在一个线程里，用协程的方式执行。
'''

import time

# 消费者
def consumer():
	r = ''
	while True:
		n = yield r
		# 如果N=0就代表没有生产，也就没有消费返回空值就可以
		if not n:
			return
		# 打印正在消费第几个的消息
		print ('[CONSUMER] Consuming %s...' % n)
		# 要1s的时间来消费, 并保存消费完成的消息
		time.sleep(1)
		r = '200 OK'

# 生产者
def produce(c):
    c.next()
    n = 0
    while n < 5:
		n = n + 1 # 生产下一个
		print ('[PRODUCER] Producing %s...' % n)
		# 把生产完第几个的消息告诉消费者，并接收消费情况
		r = c.send(n)
		# 接收销售情况的消息，并打印出来
		print ('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
	c = consumer()
	produce(c)