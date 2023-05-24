[Wiki](http://10.167.14.30:8081/gitlab/training/mtc-oai/wikis/OAI-CU-F1SIM)

### 环境
|         | 29                          | 32                                                  | 命令                                                                                                                                                                                                        |
| ------- | --------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| free5gc |                             |                                                     | 查看AMF_IP：docker inspect amf                                                                                                                                                                              |
| CU      | docker exec -it oai-cu bash | cd /home/jftt/work_jftt/yinc/oai5g_sa/cmake_targets | [ 编译 ] ./build_oai --gNB --nrUE -x -c -w None<br>[ 运行 ] ./ran_build/build/nr-softmodem --sa -O cu_gnb.conf --log_config.global_log_options level,nocolor,time                                           |
| f1sim   | docker exec -it f1sim bash  | cd /home/jftt/work_jftt/yinc/oai5g_sa/cmake_targets | [ 编译 ] ./build_oai -x -w None --F1SIM --build-lib telnetsrv -c<br>[ 运行 ] ./ran_build/build/nr-f1sim -O du_gnb.1cell.conf --sa --nokrnmod --telnetsrv --log_config.global_log_options level,nocolor,time |
|         |                             |                                                     |

### 29环境
环境: CU + F1SIM + FREE5GC
  10.167.14.29

**1. CU: http://10.37.190.73:5080/oai5g_community/oai5g_sa.git       branch: cu_configuring_multiple_cells**
  * [ 查看AMF_IP ] 
     >  docker inspect amf
  * [ 进入CU container ]  
    >  docker exec -it oai-cu bash  
  * [ 配置文件修改 ] 
    * >   vi /oai-ran/cmake_targets/cu_gnb.conf
    * >   amf_ip_address      = ( { ipv4       = "`AMF_IP`"; 
  * [ 编译 ]
    >  ./build_oai --gNB --nrUE -x -c -w None 
 * [ 运行 ] 
    >  ./ran_build/build/nr-softmodem --sa -O cu_gnb.conf --log_config.global_log_options level,nocolor,time


**2. F1SIM: http://10.37.190.73:5080/oai5g_community/oai5g_sa.git       branch: radisys_3cell_para**  
  * [ 进入F1SIM container ] 
    > docker exec -it f1sim bash 
  * [ 编译 ]  
    > ./build_oai -x -w None --F1SIM --build-lib telnetsrv -c 
  * [ 运行 ]  
    > ./ran_build/build/nr-f1sim -O du_gnb.1cell.conf --sa --nokrnmod --telnetsrv --log_config.global_log_options level,nocolor,time 

**3. ping:**
  *  [ 查看UPF_IP ]
     >  docker inspect upf
  * [ UE侧 ]  
    >  ping `UPF_IP` -I oaitun_ue1 -c 10

**4. iperf:**
  *  [ 进入UPF container ]
     >  docker exec -it upf bash
  *  [ 安装依赖包]
     >  apt-get install inetutils-ping iperf
  * [ 执行upf脚本 ]
     >  ./upf-iptables.sh
  * [ DL ]
    * [ UE ]
      >  iperf -s -u -i 1 -B `ue_ip` -p 5001
    * [ UPF ]
      >  iperf -u -t 10 -i 1 -p 5001 -c `ue_ip` -B `UPF_IP` -b 12M
  * [ UL ]
    * [ UPF ]
      > UPF: iperf -s -u -i 1 -B `UPF_IP` -p 5001  
    * [ UE ]
      >  iperf -u -t 10 -i 1 -p 5001 -c `UPF_IP` -B `ue_ip` -b 17M
## 32 环境
10.167.14.32环境
f1sim:/home/jftt/work_jftt/yinc/oai5g_sa/cmake_targets
10.167.14.29
cu:/home/jftt/work_jftt/yinc/oai5g_cu/cmake_targets

用的32上的free5gc