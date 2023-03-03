# 功能
|           |                                                                                   |                                                                                                                                 |          | 代码量  | 工时 |
| --------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------- | ------- | ---- |
| 1110      | 端末異常が発生し、iperfが途中で中断された場合にCI上でNGに見えない件の対応(見積り) | iperf 过程中，没有结果了，算NG（-t 10s 记录中要大于10）<br>-P 4 的情况下<br>-t 100<br>1 2 3 都100了<br>4 只有50 算NG吗？<br>算! |          |         | 20   | 0.5 |
| 1111 todo | iperf結果のグラフを端末毎にまとめて表示する(見積り)                               | 同一时间的图片，放在同一行                                                                                                      |          | Pipline | 15   | 0.5 |
|           |                                                                                   | 放在一张图上？                                                                                                                  |          | python  | 100  | 2   |
| 1112      | 外部スクリプト実行時のメッセージをJenkinsコンソールに表示する(見積り)             | 脚本，显示执行过程中的log                                                                                                       |          |         | 0    | 0   |
| 1113      | バッテリー残量表示のAction追加 (見積り)                                           | 根据情况获取电力（test case）                                                                                                   | 全部手机 | python  | 20   | 0.5 |
| 1114      | バッテリー残量表示コマンド発行でタイムアウトしてもAbortしないようにする(見積り)   | 电量获取失败，可以继续测试                                                                                                      |          |         | 5    | 0.5 |
| 1144 todo | ログ取得時に試験で使用したconfigとxmlを一緒に回収するようにする(見積り)           | log中config和xml 一起收集                                                                                                       |          | Pipline | 2    | 0.5 |
| 1145      | 複数シナリオ(xml)を指定、実行できるようにする(見積り)                             | ADB 允许接入多个ADB                                                                                                             |          | python  | 41   | 1   |


