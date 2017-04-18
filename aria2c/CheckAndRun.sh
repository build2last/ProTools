#!/bin/bash
# 注意 ` 和 ‘ 在 bash 里是有区别的， `` 中的内容会被当作命令执行
date=`date +%Y%m%d_%-H:%-M:%S`
query=`ps -e|grep 'aria2c'|sed -e "/grep/d"`
echo "$query"
if [ -z "$query" ];then    
	nohup aria2c -i /root/FTP/aria2/files.txt --conf-path=/root/FTP/aria2/aria2.conf &
	echo "Aria start!"
	echo "$date start aria2 download..." >>/root/FTP/aria2/bashlog.txt
else
	echo "Aria is already running!"
fi
exit 0
