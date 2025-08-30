#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 抖音
# Desc      : 根据抖音个人信息页显示的视频数量判断是否更新(可能不准,因为删除视频也会引起数量变化)

import requests, re

class dyMonitor():
	def __init__(self):
		self.reqHeaders = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
			'Cookie': '__ac_nonce = 06744533e0057a462305f; __ac_signature = _02B4Z6wo00f01HAuWQQAAIDDItF5HF.JY8xwHl2AAHtX9e; __ac_referer = __ac_blank',
			'Accept': 'application/json',
			'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
			'Accept-Encoding': 'gzip, deflate',
			'X-Requested-With': 'XMLHttpRequest',
			'Referer': 'https: // www.douyin.com / user / MS4wLjABAAAAnCz_s5xyosgWTo5lTxKCmoYX1 - uiytDsAKBye1LbfDE',
			'Priority': 'u=0, i',
			'Connection': 'close'
		}
		# 抖音网页版获取关注人个人信息URL
		self.url = 'https://www.douyin.com/user/MS4wLjABAAAAnCz_s5xyosgWTo5lTxKCmoYX1-uiytDsAKBye1LbfDE'
		self.dir = 'log/douyin.txt'
	# 日志为空时执行此函数,获取狗子抖音视频数目
	def getDYQueue(self):
		res = requests.get(self.url,headers=self.reqHeaders)
		num = re.findall('data-e2e="user-tab-count">(\d*)</span>', res.text)[0]
		with open(self.dir, 'w') as f:
			f.write(str(num)+'\n')
		self.echoMsg('Info','抖音数目获取成功')
	# 监控函数
	def startdymonitor(self):
		returnDict = {}
		douyin = []
		with open(self.dir,'r') as f:
			for line in f.readlines():
				line = line.strip('\n')
				douyin.append(line)
		res = requests.get(self.url,headers=self.reqHeaders)
		num = re.findall('data-e2e="user-tab-count">(\d*)</span>', res.text)[0]
		d_url = self.url+':'+str(num)
		if d_url not in douyin:
			with open(self.dir, 'a') as f:
				f.write(d_url+'\n')
			self.echoMsg('Info','狗子抖音更新啦!!!')
			returnDict['nickName'] = '狗子'
			return returnDict
	# 格式化输出
	def echoMsg(self, level, msg):
		if level == 'Info':
			print('[Info] %s'%msg)
		elif level == 'Error':
			print('[Error] %s'%msg)

# def main():
# 	dy = dyMonitor()
# 	dy.startdymonitor()
#
# if __name__ == '__main__':
# 	main()
