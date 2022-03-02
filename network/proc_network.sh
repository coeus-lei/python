#!/bin/bash
count=0
while [ $count -lt 2 ]
do
    count=$(($count+1))
    /usr/sbin/nethogs -t -d 2 -c 5 > /tmp/flow_nethogs.tmp
    if [[ $count == 2 ]];then
        exit
    else
        sleep 20
    fi
done
