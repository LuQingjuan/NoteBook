import sys
import os
import re
import matplotlib.pyplot as plt
import numpy as np

import logging
logging.basicConfig(
	level=logging.INFO,
	format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)

def is_number(num):
	pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
	result = pattern.match(num)
	if result:
		return True
	else:
		return False 

def get_sum_list(a_list, b_list):
	c_list = []
	if 0 != len(a_list) and 0 == len(b_list):
		return a_list
	elif 0 == len(a_list) and 0 != len(b_list):
		return b_list
	elif 0 != len(a_list) and 0 != len(b_list) and len(a_list) != len(b_list):
		return c_list
	else:
		for id in range(len(a_list)):
			c_list.append(a_list[id]+b_list[id])
		return c_list

def formate_value_unit(basic_unit, value, new_unit):
	if 0 == value:
		return value

	if "G" == basic_unit[0]:
		if "G" == new_unit[0]:
			return value
		elif "M" == new_unit[0]:
			return value/1024
		elif "K" == new_unit[0]:
			return value/1024/1024
		else:
			return value/1024/1024/1024

	elif "M" == basic_unit[0]:
		if "G" == new_unit[0]:
			return value*1024
		elif "M" == new_unit[0]:
			return value
		elif "K" == new_unit[0]:
			return value/1024
		else:
			return value/1024/1024

	elif "K" == basic_unit[0]:
		if "G" == new_unit[0]:
			return value*1024*1024
		elif "M" == new_unit[0]:
			return value*1024
		elif "K" == new_unit[0]:
			return value
		else:
			return value/1024

	else:
		if "G" == new_unit[0]:
			return value*1024*1024*1024
		elif "M" == new_unit[0]:
			return value*1024*1024
		elif "K" == new_unit[0]:
			return value*1024
		else:
			return value

class Draw_PLT_Graph():
	def __init__(self, group_num, row_num, clon_num, name, log_name):
		self.group_num = group_num
		self.row_num = row_num
		self.clon_num = clon_num
		self.name = log_name.split('.')[0] + "_" + name

		self.fig = plt.figure(dpi=120, figsize=(16*self.clon_num, 9*(self.group_num*(self.row_num))))
		self.fig.suptitle(name)

	def __del__(self):
		plt.subplots_adjust(hspace=.0)
		plt.savefig(self.name + '.png')
		plt.close()
	
	def Create_Axe(self, group_id, row_id, clon_id):
		#logging.info("num:"+str(self.group_num)+", "+str(self.row_num)+", "+str(self.clon_num))
		#logging.info(" id:"+str(group_id)+", "+str(row_id)+", "+str(clon_id))
		#logging.info("add:"+str(self.group_num*(self.row_num+1)-1)+", "+str(self.clon_num)+", "+str((group_id*(self.row_num+1)+row_id)*self.clon_num+clon_id+1))
		return self.fig.add_subplot(self.group_num*(self.row_num+1)-1, self.clon_num, (group_id*(self.row_num+1)+row_id)*self.clon_num+clon_id+1)

	#---------------------------------------------------------------------------------------
	def SetYAsix(self, ax, y_asix_unit, set_max):
		count = 10
		y_min, y_max = ax.get_ylim()

		if set_max > y_max:
			y_max = set_max

		tmp_max = 1
		base_data = 0.1
		#get base data and max data
		if y_max > 1:
			#get base data
			tmp_max = 10
			base_data = 0.5
			while tmp_max*10 < y_max:
				tmp_max *= 10
				base_data *= 10

			#get max data
			tmp_max = base_data*10
			while tmp_max < y_max:
				if tmp_max + tmp_max/10 >= y_max:
					count += 1
					tmp_max += tmp_max/10
					break
				tmp_max += base_data*10

		y_max = tmp_max
		y_list = []
		y_labels = []
		for data in np.linspace(0, tmp_max, count+1, endpoint=True):
			y_list.append(data)
			y_labels.append(str('%.1f' % data)+y_asix_unit)
		ax.set_ylim(0, y_max+int(y_max/10))
		#logging.info(str(y_list))
		ax.set_yticks(y_list)
		ax.set_yticklabels(y_labels, fontweight='ultralight')

	def SetXAsix(self, ax, x_asix_unit, x_datas):
		# X: 12/12/2022 11:08:47
		if isinstance(x_datas[0],str):
			ax.set_xlim(0, len(x_datas))
			ax.set_xticklabels(x_datas, fontweight='ultralight', rotation=60)
			return
		if 0:
			# X: num
			count = 30
			x_min, x_max = ax.get_xlim()

			base_data = 1
			while base_data*count < x_max:
				base_data += 1
			count = int(x_max/base_data)
			if x_max > base_data*count:
				count += 1
			tmp_max = base_data*count

			x_list = []
			x_labels = []
			for data in np.linspace(0, tmp_max, count+1, endpoint=True):
				x_list.append(data)
				x_labels.append(str(int(data))+x_asix_unit)
			ax.set_xlim(0, x_max)
			ax.set_xticks(x_list)
			ax.set_xticklabels(x_labels, fontweight='ultralight')

	def Draw_Axes(self, axes, table_label, x_datas, x_unit, y_datas_list, y_unit_list, y_label_list, color_list):
		for id in range(len(y_datas_list)):
			if len(x_datas) != len(y_datas_list[id]):
				logging.info(y_label_list[id] + "x-axis num != y-axis data num")
				continue
			Throughput, = axes[id].plot(x_datas, y_datas_list[id], label=y_label_list[id], color=color_list[id])
			axes[id].legend([Throughput], [y_label_list[id]])
			self.SetYAsix(axes[id], y_unit_list[id], 0)
			self.SetXAsix(axes[id], '', x_datas)
			#axes[id-1].set_xlabel('Time (s)')

		#axes[int(len(y_datas_list)/2)].set_ylabel(table_label)

	def Draw_Graph(self, axe, table_label, x_datas, x_unit, y_datas_list, y_unit_list, y_label_list, color_list):
		#logging.info(str(len(y_datas_list))+" "+str(len(y_unit_list))+" "+str(len(y_label_list))+" "+str(len(color_list)))
		for id in range(len(y_datas_list)):
			#logging.info(str(x_datas))
			#logging.info(str(y_datas_list[id]))
			#logging.info(y_label_list[id])
			#logging.info(color_list[id])
			if len(x_datas) != len(y_datas_list[id]):
				logging.info(y_label_list[id] + "x-axis num != y-axis data num")
				continue
			axe.plot(x_datas, y_datas_list[id], label=y_label_list[id], color=color_list[id])
		self.SetYAsix(axe, y_unit_list[0], 0)
		self.SetXAsix(axe, '', x_datas)
		#axe.set_ylabel(table_label)
		axe.legend()

