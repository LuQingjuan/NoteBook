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









main                                             executables\nr-f1sim.c
    create_tasks_f1sim
        nas_nrue_task
        if(next_Mod_id < (ue_count -1))          openair3\NAS\NR_UE\nr_nas_msg_sim.c
            nr_ue_rrc_trigger_msg3


check_nr_prach
nr_ue_prach_procedures
    nr_ue_get_rach

    nr_decode_SI

    nr_rrc_ue_generate_ra_msg

    nr_rrc_ue_decode_NR_BCCH_DL_SCH_Message
        nr_rrc_ue_generate_RRCSetupRequest
            do_RRCSetupRequest "RRCSetupRequest Encoded "

```mermaid
    sequenceDiagram
    participant  main   as main
    participant  gtpv1u as gtpv1uTask
    participant  nas    as nas_nrue_task
    participant  rrc    as rrc_nrue_task
    participant  du     as F1AP_DU_task
    participant  sctp   as sctp_eNB_task
    participant  cu     as cu
  
    activate main
        Note right of main:                    create_tasks_f1sim()
        main->>sctp:                           itti_create_task(TASK_SCTP, sctp_eNB_task, NULL) < 0)
        main->>rrc:                            itti_create_task (TASK_RRC_NRUE, rrc_nrue_task, NULL)
        main->>nas:                            itti_create_task (TASK_NAS_NRUE, nas_nrue_task, NULL)
        main->>du:                             itti_create_task(TASK_DU_F1, F1AP_DU_task, NULL)
        main->>gtpv1u:                         itti_create_task(TASK_GTPV1_U, gtpv1uTask, NULL)
        Note right of main:                    init_pdcp()
        main->>du:                             itti_send_msg_to_task (TASK_DU_F1, GNB_MODULE_ID_TO_INSTANCE(0), msg_p);
    deactivate main


    activate du
        Note right of du:                      case F1AP_SETUP_REQ:
        du->>sctp:                             itti_send_msg_to_task(TASK_SCTP, instance, message_p);
    deactivate du

    activate sctp
        Note right of sctp:                    case SCTP_NEW_ASSOCIATION_REQ:
    deactivate sctp



    activate nas
        Note right of nas:                    case FGS_SECURITY_MODE_COMMAND:
        Note right of nas:                    nr_ue_rrc_trigger_msg3()
        nas->>rrc:                            itti_send_msg_to_task(TASK_RRC_NRUE, 0, message_p);
    deactivate nas

    activate rrc
        Note right of rrc:                    case RRC_SEND_MSG3:
        Note right of rrc:                    nr_rrc_ue_generate_RRCSetupRequest()
        rrc->>du:                              itti_send_msg_to_task(TASK_DU_F1, 0, tmp);
    deactivate rrc

    activate du
        Note right of du:                     case F1AP_INITIAL_UL_RRC_MESSAGE:
        Note right of du:                     DU_send_INITIAL_UL_RRC_MESSAGE_TRANSFER()
        Note right of du:                     f1ap_itti_send_sctp_data_req()
        du->>sctp:                            itti_send_msg_to_task(TASK_SCTP, instance, message_p);
    deactivate du

    activate sctp
        Note right of sctp:                   case SCTP_DATA_REQ:
        Note right of sctp:                   sctp_sendmsg()
    deactivate sctp


    activate du
        Note right of du:                     case NR_RRC_MAC_CCCH_DATA_IND:
        Note right of du:                     du_task_handle_sctp_data_ind()
        Note right of du:                     f1ap_handle_message()
    deactivate du
```
rrc_ue_generate_RRCSetupComplete