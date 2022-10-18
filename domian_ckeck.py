#-*- coding=utf-8 -*-
import subprocess
import json
import sys
args="cat /etc/zabbix/"+sys.argv[1]
t=subprocess.Popen(args,shell=True,stdout=subprocess.PIPE).communicate()[0]
domains=[]
for domain in t.split('\n'):
        if len(domain) != 0:
                domains.append({'{#DOMAIN_NAME}':domain})
print json.dumps({'data':domains},indent=4,separators=(',',':'))
