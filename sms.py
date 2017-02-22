#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: zhangkun
# date: 2017-01-10
import requests
import datetime
import time


sms_url = '''http://a4.go2yd.com/Website/message/send-sms?key=a548172fdbe9ff9e754f3251efa92856&mobile=86{0}&template=1&param[]={1}&param[]={2}&param[]={3}&threhold=25'''
req = sms_url.format("13297028626", time.strftime("%H:%M", time.localtime(time.time())), "10.103.18.102", "[PushMining,PushMining,PushMining,PushMining,PushMining,PushMining,12345678]网卡入口带宽已满，当前值:99.12")
print req

try:
    r = requests.get(req)
    print datetime.datetime.now(), r.text
    d = r.json()
    if d["code"] != 0:
        print datetime.datetime.now(), d["status"], d["reason"]
except:
    print "send sms exception"

# #print len("【一点资讯】[警告] 时间：10:20；服务：10.103.18.102；原因：[PushMining，PushMining，PushMining，PushMining，PushMining，PushMining,12345678]网卡入口带宽已满，当前值:99.12")
# #print len("1".decode("gb2312"))
# print len(u"张".decode("utf-8"))