#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------
# Version
#-----------------------------------------------------------
Version = '20230309'
#-----------------------------------------------------------
# Import
#-----------------------------------------------------------
import sys		# arg
import re		# reg
import time		# sleep
import os

from datetime import datetime, date, timedelta
import configparser
from multiprocessing import Process, Lock, SimpleQueue
from pathlib import Path

import pathlib
import csv
#import numpy as np
import math
#from matplotlib.dates import DateFormatter
#import jenkins #sudo -E pip3 install python-jenkins
#import SSHClass

class Template():
	def __init__(self):
		current = datetime.today()
		self.date = str(current)[:10]
		self.time = str(current)[11:19]
		self.week_count = current.isocalendar()[1]# 分别为年、当前周数、当前处于周几(2020, 16, 7)
		self.week = current.isocalendar()[2]
		#self.week = current.weekday()+1
		#print(self.date)
		#print(self.time)
		#print(self.week)
		#print(str(self.week_count))

	def Create_Folder(path):
		if not os.path.isdir(path):
			os.mkdir(path)
			#os.makedirs(path)

	def Create_File(path):
		if not os.path.isfile(path):
			os.mknod(path)

	def Note_Template(self, topic):
		date_time = self.date + " " + self.time
		return "\
* Type:\n\
* Tags:\n\
* Date: " + date_time + "\n\
* Related:\n\
* Reference:[]()\n\
\n\
## " + topic + "\n"

	def Day_Template(self):
		return "\
## Detail\n\
![[TodoList#" + self.date + "|" + self.date + "]]\n\
\n\
## 日复盘\n\
\n\
### 活动执行过程\n\
* 这样很好\n\
    1. \n\
\n\
* 可以提升\n\
    1. \n\
\n\
### 其他人处理方式\n\
* 值得学习\n\
    1. \n\
\n\
* 自己避免\n\
    1. \n\
\n\
### 自我评价\n\
* 棒棒的\n\
    1. \n\
\n\
* 调整下\n\
    1. \n\
\n"

	def Week_Template(self):
		return "\
## 周复盘\n\
\n\
## Detail\n\
#### Work\n\
* \n\
#### Study\n\
* \n"

	def Month_Template(self):
		return "\
## 月度复盘\n\
\n\
## Detail\n\
#### Work\n\
* \n\
#### Study\n\
* \n"

	def Quarter_Template(self):
		return "\
## 季度复盘\n\
\n\
## Detail\n\
#### Work\n\
* \n\
#### Study\n\
* \n"

	def Year_Template(self):
		return "\
## 年度复盘\n\
\n\
## Detail\n\
#### Work\n\
* \n\
#### Study\n\
* \n"

	def Create_Template(self, file_name, template):
		file = open(file_name, 'w')
		try:
			file.writelines(template)
		finally:
			file.close( )

	#-----------------------------------------------------
	def Create_Note_File(self, topic):
		os.chdir("Note")
		self.Create_Template(topic+ ".md", self.Note_Template(topic))
		os.chdir("..")

	def Create_Day_File(self):
		self.Create_Template(self.date + ".md", self.Day_Template())

	def Create_Week_File(self):
		self.Create_Template( + ".md", self.Week_Template())

	def Create_Month_File(self):
		self.Create_Template( + ".md", self.Month_Template())

	def Create_Quarter_File(self):
		self.Create_Template( + ".md", self.Quarter_Template())

	def Create_Year_File(self):
		self.Create_Template( + ".md", self.Year_Template())

#-----------------------------------------------------------
# Usage()
#-----------------------------------------------------------
def Usage():
    print("---------------------------------------------------")
    print("               Usage")
    print("python3 ./template.py --mode=Temp --type=Note --topic=[Topic]")
    print("                                  --type=Day")
    print("                                  --type=Week")
    print("                                  --type=Month")
    print("                                  --type=Quarter")
    print("                                  --type=Year")
    print("---------------------------------------------------")

if __name__ == '__main__':
	mode = ''
	argvs = sys.argv
	argc = len(argvs)
	temp = Template()

	while len(argvs) > 1:
		myArgv = argvs.pop(1)	# 0th is this file's name
		if re.match('^\-\-help$', myArgv, re.IGNORECASE):
			Usage()
			sys.exit(0)
		elif re.match('^\-\-mode=(.+)$', myArgv, re.IGNORECASE):
			matchReg = re.match('^\-\-mode=(.+)$', myArgv, re.IGNORECASE)
			mode = matchReg.group(1)
		elif re.match('^\-\-type=(.+)$', myArgv, re.IGNORECASE):
			matchReg = re.match('^\-\-type=(.+)$', myArgv, re.IGNORECASE)
			type = matchReg.group(1)
		elif re.match('^\-\-topic=(.+)$', myArgv, re.IGNORECASE):
			matchReg = re.match('^\-\-topic=(.+)$', myArgv, re.IGNORECASE)
			topic = matchReg.group(1)

	os.chdir("Today")
	if mode == "Temp":
		if type == "Note":
			temp.Create_Note_File(topic)
		elif type == "Day":
			temp.Create_Day_File()
		elif type == "Week":
			temp.Create_Week_File()
		elif type == "Month":
			temp.Create_Month_File()
		elif type == "Quarter":
			temp.Create_Quarter_File()
		elif type == "Year":
			temp.Create_Year_File()
		else:
			Usage()
	else:
		Usage()
