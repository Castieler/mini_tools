#!/usr/bin/env python
#coding:utf-8

import urllib2

"""
一、说明
发送web请求工具类

二、引用方法
1.引入相应的类
sys.path.append('/data/git/hadoop_mining/data_mining/code/python/tool')
from WebRequestTool import WebRequestTool
2.通过类名点方法直接调用静态方法
WebRequestTool.sendRequestByTimeoutAndTryAgainTimes("",20,5,"error")
"""

class WebRequestTool:
	"""
	url web地址
	timeoutSecond 超过多少秒不再请求，重试下一次
	tryAgainTimes 请求发生异常或者超时时，尝试重新请求的次数
	errorMessage 请求失败时函数的返回值
	返回请求url后rd.read()的返回值，如果请求失败则返回errorMessage
	"""
	@staticmethod
	def sendRequestByTimeoutAndTryAgainTimes(url,timeoutSecond,tryAgainTimes,errorMessage):
		timeoutArg = timeoutSecond #超时时间设置，单位:秒
		tryAgainTimes = tryAgainTimes #重试次数
		j = 0
		rs = errorMessage
		while j<tryAgainTimes:
			try:
				req = urllib2.Request(url)
				rd = urllib2.urlopen(req,timeout=timeoutArg)
				rs = rd.read()
				break
			except Exception,e:
				print "url请求异常，异常详情————"+str(e)
				j += 1
		if j>=tryAgainTimes:
			print "重试"+str(j)+"次后，“"+url+"”仍然请求不到数据 "
			rs = errorMessage
		return rs

if __name__ == '__main__': #测试
	errorMessage = 0
	rd = WebRequestTool.sendRequestByTimeoutAndTryAgainTimes("",20,5,errorMessage)
	if rd != errorMessage:
		print rd
	else :
		print errorMessage
	
	rd = WebRequestTool.sendRequestByTimeoutAndTryAgainTimes(
			"http://weather.51wnl.com/weatherinfo/GetMoreWeather?cityCode=101040100&weatherType=0",
			20,
			3,errorMessage)
	if rd != errorMessage:
		print rd
	else :
		print errorMessage