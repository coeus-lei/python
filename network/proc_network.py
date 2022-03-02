#!/usr/bin/python
#coding=utf-8
#读取 nethogs.logs日志，获取流量过大的进程

#日志路径
# log_path="/tmp/flow_nethogs.tmp"
log_path="flow_nethogs.tmp"
file = open(log_path,"r")
message = file.read()
file.close()
#设置流量阀值大小，大于阀值则输出内容
max_flow = 0
#以Refreshing: 为分隔符，得到数组
mes_sp = message.split("Refreshing:")
# print(mes_sp)
#得到数组的最后一个元素，去掉空行
# print(len(mes_sp))
resu_str = mes_sp[len(mes_sp) - 1].strip("\n")
# print(resu_str)
#以换行符分割数据
resu_li = resu_str.split("\n")
for proc in resu_li:
    proc_li = proc.split("\t")
    if len(proc_li) == 3:
        proc_name = proc_li[0]
        # print(proc_name)
        proc_send = proc_li[1]
        print(proc_send)
        proc_rec = proc_li[2]
        # print(proc_rec)
        # if float(proc_send) > max_flow or float(proc_rec) > max_flow:
            # print("进程：" + proc_name + ", 发送: " + proc_send + " KB/sec, " + "接收: " + proc_rec + " KB/sec")