class Radisys_Log():
	# 例1)cu_up_statsは時間未表示、cu_cp_statsはUE CONN MGR STATISTICSで10秒ごとの時間表示。連携してcu_upの時間を確認可能に出来ないか
	def __init__(self, cu_up_log_name, cu_cp_log_name):
		self.log_name = cu_up_log_name
		self.time_info_lines = []
		self.ue_list = []
		self.x_datas = []
		self.throughputs_name = []

		x_date_log = cu_cp_log_name
		if "" == x_date_log:
			x_date_log = cu_up_log_name

		cmd = "grep -n 'UE CONN MGR STATISTICS' " + x_date_log + " | awk -F':' '{print $1}'"
		time_info_lines = self.DoCmd(cmd)
		#logging.info("time_info_lines: "+str(self.time_info_lines))

		for line_num in time_info_lines:
			cmd = "sed -n '" + line_num + "p' " + x_date_log + " | awk -F'[].[]' '{print $2}' | awk '{print $2}'"
			self.x_datas.append(self.DoCmd(cmd)[0].strip('\n'))
		#logging.info("x_datas: "+str(self.x_datas))

		cmd = "grep -n 'FAST-PKT PORT STATISTICS' " + self.log_name + " | awk -F':' '{print $1}'"
		self.time_info_lines = self.DoCmd(cmd)
		if x_date_log != cu_up_log_name:
			del self.time_info_lines[0]
		#logging.info("time_info_lines: "+str(self.time_info_lines))

		cmd = "grep -n '^UE-ID' " + self.log_name + " | awk -F'[][]' '{print $2}' | sort | uniq"
		self.ue_list = self.DoCmd(cmd)
		#logging.info("ue_datas: "+str(self.ue_list))

		cmd = "grep -B2 Throughput " + self.log_name + " | awk '{print $1}' | grep -E 'DL|UL' | sort | uniq"
		self.throughputs_name =self.DoCmd(cmd)
		#logging.info("throughputs_name: "+str(self.throughputs_name))

	def Get_UE_List(self):
		return self.ue_list

	def Get_X_List(self):
		return self.x_datas
	#---------------------------------------------------------------------------------------
	# Common
	def DoCmd(self, cmd):
		p = os.popen(cmd, 'r', 1)
		lines = p.readlines()
		values = []
		for line in lines:
			values.append(line.strip('\n'))
		p.close()
		#logging.info("------------------------------------------")
		#logging.info("CMD:"+str(cmd))
		#logging.info("RET:"+str(values))
		return values

	def Get_Key_Part_Line(self, start_line, end_line, start_flag, stop_flag):
		cmd = "sed -n '" + str(start_line) + "," + str(end_line) + "p' " + self.log_name + " | grep -n '" + start_flag + "' | awk -F':' '{print $1}END{if(NR==0){print 0}}'"
		#logging.info(cmd)
		p = os.popen(cmd, 'r', 1)
		tmp_line = p.readlines()[0].strip('\n')
		p.close()

		start_line = int(start_line) + int(tmp_line) + 1
		cmd = "sed -n '" + str(start_line) + "," + str(end_line) + "p' " + self.log_name + " | grep -n '^" + stop_flag + "' | awk -F':' '{print $1}END{if(NR==0){print 0}}'"
		#logging.info(cmd)
		p = os.popen(cmd, 'r', 1)
		tmp_line = int(p.readlines()[0].strip('\n'))
		p.close()

		return str(start_line-1), str(start_line+tmp_line-2)

	def Get_Iperf_EGTPU_Common(self, key, ue_id):
		y_datas_list = []
		y_unit = "Mbps"

		start_line = 1
		for end_line in self.time_info_lines:
			tmp_start, tmp_end = self.Get_Key_Part_Line(start_line, end_line, key, "                     ")
			cmd = "sed -n '" + tmp_start + "," + tmp_end + "p' " + self.log_name + " | grep '" + ue_id + "' | tail -n 1 | awk -F'|' '{print $10}END{if(NR==0){print 0}}'"
			#logging.info(cmd)
			p = os.popen(cmd, 'r', 1)
			line = p.readlines()
			if 0 == len(line[0].strip('\n')):
				y_datas_list.append(0)
			else:
				y_datas_list.append(float(line[0].replace('(' , '').replace(')' , '').strip('\n')))
			p.close()
			start_line = end_line
		#logging.info(str(y_datas_list))

		return y_datas_list, y_unit

	def Get_DDDS_RCVD_Common(self, key, ue_id):
		y_Rate_list = []
		y_Cnt_list = []

		start_line = 1
		for end_line in self.time_info_lines:
			tmp_start, tmp_end = self.Get_Key_Part_Line(start_line, end_line, key, "############")
			#logging.info(str(tmp_start) + "?=" + str(tmp_end))
			if tmp_start == tmp_end:
				y_Rate_list.append(0)
				y_Cnt_list.append(0)
				#logging.info(str(tmp_start) + "==" + str(tmp_end))
				start_line = end_line
				continue
			tmp_start, tmp_end = self.Get_Key_Part_Line(int(tmp_start), int(tmp_end)+1, "UE ID \[" + str(ue_id) + "\]", "############")

			cmd = "sed -n '" + tmp_start + "," + tmp_end + "p' " + self.log_name + " | grep -n 'DDDS-RCVD-Rate'"
			#logging.info(cmd)
			p = os.popen(cmd, 'r', 1)
			cmd_result = p.readlines()
			p.close()
			#logging.info(str(ue_id)+" ： "+cmd+"         "+str(cmd_result[0]))
			if len(cmd_result)>0:
				result = re.search('DDDS-RCVD-Rate (?P<Rate>\d+) DDDS-RCVD-CNT (?P<Cnt>\d+) ', cmd_result[0].strip('\n'))
				if result is not None:
					y_Rate_list.append(int(result.group('Rate')))
					y_Cnt_list.append(int(result.group('Cnt')))
				else:
					y_Rate_list.append(0)
					y_Cnt_list.append(0)
			else:
				y_Rate_list.append(0)
				y_Cnt_list.append(0)
			#logging.info(cmd+"\n"+str(cmd_result)+"\nRat = "+ str(Rate)+"    Cnt = "+ str(Cnt))
			start_line = end_line
		#logging.info(str(y_Rate)+"\n"+str(y_Cnt))

		#logging.info(str(y_tmp))
		#y_datas_list.append(y_tmp)

		return y_Rate_list, y_Cnt_list

	def Get_RX_Throughput_Common(self):
		y_DL_list = []
		y_DL_unit = "Mbps"
		y_UL_list = []
		y_UL_unit = "Mbps"

		start_line = 1
		for end_line in self.time_info_lines:
			tmp_start, tmp_end = self.Get_Key_Part_Line(start_line, end_line, "UDP RX STATISTICS", "############")
			cmd = "sed -n '" + tmp_start + "," + tmp_end + "p' " + self.log_name + " | grep -n 'Throughput'"
			#logging.info(cmd)
			p = os.popen(cmd, 'r', 1)
			cmd_result = p.readlines()
			p.close()
			#logging.info(cmd+"\n"+cmd_result[0].strip('\n'))
			if len(cmd_result)>0:
				result = re.search('Throughput \[UDP-DL-Rx (?P<DL>[0-9\.]+) (?P<DL_unit>[KMG]bps)\]  Throughput \[UDP-UL-Rx (?P<UL>[0-9\.]+) (?P<UL_unit>[KMG]bps)\]', cmd_result[0].strip('\n'))
				if result is not None:
					y_DL_list.append(formate_value_unit(y_DL_unit, float(result.group('DL')), result.group('DL_unit')))
					y_UL_list.append(formate_value_unit(y_UL_unit, float(result.group('UL')), result.group('UL_unit')))
				else:
					y_DL_list.append(0)
					y_UL_list.append(0)
			else:
				y_DL_list.append(0)
				y_UL_list.append(0)
			#logging.info(cmd+"\n"+str(cmd_result)+"\nRat = "+ str(Rate)+"    Cnt = "+ str(Cnt))
			start_line = end_line
		#logging.info(str(y_DL)+"\n"+str(y_UL))

		#logging.info(str(y_tmp))
		#y_datas_list.append(y_tmp)

		return y_DL_list, y_DL_unit, y_UL_list, y_UL_unit

	def Get_TX_Throughput_Common(self, key, type_name):
		y_Throughput_list = []
		y_Throughput_unit = "Mbps"

		start_line = 1
		for end_line in self.time_info_lines:
			tmp_start, tmp_end = self.Get_Key_Part_Line(start_line, end_line, "UDP TX STATISTICS", "####")
			cmd = "sed -n '" + tmp_start + "," + tmp_end + "p' " + self.log_name + " | grep -n '" + type_name + "'"
			#logging.info(cmd)
			p = os.popen(cmd, 'r', 1)
			cmd_result = p.readlines()
			p.close()
			#logging.info(cmd+"\n"+cmd_result[0].strip('\n'))
			if len(cmd_result)>0:
				if 'UL' in type_name:
					result = re.search('Throughput \[UDP-UL-Tx \((?P<Throughput>[0-9\.]+) (?P<Throughput_unit>[KMG]bps)\)\]', cmd_result[0].strip('\n'))
				else:
					result = re.search('Throughput \[UDP-DL-Tx \d+  \((?P<Throughput>[0-9\.]+) (?P<Throughput_unit>[KMG]bps)\)\]', cmd_result[0].strip('\n'))

				if result is not None:
					y_Throughput_list.append(formate_value_unit(y_Throughput_unit, float(result.group('Throughput')), result.group('Throughput_unit')))
				else:
					y_Throughput_list.append(0)
			else:
				y_Throughput_list.append(0)
			#logging.info(cmd+"\n"+str(cmd_result)+"\nRat = "+ str(Rate)+"    Cnt = "+ str(Cnt))
			start_line = end_line
		#logging.info(str(y_DL)+"\n"+str(y_UL))

		#logging.info(str(y_tmp))
		#y_datas_list.append(y_tmp)

		return y_Throughput_list, y_Throughput_unit

	#---------------------------------------------------------------------------------------
	# 例2)EGTPU UPPER, LOWER の STATISTICS の抽出など（10秒ごとのu-plane流量の可視化）
	def Get_DL_Iperf_EGTPU_Data(self, ue_id):
		# 5GG->CU
		y_rx_datas_list, y_rx_unit = self.Get_Iperf_EGTPU_Common('EGTPU UPPER RX STATISTICS', ue_id)
		# CU->DU
		y_tx_datas_list, y_tx_unit = self.Get_Iperf_EGTPU_Common('EGTPU LOWER TX STATISTICS', ue_id)
		return y_rx_datas_list, y_rx_unit, y_tx_datas_list, y_tx_unit

	def Get_UL_Iperf_EGTPU_Data(self, ue_id):
		# DU->CU
		y_rx_datas_list, y_rx_unit = self.Get_Iperf_EGTPU_Common('EGTPU LOWER RX STATISTICS', ue_id)
		# CU->5GG
		y_tx_datas_list, y_tx_unit = self.Get_Iperf_EGTPU_Common('EGTPU UPPER TX STATISTICS', ue_id)
		return y_rx_datas_list, y_rx_unit, y_tx_datas_list, y_tx_unit

	# 例2)UDP RX, TX の STATISTICS の抽出など（10秒ごとのu-plane流量の可視化）
	def Get_DL_Iperf_UDP_Data(self):
		y_DL_list, y_DL_unit, y_UL_list, y_UL_unit = self.Get_RX_Throughput_Common()
		y_dl8_Throughput_list, y_dl8_Throughput_unit = self.Get_TX_Throughput_Common("UDP-DL-Tx","DL-8")
		y_dl9_Throughput_list, y_dl9_Throughput_unit = self.Get_TX_Throughput_Common("UDP-DL-Tx","DL-9")
		y_dl10_Throughput_list, y_dl10_Throughput_unit = self.Get_TX_Throughput_Common("UDP-DL-Tx","DL-10")
		return y_DL_list, y_DL_unit, y_dl8_Throughput_list, y_dl8_Throughput_unit, y_dl9_Throughput_list, y_dl9_Throughput_unit, y_dl10_Throughput_list, y_dl10_Throughput_unit

	def Get_UL_Iperf_UDP_Data(self):
		y_DL_list, y_DL_unit, y_UL_list, y_UL_unit = self.Get_RX_Throughput_Common()
		y_ul11_Throughput_list, y_ul11_Throughput_unit = self.Get_TX_Throughput_Common("UDP-UL-Tx","UL-11")
		return y_UL_list, y_UL_unit, y_ul11_Throughput_list, y_ul11_Throughput_unit

	# 例3)PDCP RX, TX STATISTICSの抽出など（DDDSなどのデータを元にCU-UP内の10秒ごとの滞留バッファ量の可視化）
	def Get_DDDS_RCVD_RX0(self, ue_id):
		return self.Get_DDDS_RCVD_Common('PDCP RX \[0\] STATISTICS', ue_id)

	def Get_DDDS_RCVD_TX0(self, ue_id):
		return self.Get_DDDS_RCVD_Common('PDCP TX \[0\] STATISTICS', ue_id)

	def Get_DDDS_RCVD_TX1(self, ue_id):
		return self.Get_DDDS_RCVD_Common('PDCP TX \[1\] STATISTICS', ue_id)

	def Get_DDDS_RCVD_TX2(self, ue_id):
		return self.Get_DDDS_RCVD_Common('PDCP TX \[2\] STATISTICS', ue_id)


