#!/usr/bin/env python
#coding:utf-8

from datetime import timedelta,date,datetime

"""
一、说明
可以通过定义多个class来定义不同类别的全局变量
考虑可能对变量在不同引用处进行差异化的处理，所以使用方法而不是直接定义变量

二、引用方法
1.引入相应的类
sys.path.append('/data/git/hadoop_mining/data_mining/code/python/tool')
from DateTimeTool import DateTimeTool
2.通过类名点方法直接调用静态方法
print DateTimeTool.getPreviousMonthDateRange("2016-10-25")
"""

class DateTimeTool:
	"""
	根据传入的日期字符串（2016-10-25），返回该日期上一个月的日期范围数组
	例如"2016-10-25"返回['2016-09-01', '2016-09-30']
	dateStr为2016-10-01格式的日期字符串
	"""
	@staticmethod
	def getPreviousMonthDateRange(dateStr):
		dateStr = dateStr[0:8]+"01"
		dateStrArray = dateStr.split("-")
		datePreviousMonthLastDay = date(int(dateStrArray[0]),int(dateStrArray[1]),int(dateStrArray[2]))+timedelta(days=-1)
		previousMonthLastDayStr = datePreviousMonthLastDay.strftime("%Y-%m-%d")
		previousMonthFirstDayStr = datePreviousMonthLastDay.strftime('%Y-%m')+"-01"
		return [previousMonthFirstDayStr,previousMonthLastDayStr]
	
	"""
	根据传入的日期字符串（2016-10-25），返回该日期当前月的日期范围数组
	例如"2016-10-25"返回['2016-10-01', '2016-10-31']
	dateStr为2016-10-01格式的日期字符串
	"""
	@staticmethod
	def getCurrentMonthDateRange(dateStr):
		dateStrArray = dateStr.split("-")
		year = int(dateStrArray[0])
		month = int(dateStrArray[1])
		day = int(dateStrArray[2])
		year_for_first_day = year
		month_for_first_day = month
		if month==12:
			month_for_first_day = 1
			year_for_first_day = year+1
		else:
			month_for_first_day = month+1
		currentMonthLastDayStr = (date(year_for_first_day,month_for_first_day,1)+timedelta(days=-1)).strftime("%Y-%m-%d")
		currentMonthFirstDayStr = dateStr[0:8]+"01"
		return [currentMonthFirstDayStr,currentMonthLastDayStr]

	"""
	根据传入的日期字符串（2016-10-25）和截止星期数，返回该日期上一个星期的日期范围数组
	例如"2016-10-01" 5 返回['2016-09-18', '2016-09-24']
	python中星期数为0-6,0表示是星期一
	dateStr为2016-10-01格式的日期字符串
	endWeekNum为自定义的截止星期数0-6的整数（0表示周一）
	"""
	@staticmethod
	def getPreviousWeekDateRange(dateStr,endWeekNum):
		dateStrArray = dateStr.split("-")
		dateObj = date(int(dateStrArray[0]),int(dateStrArray[1]),int(dateStrArray[2]))
		dateWeekdayDiff = dateObj.weekday()-endWeekNum #与截止星期数相差的天数
		previousWeekLastDayStr = ""
		previousWeekFirstDayStr = ""
		if dateWeekdayDiff>0:
			previousWeekLastDayStr = (dateObj+timedelta(days=-dateWeekdayDiff)).strftime("%Y-%m-%d")
			previousWeekFirstDayStr = (dateObj+timedelta(days=-dateWeekdayDiff-6)).strftime("%Y-%m-%d")
		elif dateWeekdayDiff==0:
			previousWeekLastDayStr = (dateObj+timedelta(days=-7)).strftime("%Y-%m-%d")
			previousWeekFirstDayStr = (dateObj+timedelta(days=-7-6)).strftime("%Y-%m-%d")
		else:
			previousWeekLastDayStr = (dateObj+timedelta(days=-(7+dateWeekdayDiff))).strftime("%Y-%m-%d")
			previousWeekFirstDayStr = (dateObj+timedelta(days=-(7+dateWeekdayDiff)-6)).strftime("%Y-%m-%d")
		return [previousWeekFirstDayStr,previousWeekLastDayStr]
	
	"""
	根据传入的日期字符串（2016-10-25）和截止星期数，返回该日期所在星期的日期范围数组
	例如"2016-10-01" 5 返回['2016-09-25', '2016-10-01']
	python中星期数为0-6,0表示是星期一
	dateStr为2016-10-01格式的日期字符串
	endWeekNum为自定义的截止星期数0-6的整数（0表示周一）
	"""
	@staticmethod
	def getCurrentWeekDateRange(dateStr,endWeekNum):
		dateStrArray = dateStr.split("-")
		dateObj = date(int(dateStrArray[0]),int(dateStrArray[1]),int(dateStrArray[2]))
		dateWeekdayDiff = dateObj.weekday()-endWeekNum #与截止星期数相差的天数
		previousWeekLastDayStr = ""
		previousWeekFirstDayStr = ""
		if dateWeekdayDiff>0:
			previousWeekFirstDayStr = (dateObj+timedelta(days=-dateWeekdayDiff+1)).strftime("%Y-%m-%d")
			previousWeekLastDayStr = (dateObj+timedelta(days=-dateWeekdayDiff+1+6)).strftime("%Y-%m-%d")
		elif dateWeekdayDiff==0:
			previousWeekFirstDayStr = (dateObj+timedelta(days=dateWeekdayDiff-6)).strftime("%Y-%m-%d")
			previousWeekLastDayStr = (dateObj+timedelta(days=dateWeekdayDiff)).strftime("%Y-%m-%d")
		else:
			previousWeekFirstDayStr = (dateObj+timedelta(days=-dateWeekdayDiff-6)).strftime("%Y-%m-%d")
			previousWeekLastDayStr = (dateObj+timedelta(days=-dateWeekdayDiff)).strftime("%Y-%m-%d")
		return [previousWeekFirstDayStr,previousWeekLastDayStr]
	
	"""
	根据传入的日期字符串（2016-10-25）和增加天数，返回该日期加上传入天数后的日期字符串（2016-10-25）
	例如"2016-10-01" -1 返回2016-09-30
	dateStr为2016-10-01格式的日期字符串
	dayNum为自定义增加的天数，整数，支持正数、负数、零
	"""
	@staticmethod
	def dateAdd(dateStr,dayNum):
		dateStrArray = dateStr.split("-")
		dateObj = date(int(dateStrArray[0]),int(dateStrArray[1]),int(dateStrArray[2]))
		return (dateObj+timedelta(days=dayNum)).strftime("%Y-%m-%d")
	
	"""
	根据传入的日期字符串（2016-10-25），返回该日期的星期数（0-6，0代表周一）
	例如"2016-10-01"返回5
	python中星期数为0-6,0表示是星期一
	dateStr为2016-10-01格式的日期字符串
	"""
	@staticmethod
	def dateWeekNum(dateStr):
		dateStrArray = dateStr.split("-")
		dateObj = date(int(dateStrArray[0]),int(dateStrArray[1]),int(dateStrArray[2]))
		return dateObj.weekday()

