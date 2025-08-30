# https://www.xiaohongshu.com/user/profile/5ad2ede14eacab146f865fe9

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 小红书
# Desc      : 未登录状态下小红书个人简介页会返回最新的32条笔记,因此只存储这32条内容,若有新笔记加入则会触发判断

import requests, re

class xhsMonitor():
	def __init__(self, ):
		self.reqHeaders = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Referer': 'https://space.bilibili.com/3345720/video',
			'Connection': 'close',
			'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
		}
		self.xhsurl = 'https://www.xiaohongshu.com/user/profile/5ad2ede14eacab146f865fe9'
		self.dic = 'log/xiaohongshu.txt'
	# 日志为空时执行此函数,获取当前笔记标题
	def getXHSQueue(self):
		try:
			res = requests.get(self.xhsurl, headers=self.reqHeaders)
			content = re.findall('"displayTitle":"(.*?)"', res.text)
			with open(self.dic, 'a', encoding='utf-8') as f:
				for i in content:
					f.write(i +'\n')
			self.echoMsg('Info','笔记题目获取成功')
		except Exception as e:
			print(f"获取小红书队列失败: {e}")
	# 监控函数
	def startxhsmonitor(self):
		try:
			returnDict = {} #获取视频相关内容
			xhs = []
			with open(self.dic, 'r', encoding='utf-8') as f:
				for line in f.readlines():
					line = line.strip('\n')
					xhs.append(line)
			res = requests.get(self.xhsurl, headers=self.reqHeaders)
			content = re.findall('"displayTitle":"(.*?)"', res.text)
			# 只比较两个数组的内容是否有变化,而不关心顺序
			if set(content) != set(xhs):
				# 清空原内容,重新写入,防止后期内容太多不好比较
				with open(self.dic, 'w', encoding='utf-8') as f:
					for i in content:
						f.write(i + '\n')
				self.echoMsg('Info', '小红书更新啦!!!')
				returnDict['nickName'] = '狗子'
				return returnDict
		except Exception as e:
			print(f"监控小红书失败: {e}")
	# 格式化输出
	def echoMsg(self, level, msg):
		if level == 'Info':
			print('[Info] %s'%msg)
		elif level == 'Error':
			print('[Error] %s'%msg)

# def main():
# 	xhs = xhsMonitor()
# 	xhs.startxhsmonitor()
#
# if __name__ == '__main__':
# 	main()