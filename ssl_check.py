#!/usr/bin/env python3
# coding: utf-8 
# 查询域名证书到期情况

import re,sys
import time
import subprocess
from datetime import datetime
from io import StringIO

def main(domain):
    f = StringIO()
    comm = f"curl -Ivs https://{domain} --connect-timeout 16"
    # print(domain)
    result = subprocess.getstatusoutput(comm)
    f.write(result[1])
    m = re.search('start date: (.*?)\n.*?expire date: (.*?)\n.*?common name: (.*?)\n.*?issuer: CN=(.*?)\n', f.getvalue(), re.S)
    start_date = m.group(1)
    expire_date = m.group(2)
    # time 字符串转时间数组
    start_date = time.strptime(start_date, "%b %d %H:%M:%S %Y GMT")
    start_date_st = time.strftime("%Y-%m-%d %H:%M:%S", start_date)
    # datetime 字符串转时间数组
    expire_date = datetime.strptime(expire_date, "%b %d %H:%M:%S %Y GMT")
    expire_date_st = datetime.strftime(expire_date,"%Y-%m-%d %H:%M:%S")
    # 剩余天数
    remaining = (expire_date-datetime.now()).days
    print (remaining)
if __name__ == "__main__":
    if len(sys.argv)<2:
      print("你没有输入域名")
      sys.exit()
    domain = sys.argv[1]
    try:
      main(domain)
    except AttributeError:
      try:
        main(domain)
      except AttributeError:
        print(0)
