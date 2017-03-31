# coding:utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

# Log of FTP server:
LOG_FILE = 'FTP_LOG.txt'

# Control port to connect to server:
CONTROAL_PORT = 21

# User config:
USER_NAME = "trend"
PASSWD = "111111"

# Directory to save data:
import os
# User data default at the file's dir path.
USER_DIR = os.getcwd()

# if ANONY_DIR is empty '', anonymous user will be disabled
ANONY_DIR = os.path.join(USER_DIR, 'anonymous')
if not os.path.exists(ANONY_DIR):
    os.mkdir(ANONY_DIR)

# Banner when loggin:
banner = "Wellcome Trenders! It's a FTP server powered by Pyftpdlib."