if __name__ == '__main__': #测试
	dateStr = "2016-10-01"
	#参数为2016-10-01格式的日期字符串，返回该日期上一个月的日期范围数组['2016-09-01', '2016-09-30']
	print DateTimeTool.getPreviousMonthDateRange(dateStr)
	
	#参数为2016-10-01格式的日期字符串，返回该日期当前月的日期范围数组['2016-10-01', '2016-10-31']
	print DateTimeTool.getCurrentMonthDateRange(dateStr)
	
	#参数1为2016-10-01格式的日期字符串，参数2为自定义的截止星期数0-6的整数（0表示周一），返回该日期上一星期的日期范围数组['2016-09-18', '2016-09-24']
	print DateTimeTool.getPreviousWeekDateRange(dateStr,5)
	
	#参数1为2016-10-01格式的日期字符串，参数2为自定义的截止星期数0-6的整数（0表示周一），返回该日期所在星期的日期范围数组['2016-09-25', '2016-10-01']
	print DateTimeTool.getCurrentWeekDateRange(dateStr,5)
	
	#参数1为2016-10-01格式的日期字符串，参数2为自定义增加的天数，整数，支持正数、负数、零，返回该日期加上传入天数后的日期字符串2016-09-30
	print DateTimeTool.dateAdd(dateStr,-1)
	
	#参数为2016-10-01格式的日期字符串，返回该日期的星期数（0-6，0代表周一）5
	print DateTimeTool.dateWeekNum(dateStr)
	