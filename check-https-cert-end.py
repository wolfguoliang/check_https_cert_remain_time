#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2019-06-02 22:27 
# @Author : sunguolinag
# @File : check-https-cert-end.py 
# @Software: PyCharm
# @mail:418676288@qq.com 

import os,datetime,dateutil,sys,time
from dateutil import parser
#格式化时间串
time_format = "%Y-%m-%d"
#命令获取https 证书到期时间
cmd = "echo | openssl s_client -servername %s -connect %s:443 2>/dev/null |openssl x509 -noout -enddate | awk -F = '{print $2}'"%(sys.argv[1],sys.argv[1])
#取证书到期时间
crt_end_time = os.popen(cmd).readlines()[0]
#计算今天的时间
today = datetime.datetime.today()
#格式化字符串时间
tr_crt_end_time = parser.parse(crt_end_time)
f_crt_end_time = tr_crt_end_time.strftime(time_format)
f_today = today.strftime(time_format)
remain_days = ( parser.parse(f_crt_end_time) - parser.parse(f_today)).days
print(remain_days)
