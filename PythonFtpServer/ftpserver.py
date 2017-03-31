# coding:utf-8
#----------------------------
# Author: Kun Liu         
# Start date: 2017-03-28  
# Latest edit: 2017-03-28
#=============================
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import settings

LOG_FILE = settings.LOG_FILE
CONTROAL_PORT = settings.CONTROAL_PORT
USER_NAME = settings.USER_NAME
PASSWD = settings.PASSWD

import os
USER_DIR = settings.USER_DIR
ANONY_DIR = settings.ANONY_DIR
if not os.path.exists(ANONY_DIR):
    os.mkdir(ANONY_DIR)

#新建一个用户组
authorizer = DummyAuthorizer()
#将用户名，密码，指定目录，权限 添加到里面
authorizer.add_user(USER_NAME, PASSWD, USER_DIR, perm="elr")#adfmw
#这个是添加匿名用户,任何人都可以访问，如果去掉的话，需要输入用户名和密码，可以自己尝试
if ANONY_DIR:
    authorizer.add_anonymous(ANONY_DIR)
 
handler = FTPHandler
handler.authorizer = authorizer
# Define a customized banner (string returned when client connects)
handler.banner = settings.banner

def main():
    # 日志设置
    # logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
    #开启服务器
    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()

if __name__ == '__main__':
    main()
