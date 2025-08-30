#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 微博
# Desc      : 微博主模块
# 添加新uid时，自行清空上一层里的微博id列表

import requests,json,sys

class WBMonitor():
	def __init__(self):
		self.reqHeaders = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Referer': 'https://passport.weibo.cn/signin/login',
			'Connection': 'close',
			'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
		}
		self.uid = ['1927305954', '7347878145', '6512991534']# 这里添加关注人的uid(成果, 犬来八荒, 王冰冰)
		self.dic = 'log/wbIds.txt'
	# 获取访问连接
	def getWBInfo(self):
		self.weiboInfo = []
		success_count = 0
		for i in self.uid:
			try:
				userInfo = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=%s'%(i)
				res = requests.get(userInfo,headers=self.reqHeaders)
				data = res.json()
				for j in data['data']['tabsInfo']['tabs']:
					if j['tab_type'] == 'weibo':
						self.weiboInfo.append('https://m.weibo.cn/api/container/getIndex?type=uid&value=%s&containerid=%s'%(i,j['containerid']))
				success_count += 1
			except Exception as e:
				print(f"获取用户 {i} 信息失败: {e}")
				continue
		
		if success_count == 0:
			raise Exception("所有微博用户信息获取失败，可能是API访问受限或网络问题")

	# 收集已经发布动态的id
	def getWBQueue(self):
		self.itemIds = []
		for i in self.weiboInfo:
			try:
				res = requests.get(i,headers=self.reqHeaders)
				data = res.json()
				with open(self.dic, 'a') as f:
					for j in data['data']['cards']:
						if j['card_type'] == 9:
							f.write(j['mblog']['id']+'\n')
							self.itemIds.append(j['mblog']['id'])
			except Exception as e:
				print(f"获取微博队列失败: {e}")
				continue
		self.echoMsg('Info', '微博数目获取成功')
		self.echoMsg('Info', '目前有 %s 条微博' %len(self.itemIds))
	# 开始监控
	def startmonitor(self):
		# 获取微博相关内容，编辑邮件内容
		returnDict = {}
		itemIds = []
		with open(self.dic,'r') as f:
			for line in f.readlines():
				line = line.strip('\n')
				itemIds.append(line)
		for i in self.weiboInfo:
			try:
				res = requests.get(i,headers=self.reqHeaders)
				data = res.json()
				for j in data['data']['cards']:
					if j['card_type'] == 9:
						if str(j['mblog']['id']) not in itemIds:
							with open(self.dic,'a') as f:
								f.write(j['mblog']['id']+'\n')
							self.echoMsg('Info','发微博啦!!!')
							self.echoMsg('Info','目前有 %s 条微博'%(len(itemIds)+1))
							returnDict['created_at'] = j['mblog']['created_at']
							returnDict['text'] = j['mblog']['text']
							returnDict['source'] = j['mblog']['source']
							returnDict['nickName'] = j['mblog']['user']['screen_name']
							return returnDict
			except Exception as e:
				print(f"监控微博失败: {e}")
				continue
	# 格式化输出
	def echoMsg(self, level, msg):
		if level == 'Info':
			print('[Info] %s'%msg)
		elif level == 'Error':
			print('[Error] %s'%msg)

# def main():
# 	wb = WBMonitor()
# 	wb.getWBInfo()
# 	wb.startmonitor()
#
# if __name__ == '__main__':
# 	main()