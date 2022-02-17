#!/usr/bin/env python3
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkbssopenapi.request.v20171214.QueryAccountBalanceRequest import QueryAccountBalanceRequest
import json
import telegram
import subprocess
import json
import sys
import time
import requests
import os
import shutil

chat_id = "XXXXXXX"
token = "XXXXXXXXX"
bot = telegram.Bot(token=token)

args = sys.argv[1]
file_path = args
#if os.path.isdir()
list = []
def tele_message():
    for line in open(file_path, 'r', encoding='UTF-8'):
        account_list = line.split(' ')
        aliyunaccount = account_list[0]
        aliyunAccessKey_ID = account_list[1]
        #print(aliyunAccessKey_ID)
        aliyunAccessKey_Secret = account_list[2].replace('\n', '')
        aliyunregion = 'cn-hangzhou'
        #aliyunregion = 'cn-hangzhou'
        #print(client = AcsClient('%s, %s, %s' %(aliyunAccessKey_ID,aliyunAccessKey_Secret,aliyunregion)))
        #print("client" = AcsClient(aliyunAccessKey_ID,aliyunAccessKey_Secret,aliyunregion))
        try:
            client = AcsClient(aliyunAccessKey_ID, aliyunAccessKey_Secret, aliyunregion)
            request = QueryAccountBalanceRequest()
            request.set_accept_format('json')
            response = client.do_action_with_exception(request)
            Balance_json = str(response, encoding='utf-8')
            print(Balance_json)
            Balance_sample_json = json.loads(Balance_json)['Data']['AvailableCashAmount']
        except:
            client = AcsClient(aliyunAccessKey_ID, aliyunAccessKey_Secret, aliyunregion)
            request = QueryAccountBalanceRequest()
            request.set_accept_format('json')
            response = client.do_action_with_exception(request)
            Balance_json = str(response, encoding='utf-8')
            print(Balance_json)
            Balance_sample_json = json.loads(Balance_json)['Data']['AvailableCashAmount']
    
        message = "阿里云账号: " + aliyunaccount + '  ' "账号余额：" + Balance_sample_json + '\n'
        print(message)
        list.append(message)

tele_message()
json_str = str(list).replace("[", "").replace("]", "").replace("'", "").replace("\\n", "\\\n").replace(",", "").replace("\\", "")
#print(json)
bot.send_message(chat_id, text=json_str)
#print(message)
