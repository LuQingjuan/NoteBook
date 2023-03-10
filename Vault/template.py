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

class NotUSE():
	def Create_Folder(path):
		if not os.path.isdir(path):
			os.mkdir(path)
			#os.makedirs(path)

	def Create_File(path):
		if not os.path.isfile(path):
			os.mknod(path)

class TodoAction():
	def __init__(self):
		pass

	def Recursion_Insert_Data(self, src_lines, topic_id, topic_arr, info):
		topic = topic_arr[0]
		topic_flag = " ".rjust(topic_id+4, "#")
		tmp_src_lines = []

		write_flag = False
		search_flag = False
		update_info = ""
		for line in src_lines:
			if not write_flag:
				if not search_flag:
					if line == topic_flag + topic + "\n":
						search_flag = True
				elif search_flag:
					if line[:len(topic_flag)] != topic_flag:
						tmp_src_lines.append(line)
					if line[:len(topic_flag)] == topic_flag:
						write_flag = True
						if 0 == len(topic_arr[1:]):
							update_info = update_info + info + "\n"
						else:
							update_info = update_info + self.Recursion_Insert_Data(tmp_src_lines, topic_id+1, topic_arr[1:], info)
			update_info = update_info + line

		if write_flag == False:
			if search_flag == False:
				if 0 == len(topic_arr[1:]):
					update_info = update_info + topic_flag + topic + "\n" + info + "\n"
				else:
					update_info = update_info + topic_flag + topic + "\n"
					update_info = update_info + self.Recursion_Insert_Data(tmp_src_lines, topic_id+1, topic_arr[1:], info)
			else:
				update_info = update_info + info + "\n"
		return update_info

	def Insert_To_Todo_List_common(self, topic_arr, info):
		r_file = open("TodoList.md", 'r')
		try:
			lines_list = r_file.readlines()
		finally:
			r_file.close()

			update_info = self.Recursion_Insert_Data(lines_list, 0, topic_arr, info)

			#print(update_info)
			w_file = open("TodoList.md", 'w')
			try:
				w_file.write(update_info)
			finally:
				w_file.close( )

	#-----------------------------------------------------------------------------------
	def Note_Insert_To_Todo_List(self, topic):
		self.Insert_To_Todo_List_common(["Note"], "- [ ] ![[" + topic + "#" + topic + "|" + topic + "]]")

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

	def Todo_Template(self):
		os.chdir("PDCA")
		todo_info = ""
		todo_file = open("AllTodoList.md", 'r')
		try:
			line = ""
			while line != "---\n":
				line = todo_file.readline()
				todo_info = todo_info + line
		finally:
			todo_file.close()
		os.chdir("..")

		todo_info = todo_info + "\
## " + self.date + "\n\
\n\
\n\
### Note\n"
		return todo_info

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
![[AllTodoList#" + self.date + "|" + self.date + "]]\n\
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
	#-----------------------------------------------------

	def Create_Template(self, file_name, template):
		file = open(file_name, 'w')
		try:
			file.writelines(template)
		finally:
			file.close( )
	#-----------------------------------------------------

	def Create_Todo_File(self):
		self.Create_Template("TodoList.md", self.Todo_Template())

	def Create_Note_File(self, topic):
		os.chdir("NoteBook")
		os.chdir("01 Note")
		self.Create_Template(topic + ".md", self.Note_Template(topic))
		os.chdir("..")
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
    print("python3 ./template.py --mode=Temp --type=Todo")
    print("                                  --type=Note --topic=[Topic]")
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
	todo = TodoAction()

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

	if mode == "Temp":
		if type == "Todo":
			temp.Create_Todo_File()
		elif type == "Note":
			temp.Create_Note_File(topic)
			todo.Note_Insert_To_Todo_List(topic)
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
	os.chdir("..")
