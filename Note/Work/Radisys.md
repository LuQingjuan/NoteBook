[TOC]
[参考资料](http://10.37.190.73:5080/masayuki.harada/open_wiki/-/wikis/Radisys-%E8%A9%A6%E9%A8%93%E6%89%8B%E9%A0%86)
# 环境
| 机器            | IP                                | User   | Pass       |                                                                                   |
| --------------- | --------------------------------- | ------ | ---------- | --------------------------------------------------------------------------------- |
| K8Sクラスタ制御 | 10.38.161.196                       | ubuntu | traffic       |                                                                                   |
|                 |                                   |        | CU重启     | sudo su                                                                           |
|                 |                                   |        |            | cd /home/ubuntu/radisys_3_2_0/cu_m6_dpdk_2du_6cell       |
|                 |                                   |        |            | helm uninstall cu                                                                 |
|                 |                                   |        |            | kubectl get pod ★podが無くなるまで待つ                                            |
|                 |                                   |        |            | helm install cu .                                                                 |
|                 |                                   |        |            | kubectl get pod ★2POD共にRUNNINGになれば完了                                      |
| 5GC             | ssh ubuntu@10.38.161.164          | ubuntu | traffic    | docker exec -it 5gc_radisys bash                                                  |
|                 |                                   |        | 工作目录   | cd /opt/free5gc/                                                                  |
|                 |                                   |        | 启动       | ./run.sh                                                                          |
|                 |                                   |        | config文件 | /home/ubuntu/work_harada/F1SIM/F1SIM_radisys/config                               |
| F1SIM           | ssh -p 64035 ubuntu@10.38.161.164 | ubuntu | traffic    | sudo docker exec -it f1sim_radisys bash                                           |
|                 |                                   |        | 工作目录   | cd /opt/oai5g_sa/cmake_targets/                                                   |
|                 |                                   |        |            | ./ran_build/build/nr-f1sim -O du_gnb.conf --sa --nokrnmod --telnetsrv --num-ues 1 |
|                 |                                   |        | 编译       | ./build_oai -x -w None --F1SIM --build-lib telnetsrv                              |
| CU              | 10.38.161.149                     | ubuntu | traffic    | 常に起動状態                                                                      |
# 测试
* 启动：
`python3 main.py --mode=TesteNB --cucpIPAddress=10.38.161.164 --cucpUserName=ubuntu --cucpPassword=traffic --cucpSourceCodePath=/msyssrv/lm/ap/bin/ --cucpSSHPort=64033 --cuupIPAddress=10.38.161.164 --cuupUserName=ubuntu --cuupPassword=traffic --cuupSourceCodePath=/pdcp/5G_IPR/gNB_SW/gNB_CU/bin/ --cuupSSHPort=64034 --f1SimDockerHostIpAddr=10.38.161.164 --f1SimDockerHostUser=ubuntu --f1SimDockerHostUserPwd=traffic --f1SimDockerHostRootPwd=traffic --nrF1SIM_IPAddress=10.38.161.164 --nrF1SIM_UserName=ubuntu --nrF1SIM_Password=traffic --nrF1SIM_SourceCodePath=/opt/oai5g_sa/ --nrF1SIM_SSH_Port=64035 --nrF1SIM_TELNET_Port=9090 --nrF1SIM_Container=f1sim_radisys --FREE5GC_IPAddress=10.38.161.164 --FREE5GC_UserName=ubuntu --FREE5GC_Password=traffic --FREE5GC_SourceCodePath=/opt/free5gc --FREE5GC_SSHPort=64032 --FREE5GC_Container=5gc_radisys --FREE5GC_GtpIP=5.5.5.101 --CU_LOG_IPAddress=10.38.161.143 --CU_LOG_UserName=ubuntu --CU_LOG_Password=traffic --K8S_IPAddress=10.38.161.196 --K8S_UserName=ubuntu --K8S_Password=traffic --K8S_SourceCodePath=/home/ubuntu/radisys_3_2_0/cu_m6_dpdk_2du_6cell/ --E1APSplitFlag=true --BUILD_ID=1 --XMLTestFile=./start.xml`

Log 拷贝
`docker cp f1sim_radisys:/opt/oai5g_sa_test4/cmake_targets/nrF1SIM_start_090003.Error_Capability.log .`
`scp -P 64035 ubuntu@10.38.161.164:/home/ubuntu/nrF1SIM_start_090003.Error_Capability.log .`

* 查看UEIP:
`ifconfig oaitun_ue1 | grep -E "netmask|Mask"`

* iperf:

|     |       |                                            |
| --- | ----- | ------------------------------------------ |
| DL  | f1sim | iperf -s -i 1 -B 60.60.0.1                 |
|     | 5gc   | iperf -c 60.60.0.1 -t 10 -i 1 -B 5.5.5.101 |
| UL  | f1sim | iperf -s -i 1 -B 5.5.5.101                 |
|     | 5gc   | iperf -c 5.5.5.101 -t 10 -i 1 -B 60.60.0.1 |

* Ping

|     |       |                                     |
| --- | ----- | ----------------------------------- |
| DL  | 5gc   | ping 60.60.0.1 -i 10                |
| UL  | f1sim | ping 5.5.5.101 -i 200 -I oaitun_ue1 |


* telnet
建立连接：
`root@ubuntu:/# telnet 127.0.0.1 9090`
uesim set securityModeCommand_failed 1
nrsimue event registration
| 说明                             | 命令                                               |
| -------------------------------- | -------------------------------------------------- |
| 帮助                             | help                                               |
| 显示rnti                         | nrsimue show rnti list                             |
| Error indication 正常値          | f1sim send errorInd f313                           |
| UE Context Setup 異常応答        |                                                    |
| UE Context Setup 無応答          |                                                    |
| UE Context Modification 異常応答 |                                                    |
| UE Context Modification 無応答   |                                                    |
| UE Context Release 無応答        |                                                    |
| RRC Setup 無応答                 |                                                    |
| Security mode 異常応答           |                                                    |
| Security mode 無応答             |                                                    |
| UE capability 異常応答           | uesim [get set] ueCapabilityEnquiry_failed <value> |
| UE capability 無応答             |                                                    |
| Reconfiguration 無応答           | uesim [get set] rrcReconfiguration_failed <value>  |
| registration                     | nrsimue event registration                         |
| deregistration                   | nrsimue event release <mod id>                     |
| 查看rnti和mod id                 | nrsimue event release                              |


## 1. 5GC起動
`cd /opt/free5gc/`
`./run.sh`
	config類
	```
	/home/ubuntu/work_harada/F1SIM/F1SIM_radisys/config
	```

## 2. CUは状態確認
**クラスタ制御10.38.2.223**
`sudo su`
`kubectl get pods`
	```
	NAME                  READY   STATUS    RESTARTS   AGE
	cu-6695d4449d-cjnx7   1/1     Running   0          21h ★RunningであればOK
	oamcu                 1/1     Running   0          21h ★RunningであればOK
	```
`kubectl describe pod` ※結果を表示する

## 3. dumpログを設定
* F1のtcpdump(U-plane実施時以外)
**5GC**
`sudo tcpdump -i ens3f3 -w 5gc_dump.pcap`
* N2のtcpdump(U-plane実施時以外)
**F1SIM**
10.38.161.164に接続
192.168.122.144に接続
`sudo tcpdump -i enp4s0 -w f1_dump.pcap`

## 4. F1SIM起動
`cd /opt/oai5g_sa/cmake_targets/`
`./ran_build/build/nr-f1sim -O du_gnb.conf --sa --nokrnmod --telnetsrv --num-ues 1`

## 5. ログの回収
* F1SIMのログ
**クラスタ制御10.38.2.223**
`sudo su`
`kubectl get pods`
`kubectl describe pod`

* F1のtcpdump(U-plane実施時以外)
tcpdumpを停止
f1_dump.pcapを回収

* N2のtcpdump(U-plane実施時以外)
tcpdumpを停止
5gc_dump.pcapを回収

* CUの状態
**クラスタ制御10.38.2.223**
`sudo su`
`kubectl get pods`
`kubectl describe pod`

* CUのログ
**CU**
/var/log/pods/default_cu******の配下全て
/var/log/pods/default_oamcu******の配下全て


## CU 重启