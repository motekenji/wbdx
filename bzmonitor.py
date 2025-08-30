#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : B站
# Desc      : B站对接口进行了反爬处理,原先爬取数据json接口无法直接访问了,因此从搜索接口进行对应关注人视频数量的监控(可能不准,因为删除视频也会引起数量变化)

import requests, re
from urllib.parse import quote, unquote

class bzMonitor():
	def __init__(self, ):
		self.reqHeaders = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Connection': 'close',
			'Accept-Encoding': 'gzip, deflate, br',
			'Upgrade-Insecure-Requests': '1',
			'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
		}
		# 这里添加关注人的昵称
		self.uid = ['犬来八荒w']
		self.dic = 'log/bilibili.txt'
	# 拼接各用户的访问连接
	def getBZUrl(self):
		self.bzurl = []
		for i in self.uid:
			url = 'https://search.bilibili.com/all?keyword=' + quote(i)
			self.bzurl.append(url)
	# 日志为空时执行此函数,获取各用户当前视频数目
	def getBZQueue(self):
		for i in self.bzurl:
			res = requests.get(i, headers=self.reqHeaders)
			# 稿件：43</span><a target="_blank"
			num = re.findall('稿件：(\d*)</span><a target="_blank"', res.text)[0]
			with open('/root/log/bilibili.txt','a') as f:
				f.write(i+':'+str(num)+'\n')
			self.echoMsg('Info','视频数目获取成功')
	# 监控函数
	def startbzmonitor(self):
		returnDict = {}
		bilibili = []
		with open(self.dic,'r') as f:
			for line in f.readlines():
				line = line.strip('\n')
				bilibili.append(line)
		for i in self.bzurl:
			res = requests.get(i, headers=self.reqHeaders)
			num = re.findall('视频：(\d*) <span class="user-video-desc-text"', res.text)[0]
			url2 = i + ':' + str(num)
			if url2 not in bilibili:
				with open(self.dic, 'a') as f:
					f.write(url2+'\n')
				self.echoMsg('Info', 'B站视频更新啦!!!')
				nickName = unquote(i.strip('https://search.bilibili.com/all?keyword='))
				returnDict['nickName'] = nickName
				return returnDict
	# 格式化输出
	def echoMsg(self, level, msg):
		if level == 'Info':
			print('[Info] %s'%msg)
		elif level == 'Error':
			print('[Error] %s'%msg)

def main():
	bz = bzMonitor()
	bz.getBZUrl()
	bz.startbzmonitor()

if __name__ == '__main__':
	main()