class Radisys_Graph():
	def __init__(self, cu_up_log_name, cu_cp_log_name):
		self.log_name = cu_up_log_name
		self.radisys = Radisys_Log(cu_up_log_name, cu_cp_log_name)
		self.ue_list = self.radisys.Get_UE_List()
		self.x_list = self.radisys.Get_X_List()

	def Draw_Iperf_EGTPU(self):
		logging.info("--------------------------------------------------------------")
		logging.info("Start Draw Iperf EGTPU Graph")
		if 0 == len(self.ue_list):
			logging.info("No UE Attch.")
			logging.info("Can't Draw Iperf EGTPU Graph")
			return
		# EGTPU UPPER RX STATISTICS
		# EGTPU LOWER TX STATISTICS
		# EGTPU LOWER RX STATISTICS
		# EGTPU UPPER TX STATISTICS
		#                    group_num, row_num, clon_num, name
		#dpg = Draw_PLT_Graph(2, len(self.ue_list)+1, 3, "name")
		dpg = Draw_PLT_Graph(len(self.ue_list)+1, 3, 2, "DL UL Iperf EGTPU", self.log_name)

		y_dl_rx_sum_datas_list = []
		y_dl_tx_sum_datas_list = []
		y_ul_rx_sum_datas_list = []
		y_ul_tx_sum_datas_list = []
		axes = []
		color_list = ['black','blue','red','green']
		for ue_id in range(len(self.ue_list)):
			# ---------------------------------------------------------------------------------------------------
			# DL_Iperf_EGTPU
			y_rx_datas_list, y_rx_unit, y_tx_datas_list, y_tx_unit = self.radisys.Get_DL_Iperf_EGTPU_Data(self.ue_list[ue_id])
			y_dl_rx_sum_datas_list = get_sum_list(y_dl_rx_sum_datas_list, y_rx_datas_list)
			y_dl_tx_sum_datas_list = get_sum_list(y_dl_tx_sum_datas_list, y_tx_datas_list)

			axe = dpg.Create_Axe(ue_id+1, 0, 0)
			axe.set_title(self.ue_list[ue_id] + ' DL Iperf EGTPU')
			dpg.Draw_Graph(axe, self.ue_list[ue_id], self.x_list, "", [y_rx_datas_list, y_tx_datas_list], [y_rx_unit, y_tx_unit], ['EGTPU UPPER RX (5GC -> CU)','EGTPU LOWER TX (CU -> DU)'], color_list)

			axes.clear()
			axes.append(dpg.Create_Axe(ue_id+1, 1, 0))
			axes.append(dpg.Create_Axe(ue_id+1, 2, 0))
			dpg.Draw_Axes(axes, self.ue_list[ue_id], self.x_list, "", [y_rx_datas_list, y_tx_datas_list], [y_rx_unit, y_tx_unit], ['EGTPU UPPER RX (5GC -> CU)','EGTPU LOWER TX (CU -> DU)'], color_list)

			# ---------------------------------------------------------------------------------------------------
			# UL_Iperf_EGTPU
			y_rx_datas_list, y_rx_unit, y_tx_datas_list, y_tx_unit = self.radisys.Get_UL_Iperf_EGTPU_Data(self.ue_list[ue_id])
			y_ul_rx_sum_datas_list = get_sum_list(y_ul_rx_sum_datas_list, y_rx_datas_list)
			y_ul_tx_sum_datas_list = get_sum_list(y_ul_tx_sum_datas_list, y_tx_datas_list)

			axe = dpg.Create_Axe(ue_id+1, 0, 1)
			axe.set_title(self.ue_list[ue_id] + ' UL Iperf EGTPU')
			dpg.Draw_Graph(axe, self.ue_list[ue_id], self.x_list, "", [y_rx_datas_list, y_tx_datas_list], [y_rx_unit, y_tx_unit], ['EGTPU LOWER RX (DU -> CU)','EGTPU UPPER TX (CU -> 5GC)'], color_list)

			axes.clear()
			axes.append(dpg.Create_Axe(ue_id+1, 1, 1))
			axes.append(dpg.Create_Axe(ue_id+1, 2, 1))
			dpg.Draw_Axes(axes, self.ue_list[ue_id], self.x_list, "", [y_rx_datas_list, y_tx_datas_list], [y_rx_unit, y_tx_unit], ['EGTPU LOWER RX (DU -> CU)','EGTPU UPPER TX (CU -> 5GC)'], color_list)

		# ---------------------------------------------------------------------------------------------------
		# DL_Iperf_EGTPU
		axe = dpg.Create_Axe(0, 0, 0)
		axe.set_title('All UE DL Iperf EGTPU')
		dpg.Draw_Graph(axe, self.ue_list[ue_id], self.x_list, "", [y_dl_rx_sum_datas_list, y_dl_tx_sum_datas_list], [y_rx_unit, y_tx_unit], ['EGTPU UPPER RX (5GC -> CU)','EGTPU LOWER TX (CU -> DU)'], color_list)

		axes.clear()
		axes.append(dpg.Create_Axe(0, 1, 0))
		axes.append(dpg.Create_Axe(0, 2, 0))
		dpg.Draw_Axes(axes, self.ue_list[ue_id], self.x_list, "", [y_dl_rx_sum_datas_list, y_dl_tx_sum_datas_list], [y_rx_unit, y_tx_unit], ['EGTPU UPPER RX (5GC -> CU)','EGTPU LOWER TX (CU -> DU)'], color_list)

		# ---------------------------------------------------------------------------------------------------
		# UL_Iperf_EGTPU
		axe = dpg.Create_Axe(0, 0, 1)
		axe.set_title('All UE UL Iperf EGTPU')
		dpg.Draw_Graph(axe, self.ue_list[ue_id], self.x_list, "", [y_ul_rx_sum_datas_list, y_ul_tx_sum_datas_list], [y_rx_unit, y_tx_unit], ['EGTPU LOWER RX (DU -> CU)','EGTPU UPPER TX (CU -> 5GC)'], color_list)

		axes.clear()
		axes.append(dpg.Create_Axe(0, 1, 1))
		axes.append(dpg.Create_Axe(0, 2, 1))
		dpg.Draw_Axes(axes, self.ue_list[ue_id], self.x_list, "", [y_ul_rx_sum_datas_list, y_ul_tx_sum_datas_list], [y_rx_unit, y_tx_unit], ['EGTPU LOWER RX (DU -> CU)','EGTPU UPPER TX (CU -> 5GC)'], color_list)

	def Draw_Iperf_UDP(self):
		logging.info("--------------------------------------------------------------")
		logging.info("Start Draw Iperf UDP Graph")
		# UDP RX STATISTICS      DLRx-7 Throughput [UDP-DL-Rx 0.00 Mbps]  Throughput [UDP-UL-Rx 0.00 Mbps] 
		# UDP TX STATISTICS      DL-8  Throughput [UDP-DL-Tx 8  (0.00 Mbps)][ CUMM-TX-FAIL: 0]
		# UDP TX STATISTICS      DL-9  Throughput [UDP-DL-Tx 9  (0.00 Mbps)][ CUMM-TX-FAIL: 0]
		# UDP TX STATISTICS      DL-10  Throughput [UDP-DL-Tx 10  (0.00 Mbps)][ CUMM-TX-FAIL: 0]
		# UDP TX STATISTICS      UL-11  Throughput [UDP-UL-Tx (0.00 Mbps)][ CUMM-TX-FAIL: 0]
		#                    group_num, row_num, clon_num, name
		dpg = Draw_PLT_Graph(1, 5, 2, "DL UL Iperf Throughput", self.log_name)

		axes = []
		color_list = ['black','blue','red','green']

		# ---------------------------------------------------------------------------------------------------
		# DL_Iperf_Throughput
		y_DL_list, y_DL_unit, y_dl8_Throughput_list, y_dl8_Throughput_unit, y_dl9_Throughput_list, y_dl9_Throughput_unit, y_dl10_Throughput_list, y_dl10_Throughput_unit = self.radisys.Get_DL_Iperf_UDP_Data()

		axe = dpg.Create_Axe(0, 0, 0)
		axe.set_title('DL Iperf Throughput')
		dpg.Draw_Graph(axe, "", self.x_list, "", [y_DL_list, y_dl8_Throughput_list, y_dl9_Throughput_list, y_dl10_Throughput_list], [y_DL_unit, y_dl8_Throughput_unit, y_dl9_Throughput_unit, y_dl10_Throughput_unit], ['DL (UDP RX STATISTICS)', 'DL 8 (UDP TX STATISTICS)', 'DL 9 (UDP TX STATISTICS)', 'DL 10 (UDP TX STATISTICS)'], color_list)

		axes.clear()
		axes.append(dpg.Create_Axe(0, 1, 0))
		axes.append(dpg.Create_Axe(0, 2, 0))
		axes.append(dpg.Create_Axe(0, 3, 0))
		axes.append(dpg.Create_Axe(0, 4, 0))
		dpg.Draw_Axes(axes, "", self.x_list, "", [y_DL_list, y_dl8_Throughput_list, y_dl9_Throughput_list, y_dl10_Throughput_list], [y_DL_unit, y_dl8_Throughput_unit, y_dl9_Throughput_unit, y_dl10_Throughput_unit], ['DL (UDP RX STATISTICS)', 'DL 8 (UDP TX STATISTICS)', 'DL 9 (UDP TX STATISTICS)', 'DL 10 (UDP TX STATISTICS)'], color_list)

		# ---------------------------------------------------------------------------------------------------
		# UL_Iperf_Throughput
		y_UL_list, y_UL_unit, y_ul11_Throughput_list, y_ul11_Throughput_unit = self.radisys.Get_UL_Iperf_UDP_Data()

		axe = dpg.Create_Axe(0, 0, 1)
		axe.set_title('UL Iperf Throughput')
		dpg.Draw_Graph(axe, "", self.x_list, "", [y_UL_list, y_ul11_Throughput_list], [y_UL_unit, y_ul11_Throughput_unit], ['UL (UDP RX STATISTICS)','UL 11 (UDP TX STATISTICS)'], color_list)

		axes.clear()
		axes.append(dpg.Create_Axe(0, 1, 1))
		axes.append(dpg.Create_Axe(0, 2, 1))
		dpg.Draw_Axes(axes, "", self.x_list, "", [y_UL_list, y_ul11_Throughput_list], [y_UL_unit, y_ul11_Throughput_unit], ['UL (UDP RX STATISTICS)','UL 11 (UDP TX STATISTICS)'], color_list)

	def Draw_DDDS_RCVD(self):
		logging.info("--------------------------------------------------------------")
		logging.info("Start Draw DDDS RCVD Graph")
		if 0 == len(self.ue_list):
			logging.info("No UE Attch.")
			logging.info("Can't Draw DDDS RCVD Graph")
			return
		#PDCP RX [0] STATISTICS    DDDS-RCVD-Rate  DDDS-RCVD-CNT 
		#PDCP TX [0] STATISTICS    DDDS-RCVD-Rate  DDDS-RCVD-CNT 
		#PDCP TX [1] STATISTICS    DDDS-RCVD-Rate  DDDS-RCVD-CNT 
		#PDCP TX [2] STATISTICS    DDDS-RCVD-Rate  DDDS-RCVD-CNT 
		#                    group_num, row_num, clon_num, name
		dpg = Draw_PLT_Graph(len(self.ue_list)+1, 5, 2, "DDDS RCVD", self.log_name)

		y_rx0_sum_Rate_list = []
		y_tx0_sum_Rate_list = []
		y_tx1_sum_Rate_list = []
		y_tx2_sum_Rate_list = []
		y_rx0_sum_Cnt_list = []
		y_tx0_sum_Cnt_list = []
		y_tx1_sum_Cnt_list = []
		y_tx2_sum_Cnt_list = []
		axes = []
		color_list = ['black','blue','red','green']
		for ue_id in range(len(self.ue_list)):
			# ---------------------------------------------------------------------------------------------------
			y_rx0_Rate_list, y_rx0_Cnt_list = self.radisys.Get_DDDS_RCVD_RX0(self.ue_list[ue_id])
			y_tx0_Rate_list, y_tx0_Cnt_list = self.radisys.Get_DDDS_RCVD_TX0(self.ue_list[ue_id])
			y_tx1_Rate_list, y_tx1_Cnt_list = self.radisys.Get_DDDS_RCVD_TX1(self.ue_list[ue_id])
			y_tx2_Rate_list, y_tx2_Cnt_list = self.radisys.Get_DDDS_RCVD_TX2(self.ue_list[ue_id])

			y_rx0_sum_Rate_list = get_sum_list(y_rx0_sum_Rate_list, y_rx0_Rate_list)
			y_tx0_sum_Rate_list = get_sum_list(y_tx0_sum_Rate_list, y_tx0_Rate_list)
			y_tx1_sum_Rate_list = get_sum_list(y_tx1_sum_Rate_list, y_tx1_Rate_list)
			y_tx2_sum_Rate_list = get_sum_list(y_tx2_sum_Rate_list, y_tx2_Rate_list)
			y_rx0_sum_Cnt_list = get_sum_list(y_rx0_sum_Cnt_list, y_rx0_Cnt_list)
			y_tx0_sum_Cnt_list = get_sum_list(y_tx0_sum_Cnt_list, y_tx0_Cnt_list)
			y_tx1_sum_Cnt_list = get_sum_list(y_tx1_sum_Cnt_list, y_tx1_Cnt_list)
			y_tx2_sum_Cnt_list = get_sum_list(y_tx2_sum_Cnt_list, y_tx2_Cnt_list)

			axe = dpg.Create_Axe(ue_id+1, 0, 0)
			axe.set_title(self.ue_list[ue_id] + ' Rate')
			dpg.Draw_Graph(axe, self.ue_list[ue_id], self.x_list, "", [y_rx0_Rate_list, y_tx0_Rate_list, y_tx1_Rate_list, y_tx2_Rate_list], ["", "", "", ""], ["RX0", "TX0", "TX1", "TX2"], color_list)

			axes.clear()
			axes.append(dpg.Create_Axe(ue_id+1, 1, 0))
			axes.append(dpg.Create_Axe(ue_id+1, 2, 0))
			axes.append(dpg.Create_Axe(ue_id+1, 3, 0))
			axes.append(dpg.Create_Axe(ue_id+1, 4, 0))
			dpg.Draw_Axes(axes, self.ue_list[ue_id], self.x_list, "", [y_rx0_Rate_list, y_tx0_Rate_list, y_tx1_Rate_list, y_tx2_Rate_list], ["", "", "", ""], ["RX0", "TX0", "TX1", "TX2"], color_list)

			axe = dpg.Create_Axe(ue_id+1, 0, 1)
			axe.set_title(self.ue_list[ue_id] + ' Cnt')
			dpg.Draw_Graph(axe, self.ue_list[ue_id], self.x_list, "", [y_rx0_Cnt_list, y_tx0_Cnt_list, y_tx1_Cnt_list, y_tx2_Cnt_list], ["", "", "", ""], ["RX0", "TX0", "TX1", "TX2"], color_list)

			axes.clear()
			axes.append(dpg.Create_Axe(ue_id+1, 1, 1))
			axes.append(dpg.Create_Axe(ue_id+1, 2, 1))
			axes.append(dpg.Create_Axe(ue_id+1, 3, 1))
			axes.append(dpg.Create_Axe(ue_id+1, 4, 1))
			dpg.Draw_Axes(axes, self.ue_list[ue_id], self.x_list, "", [y_rx0_Cnt_list, y_tx0_Cnt_list, y_tx1_Cnt_list, y_tx2_Cnt_list], ["", "", "", ""], ["RX0", "TX0", "TX1", "TX2"], color_list)

			#logging.info("================================================")
			#logging.info(self.ue_list[ue_id] + " " + str(len(self.x_list)))
			#logging.info(str(len(y_rx0_Rate_list)) + " " + str(y_rx0_Cnt_list))
			#logging.info(str(len(y_tx0_Rate_list)) + " " + str(y_tx0_Cnt_list))
			#logging.info(str(len(y_tx1_Rate_list)) + " " + str(y_tx1_Cnt_list))
			#logging.info(str(len(y_tx2_Rate_list)) + " " + str(y_tx2_Cnt_list))

		axe = dpg.Create_Axe(0, 0, 0)
		axe.set_title('All Rate')
		dpg.Draw_Graph(axe, self.ue_list[ue_id], self.x_list, "", [y_rx0_sum_Rate_list, y_tx0_sum_Rate_list, y_tx1_sum_Rate_list, y_tx2_sum_Rate_list], ["", "", "", ""], ["RX0", "TX0", "TX1", "TX2"], color_list)

		axes.clear()
		axes.append(dpg.Create_Axe(0, 1, 0))
		axes.append(dpg.Create_Axe(0, 2, 0))
		axes.append(dpg.Create_Axe(0, 3, 0))
		axes.append(dpg.Create_Axe(0, 4, 0))
		dpg.Draw_Axes(axes, self.ue_list[ue_id], self.x_list, "", [y_rx0_sum_Rate_list, y_tx0_sum_Rate_list, y_tx1_sum_Rate_list, y_tx2_sum_Rate_list], ["", "", "", ""], ["RX0", "TX0", "TX1", "TX2"], color_list)

		axe = dpg.Create_Axe(0, 0, 1)
		axe.set_title('All Cnt')
		dpg.Draw_Graph(axe, self.ue_list[ue_id], self.x_list, "", [y_rx0_sum_Cnt_list, y_tx0_sum_Cnt_list, y_tx1_sum_Cnt_list, y_tx2_sum_Cnt_list], ["", "", "", ""], ["RX0", "TX0", "TX1", "TX2"], color_list)

		axes.clear()
		axes.append(dpg.Create_Axe(0, 1, 1))
		axes.append(dpg.Create_Axe(0, 2, 1))
		axes.append(dpg.Create_Axe(0, 3, 1))
		axes.append(dpg.Create_Axe(0, 4, 1))
		dpg.Draw_Axes(axes, self.ue_list[ue_id], self.x_list, "", [y_rx0_sum_Cnt_list, y_tx0_sum_Cnt_list, y_tx1_sum_Cnt_list, y_tx2_sum_Cnt_list], ["", "", "", ""], ["RX0", "TX0", "TX1", "TX2"], color_list)


