# coding=utf-8
import json
import urllib2

date = "20180618"
server_url = 'http://api.goseek.cn/Tools/holiday?date='
# server_url = "http://www.easybots.cn/api/holiday.php?d="

vop_url_request = urllib2.Request(server_url + date)
vop_response = urllib2.urlopen(vop_url_request)

vop_data = json.loads(vop_response.read())

print vop_data
# print(type(vop_data))
# print(vop_data['data'])
# 工作日对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2
if vop_data['data'] == 0:
    print "this day is weekday"
# elif vop_data[date] == '1':
#     print 'This day is weekend'
elif vop_data['data'] == 2:
    print 'This day is holiday'
else:
    print 'Error'