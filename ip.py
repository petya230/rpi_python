#!/usr/bin/python3

import glob
import time
import os
import datetime
import sqlite3 as lite
import sys
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import urllib2
# Change to your own account information
to = 'user@gmail.com'
gmail_user = 'user@gmail.com'
gmail_password = 'password'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
extipaddr = urllib2.urlopen("http://icanhazip.com").read()
my_ip = 'Local IP: %s\nGlobal IP: %s' %  (ipaddr, extipaddr)
msg = MIMEText(my_ip)
msg['Subject'] = 'IP addres at: %s' % today.strftime("%Y-%m-%d")
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
