#!/usr/bin/env bash
machine_tag=3u8
machine_mem=`cat /proc/meminfo |grep MemTotal|awk -F " " '{print $2}'`
if [ $machine_mem -lt 90000000 ]; then
    machine_tag=3u8
elif [ $machine_mem -gt 90000000 -a $machine_mem -lt 100000000 ]; then
    machine_tag=2u
else
    machine_tag=1u
fi
echo $machine_tag


# sshpass
for i in $(cat backend_lg);do echo $i;sshpass -p "w@#UR6F#jfu3^" ssh -o StrictHostKeyChecking=no $i "bash /tmp/3u8.sh";done > /tmp/3u8.log