#r_png = Radisys_Graph("86/cu_cp_stats_23_01_10_19_40_55.txt", "86/cu_up_stats_23_01_10_19_40_52.txt")
#r_png.Draw_Iperf_EGTPU()
#r_png.Draw_DDDS_RCVD()
#r_png.Draw_Iperf_UDP()
#
#exit()


argvs = sys.argv
argc = len(argvs)

if 2 == argc and "cu_cp" not in argvs[1] and "cu_up" not in argvs[1]:
	r_png = Radisys_Graph(argvs[1], "")
elif 3 == argc and "cu_cp" in argvs[1] and "cu_up" in argvs[2]:
	r_png = Radisys_Graph(argvs[2], argvs[1])
elif 3 == argc and "cu_cp" in argvs[2] and "cu_up" in argvs[1]:
	r_png = Radisys_Graph(argvs[1], argvs[2])
else:
	logging.info("python3 main.py cu_cp_status_xxxx.txt cu_up_status_xxxx.txt")
	logging.info("or")
	logging.info("python3 main.py cu_status_xxxx.txt")
	exit(1)

# ok
r_png.Draw_Iperf_EGTPU()
r_png.Draw_DDDS_RCVD()
r_png.Draw_Iperf_UDP()




#	r_log = Radisys_Log("cu_stats_22_12_12_11_31_56_2du_3ue_dl_iperf.txt")
#
#	logging.info("65537"+str(r_log.Get_Iperf_EGTPU_Common("EGTPU UPPER RX STATISTICS","65537")))
#	logging.info("65538"+str(r_log.Get_Iperf_EGTPU_Common("EGTPU LOWER TX STATISTICS","65538")))
#	logging.info("65539"+str(r_log.Get_Iperf_EGTPU_Common("EGTPU LOWER RX STATISTICS","65539")))
#	logging.info("65540"+str(r_log.Get_Iperf_EGTPU_Common("EGTPU UPPER TX STATISTICS","65540")))
#	logging.info("65541"+str(r_log.Get_Iperf_EGTPU_Common("EGTPU UPPER RX STATISTICS","65541")))
#	logging.info("65542"+str(r_log.Get_Iperf_EGTPU_Common("EGTPU UPPER RX STATISTICS","65542")))
#
#	logging.info(""+str(r_log.Get_RX_Throughput_Common()))
#	logging.info("DL-8"+str(r_log.Get_TX_Throughput_Common("UDP-DL-Tx","DL-8")))
#	logging.info("DL-9"+str(r_log.Get_TX_Throughput_Common("UDP-DL-Tx","DL-9")))
#	logging.info("DL-10"+str(r_log.Get_TX_Throughput_Common("UDP-DL-Tx","DL-10")))
#	logging.info("UL-11"+str(r_log.Get_TX_Throughput_Common("UDP-UL-Tx","UL-11")))
#
#	logging.info("65537"+str(r_log.Get_DDDS_RCVD_Common('PDCP RX \[0\] STATISTICS',"65537")))
#	logging.info("65538"+str(r_log.Get_DDDS_RCVD_Common('PDCP TX \[0\] STATISTICS',"65538")))
#	logging.info("65539"+str(r_log.Get_DDDS_RCVD_Common('PDCP TX \[1\] STATISTICS',"65539")))
#	logging.info("65540"+str(r_log.Get_DDDS_RCVD_Common('PDCP TX \[2\] STATISTICS',"65540")))
#	logging.info("65541"+str(r_log.Get_DDDS_RCVD_Common('PDCP RX \[0\] STATISTICS',"65541")))
#	logging.info("65542"+str(r_log.Get_DDDS_RCVD_Common('PDCP RX \[0\] STATISTICS',"65542")))