# 修改
环境 
151:/home/l5g/work_jftt/lu/L5G_CI_develop
```
diff --git a/Jenkins/Pipeline_parallel.txt b/Jenkins/Pipeline_parallel.txt
index f8298cb..9fa4595 100644
--- a/Jenkins/Pipeline_parallel.txt
+++ b/Jenkins/Pipeline_parallel.txt
@@ -79,7 +79,7 @@ pipeline {
                        currentBuild.result = 'FAILURE'
                        echo '\u2705 \u001B[32mLog Transfer (Jenkins)\u001B[0m'
                        sh "wget --no-proxy ${env.JENKINS_URL}/job/${env.JOB_NAME}/${env.BUILD_ID}/consoleText -O consoleText.log || true"
-                       sh "zip -m consoleText.log.${env.BUILD_ID}.zip consoleText.log || true"
+                       sh "zip -m -r consoleText.log.${env.BUILD_ID}.zip consoleText.log config.ini xml_files || true"
                        script {
                            if(fileExists("consoleText.log.${env.BUILD_ID}.zip")) {
                                archiveArtifacts "consoleText.log.${env.BUILD_ID}.zip"
@@ -216,6 +216,26 @@ pipeline {
                            archiveArtifacts "IperfPng/${filenameArray[1]}"
                            summary.appendText("<a href=\"${env.BUILD_URL}artifact/${path}\">${filenameArray[1]}</a><br/><img src=\"artifact/${path}\" height=\"400\" width=\"700\"><br />", false, false, false, "red")
                        }
+                   //  group = sh(returnStdout: true, script: "find IperfPng -name '*.png' | awk -F'_' '{print \$NF}' | awk -F'.' '{print \$1}' | sort | uniq")
+                   //  for (time in group.tokenize('\n')){
+                   //      summary = manager.createSummary("clipboard.gif")
+                   //      cmd = "find IperfPng -name *${time}.png"
+                   //      files=sh(returnStdout: true, script: cmd)
+                   //      //echo "${files}"
+                   //      for (path in files.tokenize('\n')){
+                   //          String[] filenameArray = path.split('/')
+                   //          //filename = filenameArray[1]
+                   //          //path = files.collectEntries
+                   //          //echo "${div_id} PATH: ${path}"
+                   //          //echo "${env.BUILD_URL}artifact/${path}"
+                   //          //echo "filename: ${filename}"
+                   //          //Groovy
+                   //          archiveArtifacts "IperfPng/${filenameArray[1]}"
+                   //          //summary.appendText("<a href=\"${env.BUILD_URL}artifact/${path}\"><img src=\"artifact/${path}\" height=\"400\" width=\"700\"></a>", false, false, false, "red")
+                   //          summary.appendText("<a href=\"${env.BUILD_URL}artifact/${path}\"><img src=\"artifact/${path}\" height=\"350\" width=\"400\"></a>", false, false, false, "red")
+                   //      }
+                   //      summary.appendText("<br />", false, false, false, "red")
+                   //  }
                        sh "rm -rf IperfPng"
                    }
                }
@@ -250,7 +270,7 @@ pipeline {
        always {
            echo '\u2705 \u001B[32mLog Transfer (Jenkins)\u001B[0m'
            sh "wget --auth-no-challenge --no-proxy ${env.JENKINS_URL}/job/${env.JOB_NAME}/${env.BUILD_ID}/consoleText -O consoleText.log || true"
-           sh "zip -m consoleText.log.${env.BUILD_ID}.zip consoleText.log || true"
+           sh "zip -m -r consoleText.log.${env.BUILD_ID}.zip consoleText.log config.ini xml_files || true"
            script {
                if(fileExists("consoleText.log.${env.BUILD_ID}.zip")) {
                    archiveArtifacts "consoleText.log.${env.BUILD_ID}.zip"
diff --git a/Python/SSHClass.py b/Python/SSHClass.py
index b3d77db..b146b11 100644
--- a/Python/SSHClass.py
+++ b/Python/SSHClass.py
@@ -274,13 +274,17 @@ class ADBSSHConnection(SSHConnection):
        self.open(self.ADBIPAddress, self.ADBUserName, self.ADBPassword, self.ADBPort)
        self.command('adb devices', '\$', 15)
        self.UEDevices = re.findall("\\\\r\\\\n([A-Za-z0-9]+)\\\\tdevice",str(self.ssh.before))
+       self.close()
+
+   def GetUEBattery(self):
        for device_id in self.UEDevices:
            self.command('stdbuf -o0 adb -s ' + device_id + ' shell dumpsys battery | grep level | awk \'{print $2}\'', '\$ ', 60)
            result = re.search('\\\\r\\\\n(?P<battery>\d+)\\\\r\\\\n', str(self.ssh.before))
-           battery = int(result.group('battery'))
-           logging.info("UE["+device_id+"] battery:"+str(battery))
-       self.close()
-   
+           if result is None:
+               logging.info('\u001B[1mUE (' + device_id + ') Get Battery Fail!' + '\u001B[0m')
+           else:
+               logging.info("UE["+device_id+"] battery: "+result.group('battery'))
+
 class APLADBSSHConnection(ADBSSHConnection):
    def __init__(self):
        super(APLADBSSHConnection, self).__init__()
diff --git a/Python/iperf.py b/Python/iperf.py
index 189b6e7..beb8a16 100644
--- a/Python/iperf.py
+++ b/Python/iperf.py
@@ -139,6 +139,7 @@ class Draw_PLT_Graph():
        #logging.info("y1: "+str(y1))
        #logging.info("y2: "+str(y2))
        #logging.info("y3: "+str(y3))
+       #logging.info(str(x) + ", " + str(y1) + ", \"" + y1_unit + "\", " + str(y2) + ", \"" + y2_unit + "\", " + str(y3) + ", \"" + y3_unit + "\"")
        return title, x, y1, y1_unit, y2, y2_unit, y3, y3_unit

    def SetYAsix(self, ax, y_asix_unit, set_max):
@@ -175,6 +176,7 @@ class Draw_PLT_Graph():
            y_list.append(data)
            y_labels.append(str('%.1f' % data)+y_asix_unit)
        ax.set_ylim(0, y_max+int(y_max/10))
+       #logging.info(str(y_list))
        ax.set_yticks(y_list)
        ax.set_yticklabels(y_labels, fontweight='ultralight')

@@ -258,10 +260,114 @@ class Draw_PLT_Graph():
        plt.savefig(png_name)
        plt.close()

+#######
    def Draw_Iperf_Graph(self, iperf_server_log_name):
-       title,x_datas, y1_datas, y1_unit, y2_datas, y2_unit, y3_datas, y3_unit = self.Get_Iperf_Data(iperf_server_log_name)
+       title, x_datas, y1_datas, y1_unit, y2_datas, y2_unit, y3_datas, y3_unit = self.Get_Iperf_Data(iperf_server_log_name)
        self.Draw_Graph(title + ' [' +  os.path.split(iperf_server_log_name)[1] + '] ', x_datas, y1_datas, y1_unit, y2_datas, y2_unit, y3_datas, y3_unit, os.path.splitext(iperf_server_log_name)[0]+'.png')

+   def Draw_Axes(self, axes, device, x_datas, y1_datas, y1_unit, y2_datas, y2_unit, y3_datas, y3_unit):
+       Throughput, = axes[0].plot(x_datas, y1_datas, color='black')
+       axes[0].legend([Throughput], ["Throughput"])
+       self.SetYAsix(axes[0], y1_unit, 0)
+       self.SetXAsix(axes[0], '', 1)
+       axes[0].set_xlabel('Time (s)')
+
+       if len(y2_datas) > 0 or len(y3_datas) > 0:
+           Jitter, = axes[1].plot(x_datas, y2_datas, label="Jitter", color='blue')
+           axes[1].legend([Jitter], ["Jitter"])
+           self.SetYAsix(axes[1], y2_unit, 1)
+           self.SetXAsix(axes[1], '', 1)
+           axes[1].set_xlabel('Time (s)')
+
+           Lost, = axes[2].plot(x_datas, y3_datas, label="Lost", color='red')
+           axes[2].legend([Lost], ["Lost"])
+           self.SetYAsix(axes[2], y3_unit, 100)
+           self.SetXAsix(axes[2], '', 1)
+           axes[2].set_xlabel('Time (s)')
+
+           axes[1].set_ylabel(device)
+       else:
+           axes[0].set_ylabel(device)
+
+#######
+   def Draw_Iperfs_Graph(self, name, iperf_server_log_names):
+       logging.info(str(iperf_server_log_names))
+       clon_num = len(iperf_server_log_names)
+       fig = plt.figure(dpi=120, figsize=(16*clon_num,9))
+       axes = []
+       clon_id = 1
+       for iperf_server_log_name in iperf_server_log_names:
+           iperf_server_log_name = iperf_server_log_name.strip('\n')
+           title, x_datas, y1_datas, y1_unit, y2_datas, y2_unit, y3_datas, y3_unit = self.Get_Iperf_Data(iperf_server_log_name)
+
+           axes.clear()
+           axes.append(fig.add_subplot(3, clon_num, 0*clon_num+clon_id))
+           axes.append(fig.add_subplot(3, clon_num, 1*clon_num+clon_id))
+           axes.append(fig.add_subplot(3, clon_num, 2*clon_num+clon_id))
+           plt.subplot(3, clon_num, 0*clon_num+clon_id)
+           plt.title(os.path.split(iperf_server_log_name)[1])
+           self.Draw_Axes(axes, x_datas, y1_datas, y1_unit, y2_datas, y2_unit, y3_datas, y3_unit)
+           clon_id = clon_id + 1
+
+       plt.subplots_adjust(hspace=.0)
+       plt.savefig(name + '.png')
+       plt.close()
+
+   def Draw_Iperfs_Graph_New(self, name, devices, files_list):
+       logging.info(name)
+       logging.info(str(devices))
+       logging.info(str(files_list))
+
+       device_num = len(devices)
+       clon_num = len(files_list[0])
+       fig = plt.figure(dpi=120, figsize=(16*clon_num,9*device_num))
+       axes = []
+       for device_id in range(device_num):
+           for clon_id in range(clon_num):
+               iperf_server_log_name = files_list[device_id][clon_id]
+               title, x_datas, y1_datas, y1_unit, y2_datas, y2_unit, y3_datas, y3_unit = self.Get_Iperf_Data(iperf_server_log_name)
+               axes.clear()
+               if len(y2_datas) > 0 or len(y3_datas) > 0:
+                   axes.append(fig.add_subplot(3*device_num+device_num-1, clon_num, (device_id*4+0)*clon_num+clon_id+1))#row, clon, id
+                   axes.append(fig.add_subplot(3*device_num+device_num-1, clon_num, (device_id*4+1)*clon_num+clon_id+1))
+                   axes.append(fig.add_subplot(3*device_num+device_num-1, clon_num, (device_id*4+2)*clon_num+clon_id+1))
+                   plt.subplot(3*device_num+device_num-1, clon_num, (device_id*4+0)*clon_num+clon_id+1)
+                   plt.title(os.path.split(iperf_server_log_name)[1])
+               else:
+                   axes.append(fig.add_subplot(device_num+device_num-1, clon_num, (device_id*2)*clon_num+clon_id+1))#row, clon, id
+                   #axes.append(fig.add_subplot(device_num+device_num-1, clon_num, (device_id+1)*clon_num+clon_id+1))
+                   #axes.append(fig.add_subplot(device_num+device_num-1, clon_num, (device_id+2)*clon_num+clon_id+1))
+                   plt.subplot(device_num+device_num-1, clon_num, (device_id*2)*clon_num+clon_id+1)
+                   plt.title(os.path.split(iperf_server_log_name)[1])
+               logging.info(str(axes))
+               self.Draw_Axes(axes, devices[device_id], x_datas, y1_datas, y1_unit, y2_datas, y2_unit, y3_datas, y3_unit)
+       plt.subplots_adjust(hspace=.0)
+       plt.savefig(name + '.png')
+       plt.close()
+
+   def nextDraw_Iperfs_Graph_New(self, name, iperf_server_log_names):
+       logging.info(str(iperf_server_log_names))
+       clon_num = len(iperf_server_log_names)
+       fig = plt.figure(dpi=120, figsize=(16*clon_num,9))
+       axes = []
+       clon_id = 1
+       for iperf_server_log_name in iperf_server_log_names:
+           iperf_server_log_name = iperf_server_log_name.strip('\n')
+           title, x_datas, y1_datas, y1_unit, y2_datas, y2_unit, y3_datas, y3_unit = self.Get_Iperf_Data(iperf_server_log_name)
+
+           axes.clear()
+           axes.append(fig.add_subplot(3, clon_num, 0*clon_num+clon_id))
+           axes.append(fig.add_subplot(3, clon_num, 1*clon_num+clon_id))
+           axes.append(fig.add_subplot(3, clon_num, 2*clon_num+clon_id))
+           plt.subplot(3, clon_num, 0*clon_num+clon_id)
+           plt.title(os.path.split(iperf_server_log_name)[1])
+           self.Draw_Axes(axes, x_datas, y1_datas, y1_unit, y2_datas, y2_unit, y3_datas, y3_unit)
+           clon_id = clon_id + 1
+
+       plt.subplots_adjust(hspace=.0)
+       plt.savefig(name + '.png')
+       plt.close()
+
 class IperfClass(SSHClass.APLADBSSHConnection):
    def __init__(self):
        super(IperfClass, self).__init__()
@@ -376,12 +482,33 @@ class IperfClass(SSHClass.APLADBSSHConnection):
            if thread_num > 1:
                self.command('cat ' + iperf_server_log_name + ' | grep SUM | grep sec | awk  -F[-\' \']+ \'BEGIN{falg=0}{if($8<='+self.iperf_service_packetloss_threshold+'){falg++;}else{falg = 0;}if(falg>'+self.iperf_service_packetloss_count+'){print falg;}}\' | wc -l', '\$ ', 5)
            else:
+               thread_num = 1
                self.command('cat ' + iperf_server_log_name + ' | grep sec | awk  -F[-\' \']+ \'BEGIN{falg=0}{if($8<='+self.iperf_service_packetloss_threshold+'){falg++;}else{falg = 0;}if(falg>'+self.iperf_service_packetloss_count+'){print falg;}}\' | wc -l', '\$ ', 5)
        else:
            self.command('cat ' + iperf_server_log_name + ' | grep sec | awk  -F[-\' \']+ \'BEGIN{falg=0}{if($8<='+self.iperf_service_packetloss_threshold+'){falg++;}else{falg = 0;}if(falg>'+self.iperf_service_packetloss_count+'){print falg;}}\' | wc -l', '\$ ', 5)
        result = re.search('\\\\r\\\\n(?P<error_num>\d+)\\\\r\\\\n', str(self.ssh.before))
        error_num = int(result.group('error_num'))

+       #check iperf time
+       result = re.search('-t (?P<iperf_time>\d+)', str(iperf_args))
+       if result is None:
+           message = 'Iperf time Not Found!'
+           logging.info('\u001B[1;37;41m ' + message + ' \u001B[0m')
+           os.system("echo \"        Iperf Param Error : " + message + "\" >> test_error_result.log")
+           return message,iperf_dlul,iperf_type,server_option,client_option
+
+       iperf_time = result.group('iperf_time')
+       for thread_id in range(thread_num):
+           self.command('grep -E "' + str(thread_id) + '\]( )+0(.0+)?( )?-( )?" ' + iperf_server_log_name + ' | grep % | tail -1', '\$ ', 5)
+           result = re.search('[0.]+\-(?P<run_time>[\d.]+) sec', str(self.ssh.before))
+           if result is None:
+               run_time = 0
+           else:
+               run_time = float(result.group('run_time'))
+       if run_time < iperf_time:
+           message = 'Iperf not finish!'
+           logging.info('\u001B[1;37;41m ' + message + ' \u001B[0m')
+
        #check iperf result info
        if 'udp' == iperf_type:
            self.command('grep -E "\]( )+0(.0+)?( )?-( )?" ' + iperf_server_log_name + ' | grep -v -E "\]( )+0(.0+)?( )?-( )?[01].0+ " | grep % | grep -v "SUM" | awk -F"[ /-]+" \'BEGIN{Transfer=0;Bandwidth=0;Jitter=0;Lost=0;Total=0}{Transfer+=$6;Bandwidth+=$8;if($11>Jitter){Jitter=$11};Lost+=$13;Total+=$14;print Transfer,Bandwidth,Jitter,Lost,Total;}END{print Transfer,$7,Bandwidth,$9"/"$10,Jitter,$12,(Total-Lost)/Total*100"%"}\'', '\$ ', 5)
@@ -599,8 +726,28 @@ class IperfClass(SSHClass.APLADBSSHConnection):
            message = status_queue.get()

    def TerminateIperf(self):
+       logging.debug("Kill all iperf process in APL and UE")
+       for group_id in range(len(self.ADBGroupIPAddress)):
+           self.ADBIPAddress = self.ADBGroupIPAddress[group_id]
+           self.ADBPort = self.ADBGroupPort[group_id]
+           self.ADBUserName = self.ADBGroupUserName[group_id]
+           self.ADBPassword = self.ADBGroupPassword[group_id]
+           self.open(self.ADBIPAddress, self.ADBUserName, self.ADBPassword, self.ADBPort)
+           self.command('stdbuf -o0 echo ' + self.ADBPassword + ' | killall -KILL iperf || true', '\$', 5)
+           time.sleep(2)
+           self.command('stdbuf -o0 ps -aux | grep -v grep | grep iperf', '\$', 5)
+           result = re.search('iperf', str(self.ssh.before))
+           if result is not None:
+               self.command('stdbuf -o0 echo ' + self.ADBPassword + ' | killall -KILL iperf || true', '\$', 5)
+           self.close()
+
        self.open(self.APLIPAddress, self.APLUserName, self.APLPassword, self.APLPort)
-       self.command('stdbuf -o0 echo ' + self.APLPassword + ' | sudo -S killall -KILL iperf', '\$', 5)
+       self.command('stdbuf -o0 echo ' + self.APLPassword + ' | killall -KILL iperf || true', '\$', 5)
+       time.sleep(2)
+       self.command('stdbuf -o0 ps -aux | grep -v grep | grep iperf', '\$', 5)
+       result = re.search('iperf', str(self.ssh.before))
+       if result is not None:
+           self.command('stdbuf -o0 echo ' + self.APLPassword + ' | killall -KILL iperf || true', '\$', 5)
        self.close()

    def LogCollectIperf(self):
@@ -611,6 +758,7 @@ class IperfClass(SSHClass.APLADBSSHConnection):
        os.system("mkdir -p " + destination)
        self.MoveFileToLocal(self.APLIPAddress, self.APLUserName, self.APLPassword, self.APLPort, os.path.join(self.APLSourceCodePath, "tcp_iperf*.log"), destination)

+       #old
        file_list = ["IperfLog/APL_TCP_Iperf_Log/", "IperfLog/APL_UDP_Iperf_Log/"]
        for group_id in range(len(self.ADBGroupIPAddress)):
            self.ADBIPAddress = self.ADBGroupIPAddress[group_id]
@@ -637,8 +785,54 @@ class IperfClass(SSHClass.APLADBSSHConnection):
                    dpg.Draw_Iperf_Graph(path + line.strip('\n'))
                    os.system('cp ' + path + line[0:-5] +'.png IperfPng')
            p.close()
+       # new 1
+       p = os.popen("find IperfLog -name '*_server_*.log' | awk -F'[._/]' '{if(\"APL\"==$2){print $12}else{print $13}}' | sort | uniq", 'r', 1)
+       for device_id in p.readlines():
+           device_id = device_id.strip('\n')
+           cmd = "find IperfLog -name '*_server_*" + device_id + "*.log' | awk -F'[._/]' '{if(\"APL\"==$2){print $13,$8,$0}else{print $15,$9,$0}}' | sort | awk '{print $NF}'"
+           logging.info(cmd)
+           p1 = os.popen(cmd, 'r', 1)
+           dpg.Draw_Iperfs_Graph(device_id, p1.readlines())
+           os.system('mv ' + device_id + '.png IperfPng')
+           p1.close()
+       p.close()

-       os.system("zip -r iperf.log." + self.build_id + ".zip IperfLog")
+       # new 2
+       cmd = "find IperfLog -name '*_server_*.log' | awk -F'[._]' '{print $(NF-1)}' | sort | uniq"
+       #cmd = "find IperfLog -name '*_server_*.log' | grep TCP | awk -F'[._]' '{print $(NF-1)}' | sort | uniq"
+       #logging.info(cmd)
+       p0 = os.popen(cmd, 'r', 1)
+       files_list = []
+       for time in p0.readlines():
+           time = time.strip('\n')
+           devices = []
+           files_list.clear()
+           cmd = "find IperfLog -name '*_server_*" + time + ".log' | awk -F'[._/]' '{if(\"APL\"==$2){print $12}else{print $13}}' | sort | uniq"
+           #logging.info(cmd)
+           p1 = os.popen(cmd, 'r', 1)
+           for device_id in p1.readlines():
+               device_id = device_id.strip('\n')
+               devices.append(device_id)
+               cmd = "find IperfLog -name '*_server_*" + device_id + "*" + time + ".log' | awk -F'[._/]' '{if(\"APL\"==$2){print $13,$8,$0}else{print $15,$9,$0}}' | sort | awk '{print $NF}'"
+               #logging.info(cmd)
+               p2 = os.popen(cmd, 'r', 1)
+               files = []
+               for file in p2.readlines():
+                   files.append(file.strip('\n'))
+               p2.close()
+               files_list.append(files)
+           p1.close()
+
+           cmd = "find IperfLog -name '*_server_*" + time + ".log' | awk -F'[._/]' '{if(\"APL\"==$2){print \"_\"$3\"_\"$10}else{print \"_\"$4\"_\"$11}}' | uniq"
+           #logging.info(cmd)
+           p1 = os.popen(cmd, 'r', 1)
+           name = time + p1.readline().strip('\n')
+           p1.close()
+           dpg.Draw_Iperfs_Graph_New(name, devices, files_list)
+           os.system('mv ' + name + '.png IperfPng')
+       p0.close()
+
+       os.system("zip -r iperf.log." + self.build_id + ".zip IperfLog IperfPng")
        os.system("rm -rf IperfLog")

 def Usage():
@@ -764,4 +958,5 @@ elif mode == 'LOG':
    Case.ADBGroupPort = Case.ADBPort.split(',')
    Case.ADBGroupUserName = Case.ADBUserName.split(',')
    Case.ADBGroupPassword = Case.ADBPassword.split(',')
+   Case.TerminateIperf()
    Case.LogCollectIperf()
diff --git a/Python/main.py b/Python/main.py
index ec4dede..501d108 100755
--- a/Python/main.py
+++ b/Python/main.py
@@ -205,22 +205,17 @@ class CI_Config():

        return IPAddressGroup, PortGroup, UserNameGroup, PasswordGroup, SourceCodePath

-   def Get_Xml_Conf(self, device, id):
+   def Get_Xml_Conf(self, device):
        section = device + '_Service_Info'
        XmlFile = self.conf.get(section, 'XmlFile')
+       XmlFiles = []
        if XmlFile == '':
-           logging.info(' No ' + device + ' Xml File')
+           logging.info(device + ' need set Xml File')
        elif ',' in XmlFile:
            XmlFiles = XmlFile.split(',')
-           xml_num = len(XmlFiles)
-           if id<0 or xml_num == 1:
-               XmlFile = XmlFiles
-           elif id >= xml_num:
-               logging.info('ADB (' + str(id) + ') No Xml File')
-               XmlFile = ''
-           else:
-               XmlFile = XmlFiles[id]
-       return XmlFile
+       else:
+           XmlFiles.append(XmlFile)
+       return XmlFiles

    def Get_Log_Conf(self, name):
        result = self.conf.get('LogCtl', name)
@@ -1352,17 +1347,12 @@ APLActionParam = " --APLIPAddress=" + CICase.APLIPAddress + " --APLUserName=" +
 if '' != CICase.APLPort:
    APLActionParam += " --APLPort=" + CICase.APLPort

-ADBGroupIPAddress, ADBGroupPort, ADBGroupUserName, ADBGroupPassword, CICase.ADBSourceCodePath = Config.Get_Device_Group_Conf('ADB')
-testXMLfiles = Config.Get_Xml_Conf('ADB', adb_group_id)
+ADBIPAddress, ADBPort, ADBUserName, ADBPassword, ADBSourceCodePath = Config.Get_Device_Conf('ADB_' + ADBGroupID)
+testXMLfilesList = Config.Get_Xml_Conf('ADB_' + ADBGroupID)
 # for ping LOG & iperf Log
-ADBIPAddress_Array_Str = ArrayToStr(ADBGroupIPAddress)
-ADBUserName_Array_Str = ArrayToStr(ADBGroupUserName)
-ADBPassword_Array_Str = ArrayToStr(ADBGroupPassword)
-ADBPort_Array_Str = ArrayToStr(ADBGroupPort)
-ADBActionParam = " --ADBIPAddress=" + ADBGroupIPAddress[adb_group_id] + " --ADBUserName=" + ADBGroupUserName[adb_group_id] + " --ADBPassword=" + ADBGroupPassword[adb_group_id]
-if '' != ADBGroupPort[adb_group_id]:
-   ADBActionParam += " --ADBPort=" + ADBGroupPort[adb_group_id]
-AllADBActionParam = " --ADBIPAddress=" + ADBIPAddress_Array_Str + " --ADBUserName=" + ADBUserName_Array_Str + " --ADBPassword=" + ADBPassword_Array_Str + " --ADBPort=" + ADBPort_Array_Str
+ADBActionParam = " --ADBIPAddress=" + ADBIPAddress + " --ADBUserName=" + ADBUserName + " --ADBPassword=" + ADBPassword
+if '' != ADBPort:
+   ADBActionParam += " --ADBPort=" + ADBPort

 TTLIPAddress, TTLPort, TTLUserName, TTLPassword, TTLSourceCodePath = Config.Get_Device_Conf('TTL')
 TTLMovePath = Config.Get_Common_Conf('TTL_Service_Info', 'MovePath') + '\\' + CICase.job_name + '\\' + CICase.build_id
@@ -1387,6 +1377,25 @@ SimNovatorEmail = Config.Get_Common_Conf('SimNovator_Info', 'CredintialsEmail')
 SimNovatorPassword = Config.Get_Common_Conf('SimNovator_Info', 'CredintialsPassword')
 SimNovatorActionParam = " --URL=" + SimNovatorURL + " --Email=" + SimNovatorEmail + " --Password=" + SimNovatorPassword

+AllADBActionParam = ""
+if re.match('^LogCollectPing$', mode, re.IGNORECASE) or re.match('^LogCollectIperf$', mode, re.IGNORECASE):
+   ADBGroupIPAddress = []
+   ADBGroupUserName = []
+   ADBGroupPassword = []
+   ADBGroupPort = []
+   for adb_id in range(8):
+       if config.has_section('ADB_0' + str(adb_id) + '_Service_Info'):
+           tmp_ADBIPAddress, tmp_ADBPort, tmp_ADBUserName, tmp_ADBPassword, CICase.tmp_ADBSourceCodePath = Config.Get_Device_Conf('ADB_0' + str(adb_id))
+           ADBGroupIPAddress.append(tmp_ADBIPAddress)
+           ADBGroupUserName.append(tmp_ADBUserName)
+           ADBGroupPassword.append(tmp_ADBPassword)
+           ADBGroupPort.append(tmp_ADBPort)
+   ADBIPAddress_Array_Str = ArrayToStr(ADBGroupIPAddress)
+   ADBUserName_Array_Str = ArrayToStr(ADBGroupUserName)
+   ADBPassword_Array_Str = ArrayToStr(ADBGroupPassword)
+   ADBPort_Array_Str = ArrayToStr(ADBGroupPort)
+   AllADBActionParam = " --ADBIPAddress=" + ADBIPAddress_Array_Str + " --ADBUserName=" + ADBUserName_Array_Str + " --ADBPassword=" + ADBPassword_Array_Str + " --ADBPort=" + ADBPort_Array_Str
+
 if re.match('^LogCollectPing$', mode, re.IGNORECASE):
    cmd = "python3 ping.py --mode=LOG " + APLActionParam + AllADBActionParam + " --BulidID=" + CICase.build_id
    logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
@@ -1438,338 +1447,345 @@ elif re.match('^TestL5G$', mode, re.IGNORECASE):
        if innerlogFlag == 'true':
            CICase.Prepare_TTL_Connect_Environment(TTLIPAddress, TTLUserName, TTLPassword)

-   xml_test_file = sys.path[0] + "/" + testXMLfiles
-   xmlTree = ET.parse(xml_test_file)
-   xmlRoot = xmlTree.getroot()
-   requested_tests=xmlRoot.findtext('TestCaseRequestedList',default='')
-   if "EMS" in requested_tests:
-       if WinEMSIPAddress != '' and WinEMSUserName != '' and WinEMSPassword != '':
-           CICase.UploadFile(WinEMSIPAddress, WinEMSUserName, WinEMSPassword, WinEMSPort, "ems_selenium.py", WinEMSSourceCodePath.replace("\\", "/")+"/src")
-           CICase.UploadFile(WinEMSIPAddress, WinEMSUserName, WinEMSPassword, WinEMSPort, "ems_pyautogui.py ", WinEMSSourceCodePath.replace("\\", "/")+"/src")
-
-   requested_tests=requested_tests.split()
-   TestCaseFile = get_test_case_name('/','.',testXMLfiles)
-
-   #get the list of tests to be done
-   for action in requested_tests:
-       logging.info('INFO: test will be run: ' + action)
-   signal.signal(signal.SIGUSR1, receive_signal)
-
-   if "Change_L5GC_Environment" in requested_tests or "CheckCUDUStatus" in requested_tests:
-       CICase.Update_Act_L5GC()
-
-   for action in requested_tests:
-       testCase_id = action
-       ShowTestID(TestCaseFile, testCase_id)
-       if 'Initialize_UE' == action:
-           cmd = "python3 ueaction.py --mode=Initialize" + ADBActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'Attach_' == action[0:len('Attach_')]:
-           UECount = action[action.index('_')+1:action.rindex('_')]
-           cmd = "python3 ueaction.py --mode=Attach --UECount=" + UECount + ADBActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'Detach_UE' == action:
-           cmd = "python3 ueaction.py --mode=Detach" + ADBActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'Ping_DL_' == action[0:len('Ping_DL_')]:
-           ping_args, ping_packetloss_threshold, ping_rttmax_threshold = Config.Get_Ping_Conf(ADBGroupID, action)
-           cmd = "python3 ping.py --mode=DL" + APLActionParam + ADBActionParam + " --args=\"" + ping_args + "\" --packetloss_threshold=" + ping_packetloss_threshold + " --rttmax_threshold=" + ping_rttmax_threshold
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'Ping_UL_' == action[0:len('Ping_UL_')]:
-           ping_args, ping_packetloss_threshold, ping_rttmax_threshold = Config.Get_Ping_Conf(ADBGroupID, action)
-           cmd = "python3 ping.py --mode=UL" + ADBActionParam + " --args=\"" + ping_args + "\" --packetloss_threshold=" + ping_packetloss_threshold + " --rttmax_threshold=" + ping_rttmax_threshold
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'UDP_Iperf_DL_' == action[0:len('UDP_Iperf_DL_')] or 'UDP_Iperf_UL_' == action[0:len('UDP_Iperf_UL_')]:
-           iperf_args, iperf_packetloss_threshold, iperf_service_packetloss_count, iperf_service_packetloss_threshold = Config.Get_UDP_Iperf_Conf(ADBGroupID, action)
-           cmd = "python3 iperf.py --mode=UDP_" + action[len('UDP_Iperf_'):len('UDP_Iperf_DL')] + APLActionParam + ADBActionParam + " --iperf_port=" + iperf_port + " --args=\"" + iperf_args + "\" --packetloss_threshold=" + iperf_packetloss_threshold + " --service_packetloss_count=" + iperf_service_packetloss_count + " --service_packetloss_threshold=" + iperf_service_packetloss_threshold
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'UDP_Iperf_DLUL_' == action[0:len('UDP_Iperf_DLUL_')]:
-           iperf_args_dl, iperf_args_ul, iperf_packetloss_threshold = Config.Get_UDP_DLUL_Iperf_Conf(ADBGroupID, action)
-           cmd = "python3 iperf.py --mode=UDP_DLUL" + APLActionParam + ADBActionParam + " --iperf_port=" + iperf_port + " --dl_args=\"" + iperf_args_dl + "\" --ul_args=\"" + iperf_args_ul + "\" --packetloss_threshold=" + iperf_packetloss_threshold
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'TCP_Iperf_DL_' == action[0:len('TCP_Iperf_DL_')] or 'TCP_Iperf_UL_' == action[0:len('TCP_Iperf_UL_')]:
-           iperf_args = Config.Get_TCP_Iperf_Conf(ADBGroupID, action)
-           cmd = "python3 iperf.py --mode=TCP_" + action[len('TCP_Iperf_'):len('TCP_Iperf_DL')] + APLActionParam + ADBActionParam + " --iperf_port=" + iperf_port + " --args=\"" + iperf_args + "\""
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'TCP_Iperf_DLUL_' == action[0:len('TCP_Iperf_DLUL_')]:
-           iperf_args_dl, iperf_args_ul = Config.Get_TCP_DLUL_Iperf_Conf(ADBGroupID, action)
-           cmd = "python3 iperf.py --mode=TCP_DLUL" + APLActionParam + ADBActionParam + " --iperf_port=" + iperf_port + " --dl_args=\"" + iperf_args_dl + "\" --ul_args=\"" + iperf_args_ul + "\""
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'Terminate_All' == action:
-           CICase.TerminateAll()
-       elif 'Detach_Attach' == action:
-           CICase.Detach_Attach()
-       elif 'Terminate_Ping' == action:
-           CICase.TerminatePing()
-       elif 'Terminate_Iperf' == action:
-           CICase.TerminateIperf()
-       elif 'CollectDULogOpen' == action:
-           CICase.CollectDULogOpen()
-       elif 'CollectDULogOpen_nocyc' == action:
-           CICase.CollectDULogOpen_nocyc()
-       elif 'CollectDULogClose' == action:
-           CICase.CollectDULogClose()
-       elif 'Change_L5GC_Environment' == action:
-           if (-1 == CICase.Change_L5GC_ACT_SBY_Environment()):
-               is_NG = 1
-       elif 'Update_Config_' == action[0:len('Update_Config_')]:
-           del Config
-           conf_file = action[len('Update_Config_'):len(action)]+'.ini'
-           logging.info("Cat "+conf_file)
-           logging.info("-------------------------------------------------")
-           #res = subprocess.Popen("cat "+conf_file, stdout=subprocess.PIPE, shell=True)
-           #for line in res.stdout.readlines():
-           #   print(line.decode("utf-8").strip())
-           os.system('cat '+conf_file)
-           logging.info("-------------------------------------------------")
-           Config = CI_Config(conf_file)
-       elif 'Check_IsLock_' == action[0:len('Check_IsLock_')]:
-           device = action[len('Check_IsLock_'):len(action)]
-           CICase.CheckCUDUStatus("ActionCheck", device, "LOCK")
-       elif 'Check_IsUnlock_' == action[0:len('Check_IsUnlock_')]:
-           device = action[len('Check_IsUnlock_'):len(action)]
-           CICase.CheckCUDUStatus("ActionCheck", device, "UNLOCKED")
-       elif 'EMS_Lock_And_Check_' == action[0:len('EMS_Lock_And_Check_')]:
-           device = action[len('EMS_Lock_And_Check_'):len(action)]
-           DeviceName = CICase.GetCUDUDeviceName(device)
-           if '' == DeviceName:
-               logging.info('ERROR: wrong class ' + action)
-               continue
-           # Check Status
-           if 1 == CICase.CheckCUDUStatus("BaseCheck", device, "LOCK"):
-               continue
-           # Lock
-           cmd = "python3 ems.py --mode=Lock --DeviceName=" + DeviceName + WinEMSActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-           # Check Lock Result
-           CICase.CheckCUDUStatus("ActionCheck", device, "LOCK")
-       elif 'EMS_Unlock_And_Check_' == action[0:len('EMS_Unlock_And_Check_')]:
-           device = action[len('EMS_Unlock_And_Check_'):len(action)]
-           DeviceName = CICase.GetCUDUDeviceName(device)
-           if '' == DeviceName:
-               logging.info('ERROR: wrong class ' + action)
-               continue
-           # Check Status
-           if 1 == CICase.CheckCUDUStatus("BaseCheck", device, "UNLOCKED"):
-               continue
-           # Unlock
-           cmd = "python3 ems.py --mode=Unlock --DeviceName=" + DeviceName + WinEMSActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-           # Check unlock Result
-           CICase.CheckCUDUStatus("ActionCheck", device, "UNLOCKED")
-       elif 'EMS_IsEnabled_' == action[0:len('EMS_IsEnabled_')]:
-           DeviceName = CICase.GetCUDUDeviceName(action[len('EMS_IsEnabled_'):len(action)])
-           if '' == DeviceName:
-               logging.info('ERROR: wrong class ' + action)
-               continue
-           cmd = "python3 ems.py --mode=IsEnabled --DeviceName=" + DeviceName + WinEMSActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'EMS_IsDisabled_' == action[0:len('EMS_IsDisabled_')]:
-           DeviceName = CICase.GetCUDUDeviceName(action[len('EMS_IsDisabled_'):len(action)])
-           if '' == DeviceName:
-               logging.info('ERROR: wrong class ' + action)
-               continue
-           cmd = "python3 ems.py --mode=IsDisabled --DeviceName=" + DeviceName + WinEMSActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       #elif 'EMS_Config_Update_' == action[0:len('EMS_Config_Update_')]:
-       #   DeviceName = CICase.GetCUDUDeviceName(action[len('EMS_Config_Update_'):len(action)])
-       #   PacketPath = Config.Get_Common_Conf(action, 'PacketPath')
-       #   cmd = "python3 ems.py --mode=Config --DeviceName=" + DeviceName + " --Packet=" + PacketPath + WinEMSActionParam
-       #   logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-       #   p = os.popen(cmd,'r',1)
-       #   p.close()
-       #l5GC
-       # elif 'EMS_Config_Update' == action:
-       #   DeviceName = CICase.L5GC_CenterVMNodeName
-       #   PacketPath = Config.Get_Common_Conf(action, 'PacketPath')
-       #   cmd = "python3 ems.py --mode=Config --DeviceName=" + DeviceName + " --Packet=" + PacketPath + WinEMSActionParam
-       #   logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-       #   p = os.popen(cmd,'r',1)
-       #   p.close()
-       # elif 'EMS_Config_Change_' == action[0:len('EMS_Config_Change_')]:
-       #   ConfigFile = action[len('EMS_Config_Change_'):len(action)] + '.yaml'
-       #   DeviceName = CICase.L5GC_CenterVMNodeName
-       #   ParamValue = Config.Get_Common_Conf(action, 'ParamValue')
-       #   cmd = "python3 ems.py --mode=Config --DeviceName=" + DeviceName + " --ConfigFile=" + ConfigFile + " --ParamValue=" + ParamValue + WinEMSActionParam
-       #   logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-       #   p = os.popen(cmd,'r',1)
-       #   p.close()
-       elif 'EMS_Update_CU_' == action[0:len('EMS_Update_CU_')]:
-           DeviceType = 'CU'
-           UpdatePacket = Config.Get_Common_Conf(action, 'UpdatePacketPath')
-           ConfigPacket = Config.Get_Common_Conf(action, 'ConfigPacketPath')
-           DeviceName = CICase.GetCUDUDeviceName('CU')
-           cmd = "python3 ems.py --mode=Update --DeviceType=" + DeviceType + " --DeviceName=" + DeviceName + " --UpdatePacket=\"" + UpdatePacket + "\" --ConfigPacket=\"" + ConfigPacket + "\"" + WinEMSActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'EMS_Update_DU_' == action[0:len('EMS_Update_DU_')]:
-           DeviceType = 'DU'
-           UpdatePacket = Config.Get_Common_Conf(action, 'UpdatePacketPath')
-           ConfigPacket = Config.Get_Common_Conf(action, 'ConfigPacketPath')
-           DeviceName = ''
-           for group_id in range(len(CICase.DUGroupIPAddress)):
-               CICase.DUIPAddress = CICase.DUGroupIPAddress[group_id]
-               CICase.DUPort = CICase.DUGroupPort[group_id]
-               CICase.DUUserName = CICase.DUGroupUserName[group_id]
-               CICase.DUPassword = CICase.DUGroupPassword[group_id]
-               CICase.SaveDUrHUBInfo('DU'+str(group_id+1) + "_Before_Update")
-               if group_id > 0:
-                   DeviceName = DeviceName + ','
-               DeviceName = DeviceName + CICase.GetCUDUDeviceName('DU'+str(group_id+1))
-           cmd = "python3 ems.py --mode=Update --DeviceType=" + DeviceType + " --DeviceName=" + DeviceName + " --UpdatePacket=\"" + UpdatePacket + "\" --ConfigPacket=\"" + ConfigPacket + "\"" + WinEMSActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-           logging.info("Wait DU restart (5min) ...")
-           time.sleep(300)
-           for group_id in range(len(CICase.DUGroupIPAddress)):
-               CICase.SaveDUrHUBInfo('DU'+str(group_id) + "_After_Update")
-       elif 'Delete_IMSI_' == action[0:len('Delete_IMSI_')]:
-           IMSI = Config.Get_Common_Conf(action, 'IMSI')
-           Args = Config.Get_Common_Conf(action, 'Args')
-           CICase.Delete_IMSI(IMSI, Args)
-       elif 'Add_IMSI_' == action[0:len('Add_IMSI_')]:
-           IMSI = Config.Get_Common_Conf(action, 'IMSI')
-           Args = Config.Get_Common_Conf(action, 'Args')
-           CICase.Add_IMSI(IMSI, Args)
-       elif "Get_IMSI_List" == action:
-           SSH.Get_All_IMSI_Status()
-       elif "Get_Connected_IMSI_List" == action:
-           IMSIArray = Config.Get_Common_Conf('IMSI_List', 'List').split(",")
-           SSH.Check_IMSI_Status(IMSIArray, "CONN")
-       elif "Get_Idle_IMSI_List" == action:
-           IMSIArray = Config.Get_Common_Conf('IMSI_List', 'List').split(",")
-           SSH.Check_IMSI_Status(IMSIArray, "IDLE")
-       elif 'Area_Stop_' == action[0:len('Area_Stop_')]:
-           #Area_Stop('amf')
-           #Area_Stop('smf')
-           CICase.Area_Stop(action[len('Area_Stop_'):len(action)].lower)
-       elif 'CU_Stop_' == action[0:len('CU_Stop_')]:
-           #CU_docker_Stop("cu_cp")
-           #CU_docker_Stop("cu_oam")
-           CICase.CU_docker_Stop('cu_'+action[len('CU_Stop_'):len(action)].lower)
-       elif 'DU_Stop_' == action[0:len('DU_Stop_')]:
-           #DU_docker_Stop("du_rlc_mac")
-           #DU_docker_Stop("du_scd")
-           #DU_docker_Stop("du_oam")
-           #DU_docker_Stop("du_oam_if")
-           CICase.DU_docker_Stop('du_'+action[len('DU_Stop_'):len(action)].lower)
-       elif 'DU_Stop_Process_' == action[0:len('DU_Stop_Process_')]:
-           CICase.DU_Process_Stop(action[len('DU_Stop_Process_'):len(action)])
-       #Not need
-       #elif 'EMS_Fault_Clear' == action:
-       #   EMS_Fault_Clear()
-       elif 'PerformPy_' == action[0:len('PerformPy_')] or 'PerformSh_' == action[0:len('PerformSh_')]:
-           Script = action[action.index('_')+1:action.rindex('_')] + '.' + action[len('Perform'):len('Perform')+2].lower()
-           IPAddress, Port, UserName, Password, ScriptPath, Args, FinishFlag, WaitFinish= Config.Get_Perform_Conf(action)
-           CICase.Perform(IPAddress, Port, UserName, Password, ScriptPath, Script, Args, FinishFlag, WaitFinish)
-       elif "Simnovator_Execute_" == action[0:len('Simnovator_Execute_')]:
-           TestCase = action[len('Simnovator_Execute_'):len(action)]
-
-           # Execute Case
-           cmd = "python3 simnovator.py --mode=Execute --TestCase=" + TestCase + SimNovatorActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-
-           # Start Monitor
-           cmd = "python3 simnovator.py --mode=Monitor --TestCase=" + TestCase + SimNovatorActionParam + " &"
-           logging.info(cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif "Simnovator_Stop_" == action[0:len('Simnovator_Stop_')]:
-           TestCase = action[len('Simnovator_Stop_'):len(action)]
-
-           # Stop Monitor
-           cmd = "kill -9 `ps -aux | grep \"python3 simnovator.py --Action=Monitor --TestCase=" + TestCase + "\" |grep -v grep |awk '{print $2}'`"
-           logging.info(cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-
-           # Stop Case
-           cmd = "python3 simnovator.py --mode=Stop --TestCase=" + TestCase + SimNovatorActionParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'CheckCUDUStatus' == action:
-           CICase.Check_CU_DU_Free5GC_Status()
-       elif 'LogCollect' == action:
-           DUIPAddress_Array_Str = ArrayToStr(CICase.DUGroupIPAddress)
-           DUUserName_Array_Str = ArrayToStr(CICase.DUGroupUserName)
-           DUPassword_Array_Str = ArrayToStr(CICase.DUGroupPassword)
-           DUPort_Array_Str = ArrayToStr(CICase.DUGroupPort)
-           CriticalLogParam = " --EMSIPAddress=" + CICase.EMSIPAddress + " --EMSUserName=" + CICase.EMSUserName + " --EMSPassword=" + CICase.EMSPassword + " --EMSSourceCodePath=\"" + CICase.EMSSourceCodePath + "\" --CUIPAddress=" + CICase.CUIPAddress + " --CUUserName=" + CICase.CUUserName + " --CUPassword=" + CICase.CUPassword + " --DUIPAddress=" + DUIPAddress_Array_Str + " --DUUserName=" + DUUserName_Array_Str + " --DUPassword=" + DUPassword_Array_Str + " --DUPort=" + DUPort_Array_Str + " --CenterVMIPAddress=" + CICase.L5GC_CenterVMIPAddress + " --CenterVMUserName=" + CICase.L5GC_CenterVMUserName + " --CenterVMPassword=" + CICase.L5GC_CenterVMPassword + " --CenterVMSourceCodePath=" + CICase.L5GC_CenterVMSourceCodePath + " --MountIPAddress=" + MountIPAddress + " --MountUserName=" + MountUserName + " --MountPassword=" + MountPassword + " --MountSourceCodePath=" + MountSourceCodePath + " --MountMovePath=" + MountMovePath
-           if '' != CICase.EMSPort:
-               CriticalLogParam += " --EMSPort=" + CICase.EMSPort
-           if '' != CICase.CUPort :
-               CriticalLogParam +=" --CUPort=" + CICase.CUPort
-           if '' != CICase.L5GC_CenterVMPort:
-               CriticalLogParam += " --CenterVMPort=" + CICase.L5GC_CenterVMPort
-           if '' != MountPort:
-               CriticalLogParam += " --MountPort=" + MountPort
-           cmd = "python3 criticallog.py" + CriticalLogParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       elif 'wait_' in action[0:len('wait_')]:
-           WaitTime(int(action[len('wait_'):len(action)]))
-       else:
-           logging.info('ERROR: wrong class ' + action)
-           sys.exit('Invalid action')
-
-       # Save Result
-       if "Ping" in action or "Iperf" in action or "EMS_" in action:
-           if(os.path.exists("test_error_result.log")):
-               os.system("echo \"    " + action + " : NG\" >> all_test_results." + CICase.build_id + ".log")
-               os.system("cat test_error_result.log >> all_test_results." + CICase.build_id + ".log")
-               os.system("rm test_error_result.log")
-               is_NG = 1
+   for testXMLfiles in testXMLfilesList:
+       xml_test_file = sys.path[0] + "/" + testXMLfiles
+       xmlTree = ET.parse(xml_test_file)
+       xmlRoot = xmlTree.getroot()
+       requested_tests=xmlRoot.findtext('TestCaseRequestedList',default='')
+       if "EMS" in requested_tests:
+           if WinEMSIPAddress != '' and WinEMSUserName != '' and WinEMSPassword != '':
+               CICase.UploadFile(WinEMSIPAddress, WinEMSUserName, WinEMSPassword, WinEMSPort, "ems_selenium.py", WinEMSSourceCodePath.replace("\\", "/")+"/src")
+               CICase.UploadFile(WinEMSIPAddress, WinEMSUserName, WinEMSPassword, WinEMSPort, "ems_pyautogui.py ", WinEMSSourceCodePath.replace("\\", "/")+"/src")
+
+       requested_tests=requested_tests.split()
+       TestCaseFile = get_test_case_name('/','.',testXMLfiles)
+
+       #get the list of tests to be done
+       for action in requested_tests:
+           logging.info('INFO: test will be run: ' + action)
+       signal.signal(signal.SIGUSR1, receive_signal)
+
+       if "Change_L5GC_Environment" in requested_tests or "CheckCUDUStatus" in requested_tests:
+           CICase.Update_Act_L5GC()
+
+       for action in requested_tests:
+           testCase_id = action
+           ShowTestID(TestCaseFile, testCase_id)
+           if 'Initialize_UE' == action:
+               cmd = "python3 ueaction.py --mode=Initialize" + ADBActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'Attach_' == action[0:len('Attach_')]:
+               UECount = action[action.index('_')+1:action.rindex('_')]
+               cmd = "python3 ueaction.py --mode=Attach --UECount=" + UECount + ADBActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'Detach_UE' == action:
+               cmd = "python3 ueaction.py --mode=Detach" + ADBActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'UE_Battery' == action:
+               UECount = action[action.index('_')+1:action.rindex('_')]
+               cmd = "python3 ueaction.py --mode=Battery" + ADBActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'Ping_DL_' == action[0:len('Ping_DL_')]:
+               ping_args, ping_packetloss_threshold, ping_rttmax_threshold = Config.Get_Ping_Conf(ADBGroupID, action)
+               cmd = "python3 ping.py --mode=DL" + APLActionParam + ADBActionParam + " --args=\"" + ping_args + "\" --packetloss_threshold=" + ping_packetloss_threshold + " --rttmax_threshold=" + ping_rttmax_threshold
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'Ping_UL_' == action[0:len('Ping_UL_')]:
+               ping_args, ping_packetloss_threshold, ping_rttmax_threshold = Config.Get_Ping_Conf(ADBGroupID, action)
+               cmd = "python3 ping.py --mode=UL" + ADBActionParam + " --args=\"" + ping_args + "\" --packetloss_threshold=" + ping_packetloss_threshold + " --rttmax_threshold=" + ping_rttmax_threshold
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'UDP_Iperf_DL_' == action[0:len('UDP_Iperf_DL_')] or 'UDP_Iperf_UL_' == action[0:len('UDP_Iperf_UL_')]:
+               iperf_args, iperf_packetloss_threshold, iperf_service_packetloss_count, iperf_service_packetloss_threshold = Config.Get_UDP_Iperf_Conf(ADBGroupID, action)
+               cmd = "python3 iperf.py --mode=UDP_" + action[len('UDP_Iperf_'):len('UDP_Iperf_DL')] + APLActionParam + ADBActionParam + " --iperf_port=" + iperf_port + " --args=\"" + iperf_args + "\" --packetloss_threshold=" + iperf_packetloss_threshold + " --service_packetloss_count=" + iperf_service_packetloss_count + " --service_packetloss_threshold=" + iperf_service_packetloss_threshold
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'UDP_Iperf_DLUL_' == action[0:len('UDP_Iperf_DLUL_')]:
+               iperf_args_dl, iperf_args_ul, iperf_packetloss_threshold = Config.Get_UDP_DLUL_Iperf_Conf(ADBGroupID, action)
+               cmd = "python3 iperf.py --mode=UDP_DLUL" + APLActionParam + ADBActionParam + " --iperf_port=" + iperf_port + " --dl_args=\"" + iperf_args_dl + "\" --ul_args=\"" + iperf_args_ul + "\" --packetloss_threshold=" + iperf_packetloss_threshold
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'TCP_Iperf_DL_' == action[0:len('TCP_Iperf_DL_')] or 'TCP_Iperf_UL_' == action[0:len('TCP_Iperf_UL_')]:
+               iperf_args = Config.Get_TCP_Iperf_Conf(ADBGroupID, action)
+               cmd = "python3 iperf.py --mode=TCP_" + action[len('TCP_Iperf_'):len('TCP_Iperf_DL')] + APLActionParam + ADBActionParam + " --iperf_port=" + iperf_port + " --args=\"" + iperf_args + "\""
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'TCP_Iperf_DLUL_' == action[0:len('TCP_Iperf_DLUL_')]:
+               iperf_args_dl, iperf_args_ul = Config.Get_TCP_DLUL_Iperf_Conf(ADBGroupID, action)
+               cmd = "python3 iperf.py --mode=TCP_DLUL" + APLActionParam + ADBActionParam + " --iperf_port=" + iperf_port + " --dl_args=\"" + iperf_args_dl + "\" --ul_args=\"" + iperf_args_ul + "\""
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'Terminate_All' == action:
+               CICase.TerminateAll()
+           elif 'Detach_Attach' == action:
+               CICase.Detach_Attach()
+           elif 'Terminate_Ping' == action:
+               CICase.TerminatePing()
+           elif 'Terminate_Iperf' == action:
+               CICase.TerminateIperf()
+           elif 'CollectDULogOpen' == action:
+               CICase.CollectDULogOpen()
+           elif 'CollectDULogOpen_nocyc' == action:
+               CICase.CollectDULogOpen_nocyc()
+           elif 'CollectDULogClose' == action:
+               CICase.CollectDULogClose()
+           elif 'Change_L5GC_Environment' == action:
+               if (-1 == CICase.Change_L5GC_ACT_SBY_Environment()):
+                   is_NG = 1
+           elif 'Update_Config_' == action[0:len('Update_Config_')]:
+               del Config
+               conf_file = action[len('Update_Config_'):len(action)]+'.ini'
+               logging.info("Cat "+conf_file)
+               logging.info("-------------------------------------------------")
+               #res = subprocess.Popen("cat "+conf_file, stdout=subprocess.PIPE, shell=True)
+               #for line in res.stdout.readlines():
+               #   print(line.decode("utf-8").strip())
+               os.system('cat '+conf_file)
+               logging.info("-------------------------------------------------")
+               Config = CI_Config(conf_file)
+           elif 'Check_IsLock_' == action[0:len('Check_IsLock_')]:
+               device = action[len('Check_IsLock_'):len(action)]
+               CICase.CheckCUDUStatus("ActionCheck", device, "LOCK")
+           elif 'Check_IsUnlock_' == action[0:len('Check_IsUnlock_')]:
+               device = action[len('Check_IsUnlock_'):len(action)]
+               CICase.CheckCUDUStatus("ActionCheck", device, "UNLOCKED")
+           elif 'EMS_Lock_And_Check_' == action[0:len('EMS_Lock_And_Check_')]:
+               device = action[len('EMS_Lock_And_Check_'):len(action)]
+               DeviceName = CICase.GetCUDUDeviceName(device)
+               if '' == DeviceName:
+                   logging.info('ERROR: wrong class ' + action)
+                   continue
+               # Check Status
+               if 1 == CICase.CheckCUDUStatus("BaseCheck", device, "LOCK"):
+                   continue
+               # Lock
+               cmd = "python3 ems.py --mode=Lock --DeviceName=" + DeviceName + WinEMSActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+               # Check Lock Result
+               CICase.CheckCUDUStatus("ActionCheck", device, "LOCK")
+           elif 'EMS_Unlock_And_Check_' == action[0:len('EMS_Unlock_And_Check_')]:
+               device = action[len('EMS_Unlock_And_Check_'):len(action)]
+               DeviceName = CICase.GetCUDUDeviceName(device)
+               if '' == DeviceName:
+                   logging.info('ERROR: wrong class ' + action)
+                   continue
+               # Check Status
+               if 1 == CICase.CheckCUDUStatus("BaseCheck", device, "UNLOCKED"):
+                   continue
+               # Unlock
+               cmd = "python3 ems.py --mode=Unlock --DeviceName=" + DeviceName + WinEMSActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+               # Check unlock Result
+               CICase.CheckCUDUStatus("ActionCheck", device, "UNLOCKED")
+           elif 'EMS_IsEnabled_' == action[0:len('EMS_IsEnabled_')]:
+               DeviceName = CICase.GetCUDUDeviceName(action[len('EMS_IsEnabled_'):len(action)])
+               if '' == DeviceName:
+                   logging.info('ERROR: wrong class ' + action)
+                   continue
+               cmd = "python3 ems.py --mode=IsEnabled --DeviceName=" + DeviceName + WinEMSActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'EMS_IsDisabled_' == action[0:len('EMS_IsDisabled_')]:
+               DeviceName = CICase.GetCUDUDeviceName(action[len('EMS_IsDisabled_'):len(action)])
+               if '' == DeviceName:
+                   logging.info('ERROR: wrong class ' + action)
+                   continue
+               cmd = "python3 ems.py --mode=IsDisabled --DeviceName=" + DeviceName + WinEMSActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           #elif 'EMS_Config_Update_' == action[0:len('EMS_Config_Update_')]:
+           #   DeviceName = CICase.GetCUDUDeviceName(action[len('EMS_Config_Update_'):len(action)])
+           #   PacketPath = Config.Get_Common_Conf(action, 'PacketPath')
+           #   cmd = "python3 ems.py --mode=Config --DeviceName=" + DeviceName + " --Packet=" + PacketPath + WinEMSActionParam
+           #   logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+           #   p = os.popen(cmd,'r',1)
+           #   p.close()
+           #l5GC
+           # elif 'EMS_Config_Update' == action:
+           #   DeviceName = CICase.L5GC_CenterVMNodeName
+           #   PacketPath = Config.Get_Common_Conf(action, 'PacketPath')
+           #   cmd = "python3 ems.py --mode=Config --DeviceName=" + DeviceName + " --Packet=" + PacketPath + WinEMSActionParam
+           #   logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+           #   p = os.popen(cmd,'r',1)
+           #   p.close()
+           # elif 'EMS_Config_Change_' == action[0:len('EMS_Config_Change_')]:
+           #   ConfigFile = action[len('EMS_Config_Change_'):len(action)] + '.yaml'
+           #   DeviceName = CICase.L5GC_CenterVMNodeName
+           #   ParamValue = Config.Get_Common_Conf(action, 'ParamValue')
+           #   cmd = "python3 ems.py --mode=Config --DeviceName=" + DeviceName + " --ConfigFile=" + ConfigFile + " --ParamValue=" + ParamValue + WinEMSActionParam
+           #   logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+           #   p = os.popen(cmd,'r',1)
+           #   p.close()
+           elif 'EMS_Update_CU_' == action[0:len('EMS_Update_CU_')]:
+               DeviceType = 'CU'
+               UpdatePacket = Config.Get_Common_Conf(action, 'UpdatePacketPath')
+               ConfigPacket = Config.Get_Common_Conf(action, 'ConfigPacketPath')
+               DeviceName = CICase.GetCUDUDeviceName('CU')
+               cmd = "python3 ems.py --mode=Update --DeviceType=" + DeviceType + " --DeviceName=" + DeviceName + " --UpdatePacket=\"" + UpdatePacket + "\" --ConfigPacket=\"" + ConfigPacket + "\"" + WinEMSActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'EMS_Update_DU_' == action[0:len('EMS_Update_DU_')]:
+               DeviceType = 'DU'
+               UpdatePacket = Config.Get_Common_Conf(action, 'UpdatePacketPath')
+               ConfigPacket = Config.Get_Common_Conf(action, 'ConfigPacketPath')
+               DeviceName = ''
+               for group_id in range(len(CICase.DUGroupIPAddress)):
+                   CICase.DUIPAddress = CICase.DUGroupIPAddress[group_id]
+                   CICase.DUPort = CICase.DUGroupPort[group_id]
+                   CICase.DUUserName = CICase.DUGroupUserName[group_id]
+                   CICase.DUPassword = CICase.DUGroupPassword[group_id]
+                   CICase.SaveDUrHUBInfo('DU'+str(group_id+1) + "_Before_Update")
+                   if group_id > 0:
+                       DeviceName = DeviceName + ','
+                   DeviceName = DeviceName + CICase.GetCUDUDeviceName('DU'+str(group_id+1))
+               cmd = "python3 ems.py --mode=Update --DeviceType=" + DeviceType + " --DeviceName=" + DeviceName + " --UpdatePacket=\"" + UpdatePacket + "\" --ConfigPacket=\"" + ConfigPacket + "\"" + WinEMSActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+               logging.info("Wait DU restart (5min) ...")
+               time.sleep(300)
+               for group_id in range(len(CICase.DUGroupIPAddress)):
+                   CICase.SaveDUrHUBInfo('DU'+str(group_id) + "_After_Update")
+           elif 'Delete_IMSI_' == action[0:len('Delete_IMSI_')]:
+               IMSI = Config.Get_Common_Conf(action, 'IMSI')
+               Args = Config.Get_Common_Conf(action, 'Args')
+               CICase.Delete_IMSI(IMSI, Args)
+           elif 'Add_IMSI_' == action[0:len('Add_IMSI_')]:
+               IMSI = Config.Get_Common_Conf(action, 'IMSI')
+               Args = Config.Get_Common_Conf(action, 'Args')
+               CICase.Add_IMSI(IMSI, Args)
+           elif "Get_IMSI_List" == action:
+               SSH.Get_All_IMSI_Status()
+           elif "Get_Connected_IMSI_List" == action:
+               IMSIArray = Config.Get_Common_Conf('IMSI_List', 'List').split(",")
+               SSH.Check_IMSI_Status(IMSIArray, "CONN")
+           elif "Get_Idle_IMSI_List" == action:
+               IMSIArray = Config.Get_Common_Conf('IMSI_List', 'List').split(",")
+               SSH.Check_IMSI_Status(IMSIArray, "IDLE")
+           elif 'Area_Stop_' == action[0:len('Area_Stop_')]:
+               #Area_Stop('amf')
+               #Area_Stop('smf')
+               CICase.Area_Stop(action[len('Area_Stop_'):len(action)].lower)
+           elif 'CU_Stop_' == action[0:len('CU_Stop_')]:
+               #CU_docker_Stop("cu_cp")
+               #CU_docker_Stop("cu_oam")
+               CICase.CU_docker_Stop('cu_'+action[len('CU_Stop_'):len(action)].lower)
+           elif 'DU_Stop_' == action[0:len('DU_Stop_')]:
+               #DU_docker_Stop("du_rlc_mac")
+               #DU_docker_Stop("du_scd")
+               #DU_docker_Stop("du_oam")
+               #DU_docker_Stop("du_oam_if")
+               CICase.DU_docker_Stop('du_'+action[len('DU_Stop_'):len(action)].lower)
+           elif 'DU_Stop_Process_' == action[0:len('DU_Stop_Process_')]:
+               CICase.DU_Process_Stop(action[len('DU_Stop_Process_'):len(action)])
+           #Not need
+           #elif 'EMS_Fault_Clear' == action:
+           #   EMS_Fault_Clear()
+           elif 'PerformPy_' == action[0:len('PerformPy_')] or 'PerformSh_' == action[0:len('PerformSh_')]:
+               Script = action[action.index('_')+1:action.rindex('_')] + '.' + action[len('Perform'):len('Perform')+2].lower()
+               IPAddress, Port, UserName, Password, ScriptPath, Args, FinishFlag, WaitFinish= Config.Get_Perform_Conf(action)
+               CICase.Perform(IPAddress, Port, UserName, Password, ScriptPath, Script, Args, FinishFlag, WaitFinish)
+           elif "Simnovator_Execute_" == action[0:len('Simnovator_Execute_')]:
+               TestCase = action[len('Simnovator_Execute_'):len(action)]
+
+               # Execute Case
+               cmd = "python3 simnovator.py --mode=Execute --TestCase=" + TestCase + SimNovatorActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+
+               # Start Monitor
+               cmd = "python3 simnovator.py --mode=Monitor --TestCase=" + TestCase + SimNovatorActionParam + " &"
+               logging.info(cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif "Simnovator_Stop_" == action[0:len('Simnovator_Stop_')]:
+               TestCase = action[len('Simnovator_Stop_'):len(action)]
+
+               # Stop Monitor
+               cmd = "kill -9 `ps -aux | grep \"python3 simnovator.py --Action=Monitor --TestCase=" + TestCase + "\" |grep -v grep |awk '{print $2}'`"
+               logging.info(cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+
+               # Stop Case
+               cmd = "python3 simnovator.py --mode=Stop --TestCase=" + TestCase + SimNovatorActionParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'CheckCUDUStatus' == action:
+               CICase.Check_CU_DU_Free5GC_Status()
+           elif 'LogCollect' == action:
+               DUIPAddress_Array_Str = ArrayToStr(CICase.DUGroupIPAddress)
+               DUUserName_Array_Str = ArrayToStr(CICase.DUGroupUserName)
+               DUPassword_Array_Str = ArrayToStr(CICase.DUGroupPassword)
+               DUPort_Array_Str = ArrayToStr(CICase.DUGroupPort)
+               CriticalLogParam = " --EMSIPAddress=" + CICase.EMSIPAddress + " --EMSUserName=" + CICase.EMSUserName + " --EMSPassword=" + CICase.EMSPassword + " --EMSSourceCodePath=\"" + CICase.EMSSourceCodePath + "\" --CUIPAddress=" + CICase.CUIPAddress + " --CUUserName=" + CICase.CUUserName + " --CUPassword=" + CICase.CUPassword + " --DUIPAddress=" + DUIPAddress_Array_Str + " --DUUserName=" + DUUserName_Array_Str + " --DUPassword=" + DUPassword_Array_Str + " --DUPort=" + DUPort_Array_Str + " --CenterVMIPAddress=" + CICase.L5GC_CenterVMIPAddress + " --CenterVMUserName=" + CICase.L5GC_CenterVMUserName + " --CenterVMPassword=" + CICase.L5GC_CenterVMPassword + " --CenterVMSourceCodePath=" + CICase.L5GC_CenterVMSourceCodePath + " --MountIPAddress=" + MountIPAddress + " --MountUserName=" + MountUserName + " --MountPassword=" + MountPassword + " --MountSourceCodePath=" + MountSourceCodePath + " --MountMovePath=" + MountMovePath
+               if '' != CICase.EMSPort:
+                   CriticalLogParam += " --EMSPort=" + CICase.EMSPort
+               if '' != CICase.CUPort :
+                   CriticalLogParam +=" --CUPort=" + CICase.CUPort
+               if '' != CICase.L5GC_CenterVMPort:
+                   CriticalLogParam += " --CenterVMPort=" + CICase.L5GC_CenterVMPort
+               if '' != MountPort:
+                   CriticalLogParam += " --MountPort=" + MountPort
+               cmd = "python3 criticallog.py" + CriticalLogParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           elif 'wait_' in action[0:len('wait_')]:
+               WaitTime(int(action[len('wait_'):len(action)]))
            else:
-               os.system("echo \"    " + action + " : OK\" >> all_test_results." + CICase.build_id + ".log")
-
-   if ADBGroupID == '00':
-       # DataCollectOFF
-       if syslogFlag == 'true':
-           cmd = "python3 syslog.py --mode=STOP" + SysLogCollectDeviceParam + LogCollectTTLParam
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-       # LogCollect
-       if innerlogFlag == 'true':
-           TTLXmlFile = Config.Get_Common_Conf('TTL_Service_Info', 'XmlFile')
-           cmd = "python3 innerlog.py" + InnerLogCollectDeviceParam + LogCollectTTLParam + " --TTLXmlFile=\"" + TTLXmlFile + "\""
-           logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
-           p = os.popen(cmd,'r',1)
-           p.close()
-   #sys.exit(CICase.fail_flag)#CI result show red
-   CICase.Set_TestL5G_Groups_Status(ADBGroupID, 1)
+               logging.info('ERROR: wrong class ' + action)
+               sys.exit('Invalid action')
+
+           # Save Result
+           if "Ping" in action or "Iperf" in action or "EMS_" in action:
+               if(os.path.exists("test_error_result.log")):
+                   os.system("echo \"    " + action + " : NG\" >> all_test_results." + CICase.build_id + ".log")
+                   os.system("cat test_error_result.log >> all_test_results." + CICase.build_id + ".log")
+                   os.system("rm test_error_result.log")
+                   is_NG = 1
+               else:
+                   os.system("echo \"    " + action + " : OK\" >> all_test_results." + CICase.build_id + ".log")
+
+       if ADBGroupID == '00':
+           # DataCollectOFF
+           if syslogFlag == 'true':
+               cmd = "python3 syslog.py --mode=STOP" + SysLogCollectDeviceParam + LogCollectTTLParam
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+           # LogCollect
+           if innerlogFlag == 'true':
+               TTLXmlFile = Config.Get_Common_Conf('TTL_Service_Info', 'XmlFile')
+               cmd = "python3 innerlog.py" + InnerLogCollectDeviceParam + LogCollectTTLParam + " --TTLXmlFile=\"" + TTLXmlFile + "\""
+               logging.info("---------------------------------------------------------------------------------------\nCMD: "+cmd)
+               p = os.popen(cmd,'r',1)
+               p.close()
+       #sys.exit(CICase.fail_flag)#CI result show red
+       CICase.Set_TestL5G_Groups_Status(ADBGroupID, 1)

 elif re.match('^MonitorCUDU', mode, re.IGNORECASE):
    if monitorFlag == 'false':
diff --git a/Python/ping.py b/Python/ping.py
index 1319178..dc66790 100644
--- a/Python/ping.py
+++ b/Python/ping.py
@@ -222,8 +222,28 @@ class PingClass(SSHClass.APLADBSSHConnection):
            message = status_queue.get()

    def TerminatePing(self):
+       logging.debug("Kill all ping process in APL and UE")
+       for group_id in range(len(self.ADBGroupIPAddress)):
+           self.ADBIPAddress = self.ADBGroupIPAddress[group_id]
+           self.ADBPort = self.ADBGroupPort[group_id]
+           self.ADBUserName = self.ADBGroupUserName[group_id]
+           self.ADBPassword = self.ADBGroupPassword[group_id]
+           self.open(self.ADBIPAddress, self.ADBUserName, self.ADBPassword, self.ADBPort)
+           self.command('stdbuf -o0 echo ' + self.ADBPassword + ' | killall -KILL ping || true', '\$', 5)
+           time.sleep(1)
+           self.command('stdbuf -o0 ps -aux | grep -v grep | grep ping', '\$', 5)
+           result = re.search('iperf', str(self.ssh.before))
+           if result is not None:
+               self.command('stdbuf -o0 echo ' + self.ADBPassword + ' | killall -KILL ping || true', '\$', 5)
+           self.close()
+
        self.open(self.APLIPAddress, self.APLUserName, self.APLPassword, self.APLPort)
-       self.command('stdbuf -o0 echo ' + self.APLPassword + ' | sudo -S killall -KILL ping', '\$', 5)
+       self.command('stdbuf -o0 echo ' + self.ADBPassword + ' | killall -KILL ping || true', '\$', 5)
+       time.sleep(1)
+       self.command('stdbuf -o0 ps -aux | grep -v grep | grep ping', '\$', 5)
+       result = re.search('iperf', str(self.ssh.before))
+       if result is not None:
+           self.command('stdbuf -o0 echo ' + self.ADBPassword + ' | killall -KILL ping || true', '\$', 5)
        self.close()

    def LogCollectPing(self):
@@ -340,4 +360,5 @@ elif mode == 'LOG':
    Case.ADBGroupPort = Case.ADBPort.split(',')
    Case.ADBGroupUserName = Case.ADBUserName.split(',')
    Case.ADBGroupPassword = Case.ADBPassword.split(',')
+   Case.TerminatePing()
    Case.LogCollectPing()
diff --git a/Python/ueaction.py b/Python/ueaction.py
index e826023..69e938f 100644
--- a/Python/ueaction.py
+++ b/Python/ueaction.py
@@ -287,7 +287,7 @@ def Usage():
    print('------------------------------------------------------------')
    print('Usage: python main.py [options]')
    print('  --help  Show this help.')
-   print('  --mode=[Initialize Attach Detach]')
+   print('  --mode=[Initialize Attach Detach Battery]')
    print('    --ADBIPAddress=ADBIPAddress')
    print('    --ADBUserName=ADBUserName')
    print('    --ADBPassword=ADBPassword')
@@ -338,3 +338,5 @@ elif mode == 'Attach':
    Case.AttachUE(ue_num)
 elif mode == 'Detach':
    Case.DetachUE()
+elif mode == 'Battery':
+   Case.GetUEBattery()
\ No newline at end of file
diff --git a/xml_files/Readme.txt b/xml_files/Readme.txt
index b4b37b3..420a2be 100644
--- a/xml_files/Readme.txt
+++ b/xml_files/Readme.txt
@@ -19,6 +19,7 @@ Actions for xml file:
    Attach_[ue_num]_UE                                  <!--Attach UE
                                                            [ue_num]:ALL 1 2 3 4 5 6 7 8-->
    Detach_UE                                           <!--Detach UE-->
+   UE_Battery                                          <!--Show UE Battery-->
    Ping_UL_[case_id]                                   <!--UL ping                             need set Ping param at config.ini
                                                            [case_id]: user define-->
    Ping_DL_[case_id]                                   <!--DL ping                             need set Ping param at config.ini

```