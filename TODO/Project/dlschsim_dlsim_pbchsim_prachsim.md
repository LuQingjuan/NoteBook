## 基本信息
### 源码
* url:    http://10.167.14.30:8081/gitlab/training/mtc-oai
* branch: feature_mmWave_nfapi_f1ap
* commit: 427679609b859b71c5cf32a413aece38e8c14032

### 编译
```
source oaienv 
cd openairinterface5g/cmake_targets/
./build_oai --phy_simulators
```

### CI
```
cd cmake_targets/autotests
sudo -E ./run_exec_autotests.bash -c test_case_list.xml

cat cmake_targets/autotests/log/results_autotests.xml
```

## nr_dlschsim
### 手动运行
* 命令
    * 切换路径：      `cd cmake_targets/ran_build/build/`

| 测试           | 命令                                           |
| -------------- | ---------------------------------------------- |
| Test1: 106 PRB | `sudo -E ./nr_dlschsim -R 106 -m9 -s13 -n100`  |
| Test2: 217 PRB | `sudo -E ./nr_dlschsim -R 217 -m15 -s15 -n100` |
| Test3: 273 PRB | `sudo -E ./nr_dlschsim -R 273 -m19 -s20 -n100` |

* log 结果确认：`PDSCH test OK`
### 参数说明
* help
`$ sudo -E ./nr_dlschsim -h`
`./nr_dlschsim -h(elp) -p(extended_prefix) -N cell_id -f output_filename -F input_filename -g channel_model -n n_frames -t Delayspread -s snr0 -S snr1  -y TXant -z RXant -i Intefrence0 -j Interference1 -A interpolation_file -C(alibration offset dB) -N CellId`
**-h** This message
**-p** Use extended prefix mode
**-V** Enable VCD dumb functions
**-n** Number of frames to simulate
**-s** Starting SNR, runs from SNR0 to SNR0 + 5 dB.  If n_frames is 1 then just SNR is simulated
**-S** Ending SNR, runs from SNR0 to SNR1
~~**-t** Delay spread for multipath channel~~
**-g** [A,B,C,D,E,F,G] Use 3GPP SCM (A,B,C,D) or 36-101 (E-EPA,F-EVA,G-ETU) models (ignores delay spread and Ricean factor)
**-y** Number of TX antennas used in eNB
**-z** Number of RX antennas used in UE
**-M** Multiple SSB positions in burst
**-N** Nid_cell
**-R** N_RB_DL
~~**-O** oversampling factor (1,2,4,8,16)~~
~~**-A** Interpolation_filname Run with Abstraction to generate Scatter plot using interpolation polynomial in file~~
**-F** Input filename (.txt format) for RX conformance testing
**-d** number of dlsch threads, 0: no dlsch parallelization
`df:hpVg:i:j:n:l:m:r:s:S:y:z:M:N:F:R:P:L:X:`

| 参数   | 说明                                                                     | 默认值              | 数据类型               | 取值范围                                                                                                                                                       |
| ------ | ------------------------------------------------------------------------ | ------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **-h** | 帮助文档                                                                 |                     | -                      |                                                                                                                                                                |
| **-d** | dlsch线程数                                                              | 0                   | uint8_t                | [0,255]<br>0：无dlsch并行化                                                                                                                                    |
| **-g** | channel_model                                                            | AWGN                | typedef enum {} SCM_t; | 'A':(3GPP SCM) SCM_A<br>'B':(3GPP SCM) SCM_B<br>'C':(3GPP SCM) SCM_C<br>'D':(3GPP SCM) SCM_D<br>'E':(36-101) E-EPA<br>'F':(36-101) F-EVA<br>'G':(36-101) G-ETU |
| **-n** | 要模拟的帧数                                                             | 1                   | int                    |                                                                                                                                                                |
| **-s** | 起始SNR，从SNR0运行到SNR0+5dB<br>如果n_frames为1，则仅模拟SNR            | -2.0                | double                 |                                                                                                                                                                |
| **-V** | 启用VCD功能                                                              | false(0)            | -                      | 0:enable<br>1:disable                                                                                                                                          |
| **-S** | 结束SNR，从SNR0运行到SNR1                                                | snr0(-s的数值) + 10 | double                 |                                                                                                                                                                |
| **-p** | 使用扩展前缀模式                                                         | false(0)            | -                      | 0:enable<br>1:disable                                                                                                                                          |
| **-y** | eNB中使用的TX天线数量                                                    | 1                   | uint8_t                | {1,2}                                                                                                                                                          |
| **-z** | UE中使用的RX天线数量                                                     | 1                   | uint8_t                | {1,2}                                                                                                                                                          |
| **-M** | 突发中的多个SSB位置                                                      | 0x01                | uint64_t               |                                                                                                                                                                |
| **-N** | Nid_cell<br>LTE 一共定义了504 个不同的PCI（即NID cell，取值范围0 ~ 503） | 0                   | uint16_t               |                                                                                                                                                                |
| **-R** | N_RB_DL<br>例如：-R 217<br>表示：217 PRB                                 | 106                 | uint16_t               |                                                                                                                                                                |
| **-F** | RX一致性测试的输入文件名（.txt格式）                                     |                     | file name              |                                                                                                                                                                |
| **-P** | PBCH相位                                                                 | 0                   | unsigned char          | {0,1,2,3}                                                                                                                                                      |
| **-L** | 日志级别                                                                 | OAILOG_WARNING      | int                    | -1: OAILOG_DISABLE<br>0: OAILOG_ERR<br>1: OAILOG_WARNING<br>2: OAILOG_ANALYSIS<br>3: OAILOG_INFO<br>4: OAILOG_DEBUG<br>5: OAILOG_TRACE                         |
| **-m** | Imcs                                                                     | 9                   | uint8_t                | [0,28]<br>因为：<br>MCS table 0 [0,28]<br>MCS table 1 [0,27]<br>MCS table 2 [0,28]<br>代码中：mcs_table = 0                                                    |
| **-l** | nb_symb_sch                                                              | 12                  | uint16_t               |                                                                                                                                                                |
| **-r** | nb_rb                                                                    | 50                  | uint16_t               |                                                                                                                                                                |
| **-X** | gNB线程池配置，n=>无线程                                                 |                     | char [128]             |                                                                                                                                                                |

### 内部的调用（TBD）
#### 编译
* /home/jftt/work_jftt/lu/mtc-oai/CMakeLists.txt
```
add_executable(nr_dlschsim
  ${OPENAIR1_DIR}/SIMULATION/NR_PHY/dlschsim.c
  ${OPENAIR1_DIR}/SIMULATION/NR_PHY/nr_dummy_functions.c
  ${OPENAIR_DIR}/common/utils/nr/nr_common.c
  ${T_SOURCE}
  ${SHLIB_LOADER_SOURCES}
  )
target_link_libraries(nr_dlschsim PRIVATE
  -Wl,--start-group UTIL SIMU PHY_COMMON PHY_NR_COMMON PHY_NR PHY_NR_UE SCHED_NR_LIB CONFIG_LIB MAC_NR_COMMON -Wl,--end-group
  m pthread ${ATLAS_LIBRARIES} ${T_LIB} ITTI dl
  )
target_link_libraries(nr_dlschsim PRIVATE asn1_nr_rrc_hdrs)
```
```
  set(T_SOURCE
      ${OPENAIR_DIR}/common/utils/T/T_IDs.h
      ${OPENAIR_DIR}/common/utils/T/T.c
      ${OPENAIR_DIR}/common/utils/T/local_tracer.c)
```
```
set (SHLIB_LOADER_SOURCES
  ${OPENAIR_DIR}/common/utils/load_module_shlib.c
)
```
#### 全局变量
|     |     ||
| --- | --- | - |

## nr_dlsim
### 手动运行
* 命令
    * 切换路径：      `cd cmake_targets/ran_build/build/`

| 测试                                           | 命令                                                      |
| ---------------------------------------------- | --------------------------------------------------------- |
| Test1: 106 PRB                                 | `sudo -E ./nr_dlsim -n100 -R106 -b106 -s5`                |
| Test2: 217 PRB                                 | `sudo -E ./nr_dlsim -n100 -R217 -b217 -s5`                |
| Test3: 273 PRB                                 | `sudo -E ./nr_dlsim -n100 -R273 -b273 -s5`                |
| Test4: HARQ test 25% TP 4 rounds               | `sudo -E ./nr_dlsim -n100 -s1 -S2 -t25`                   |
| Test5: HARQ test 33% TP 3 rounds               | `sudo -E ./nr_dlsim -n100 -s1 -S2 -t33`                   |
| Test6: HARQ test 50% TP 2 rounds               | `sudo -E ./nr_dlsim -n100 -s5 -S7 -t50`                   |
| Test7: 25 PRBs, 15 kHz SCS                     | `sudo -E ./nr_dlsim -n100 -m0 -e0 -R25 -b25 -i 2 1 0`     |
| Test1: 106 PRB 25 PDSCH-Offset                 | `sudo -E ./nr_dlsim -n100 -R106 -a25 -s5`                 |
| Test2: 106 PRB 51 PDSCH-Offset                 | `sudo -E ./nr_dlsim -n100 -R106 -a51 -s5`                 |
| Test3: 217 PRB 100 PDSCH-PRBs                  | `sudo -E ./nr_dlsim -n100 -R217 -b100 -s5`                |
| Test4: 217 PRB 80 PDSCH-Offset                 | `sudo -E ./nr_dlsim -n100 -R217 -a80 -s5`                 |
| Test5: 217 PRB 100 PDSCH-PRBs 110 PDSCH-Offset | `sudo -E ./nr_dlsim -n100 -R217 -a110 -s5 -b100`          |
| Test1: 106 PRBs 50 PDSCH-PRBs MCS Index 27     | `sudo -E ./nr_dlsim -n100 -e27 -s30`                      |
| Test2: 106 PRBs 50 PDSCH-PRBs MCS Index 16     | `sudo -E ./nr_dlsim -n100 -e16 -s11 -S13`                 |
| Test3: 106 MCS-TABLE 256 QAM MCS Index 26      | `sudo -E ./nr_dlsim -n100 -q1 -e26 -s30`                  |
| Test4: MCS 0, low SNR performance              | `sudo -E ./nr_dlsim -n100 -e0 -t95 -S-1.0 -i 2 1 0`       |
| Test5: 4x4 MIMO, 1 Layer                       | `sudo -E ./nr_dlsim -n10 -s20 -U 3 0 0 2 -gR -x1 -y4 -z4` |
| Test6: 4x4 MIMO, 2 Layers                      | `sudo -E ./nr_dlsim -n10 -s20 -U 3 0 0 2 -gR -x2 -y4 -z4` |
| Test7: 4x4 MIMO, 4 Layers                      | `sudo -E ./nr_dlsim -n10 -s20 -U 3 0 0 2 -x4 -y4 -z4`     |
| Test1: 3 PTRS, 8 Interpolated Symbols          | `sudo -E ./nr_dlsim -n100 -s5 -T 2 2 2`                   |
| Test2: 6 PTRS, 5 Interpolated Symbols          | `sudo -E ./nr_dlsim -n100 -s5 -T 2 1 2`                   |
| Test3: 11 PTRS, 0 Interpolated Symbols         | `sudo -E ./nr_dlsim -n100 -s5 -T 2 0 4`                   |
| Test4: Mapping type A, 2 DMRS Symbols          | `sudo -E ./nr_dlsim -n100 -s5 -S7 -U 2 0 1`               |
| Test5: Mapping type A, 3 DMRS Symbols          | `sudo -E ./nr_dlsim -n100 -s5 -S7 -U 2 0 2`               |
| Test6: Mapping type B, 4 DMRS Symbols          | `sudo -E ./nr_dlsim -n100 -s5 -S7 -U 2 1 3`               |

* log 结果确认：`PDSCH test OK`
### 参数说明
* help
`$ sudo -E ./nr_dlsim -h`
`./nr_dlsim -h(elp) -p(extended_prefix) -N cell_id -f output_filename -F input_filename -g channel_model -n n_frames -s snr0 -S snr1 -x transmission_mode -y TXant -z RXant -i Intefrence0 -j Interference1 -A interpolation_file -C(alibration offset dB) -N CellId`
**-h** This message
**-L** <log level, 0(errors), 1(warning), 2(analysis), 3(info), 4(debug), 5(trace)>
**-n** Number of frames to simulate
**-s** Starting SNR, runs from SNR0 to SNR0 + 5 dB.  If n_frames is 1 then just SNR is simulated
**-S** Ending SNR, runs from SNR0 to SNR1
**-g** [A,B,C,D,E,F,G,R] Use 3GPP SCM (A,B,C,D) or 36-101 (E-EPA,F-EVA,G-ETU) models or R for MIMO model (ignores delay spread and Ricean factor)
**-y** Number of TX antennas used in gNB
**-z** Number of RX antennas used in UE
**-x** Num of layer for PDSCH
**-p** Precoding matrix index
**-i** Change channel estimation technique. Arguments list: Frequency domain {0:Linear interpolation, 1:PRB based averaging}, Time domain {0:Estimates of last DMRS symbol, 1:Average of DMRS symbols}
**-R** N_RB_DL
~~**-O** oversampling factor (1,2,4,8,16)~~
~~**-A** Interpolation_filname Run with Abstraction to generate Scatter plot using interpolation polynomial in file~~
**-f** raw file containing RRC configuration (generated by gNB)
**-F** Input filename (.txt format) for RX conformance testing
~~**-o** CORESET offset~~
**-a** Start PRB for PDSCH
**-b** Number of PRB for PDSCH
~~**-c** Start symbol for PDSCH (fixed for now)~~
~~**-j** Number of symbols for PDSCH (fixed for now)~~
**-e** MSC index
**-q** MCS Table index
**-t** Acceptable effective throughput (in percentage)
**-I** Maximum LDPC decoder iterations
**-T** Enable PTRS, arguments list L_PTRS{0,1,2} K_PTRS{2,4}, e.g. -T 2 0 2 
**-U** Change DMRS Config, arguments list DMRS TYPE{0=A,1=B} DMRS AddPos{0:2} DMRS ConfType{1:2}, e.g. -U 3 0 2 1 
**-P** Print DLSCH performances
**-v** Maximum number of rounds
**-w** Write txdata to binary file (one frame)
**-d** number of dlsch threads, 0: no dlsch parallelization
**-X** gNB thread pool configuration, n => no threads
**-Y** Run initial sync in UE
`f:hA:p:f:g:i:n:s:S:t:v:x:y:z:M:N:F:GR:d:PI:L:a:b:e:m:w:T:U:q:X:Y`

| 参数   | 说明                                                                                                            | 默认值                   | 数据类型               | 取值范围                                                                                                                                                                                   |
| ------ | --------------------------------------------------------------------------------------------------------------- | ------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **-h** | 帮助文档                                                                                                        | -                        |                        |                                                                                                                                                                                            |
| **-f** | 包含RRC配置的原始文件（由gNB生成）                                                                              | NULL                     | file name              |                                                                                                                                                                                            |
| **-g** | channel_model                                                                                                   | AWGN                     | typedef enum {} SCM_t; | 'A':(3GPP SCM) SCM_A<br>'B':(3GPP SCM) SCM_B<br>'C':(3GPP SCM) SCM_C<br>'D':(3GPP SCM) SCM_D<br>'E':(36-101) E-EPA<br>'F':(36-101) F-EVA<br>'G':(36-101) G-ETU<br>'R':(MIMO模型) Rayleigh1 |
| **-i** | 改变信道估计技术。<br>例如：-i 2 1 0 <br>表示：后面有2个数据<br>频域基于PRB的平均<br>时域最后一个DMRS符号的估计 | 0                        | int[2]                 | 第一个参数：{1,2}<br>第二个参数（频域）：<br>0:线性插值<br>1:基于PRB的平均<br>第三个参数（时域）：<br>0:最后一个DMRS符号的估计<br>1:DMRS符号平均                                           |
| **-n** | 要模拟的帧数                                                                                                    | 1                        | int                    |                                                                                                                                                                                            |
| **-s** | 起始SNR，从SNR0运行到SNR0+5dB<br>如果n_frames为1，则仅模拟SNR                                                   | -2.0                     | double                 |                                                                                                                                                                                            |
| **-S** | 结束SNR，从SNR0运行到SNR1                                                                                       | snr0(-s的数值) + 10      | double                 |                                                                                                                                                                                            |
| **-x** | PDSCH的层数                                                                                                     | 1                        | int                    | {1,2,3,4}                                                                                                                                                                                  |
| **-p** | 预编码矩阵索引                                                                                                  | 0                        | int                    |                                                                                                                                                                                            |
| **-v** | 最大轮次                                                                                                        | 4                        | uint8_t                | [1,16]                                                                                                                                                                                     |
| **-y** | gNB中使用的TX天线数量                                                                                           | 1                        | uint8_t                | {1,2,3,4}                                                                                                                                                                                  |
| **-z** | UE中使用的RX天线数量                                                                                            | 1                        | uint8_t                | {1,2,3,4}                                                                                                                                                                                  |
| **-R** | N_RB_DL<br>例如：-R217<br>表示：217 PRB                                                                         | 106                      | int                    |                                                                                                                                                                                            |
| **-F** | RX一致性测试的输入文件名（.txt格式）                                                                            | NULL                     | file name              |                                                                                                                                                                                            |
| **-P** | 打印DLSCH性能print_perf=1;<br>opp_enabled=1;print_perf=1;<br>opp_enabled=1;                                     | false(0)                 | -                      | 0:enable<br>1:disable                                                                                                                                                                      |
| **-I** | LDPC解码器最大迭代次数                                                                                          | 5                        | uint8_t                |                                                                                                                                                                                            |
| **-L** | 日志级别                                                                                                        | OAILOG_WARNING           | int                    | -1: OAILOG_DISABLE<br>0: OAILOG_ERR<br>1: OAILOG_WARNING<br>2: OAILOG_ANALYSIS<br>3: OAILOG_INFO<br>4: OAILOG_DEBUG<br>5: OAILOG_TRACE                                                     |
| **-a** | PDSCH的启动PRB  PDSCH-Offset<br>例如：-a51<br>表示：51 PDSCH-Offset                                             | -1                       | int                    |                                                                                                                                                                                            |
| **-b** | PDSCH的PRB数量<br>例如：-b100 <br>表示：100 PDSCH-PRBs                                                          | -1                       | int                    |                                                                                                                                                                                            |
| **-d** | dlsch线程数<br>0：无dlsch并行化                                                                                 | 0                        | uint8_t                |                                                                                                                                                                                            |
| **-e** | MCS Index<br>例如：-e16<br>表示：MCS Index 16                                                                   | -1                       | int                    |                                                                                                                                                                                            |
| **-q** | MCS表索引                                                                                                       | 0                        | int                    |                                                                                                                                                                                            |
| **-m** | mu 数字索引                                                                                                     | 1                        | int                    | {0,1,2,3,4}<br>ue_init_config_request(UE_mac, mu);<br>int slots_per_frame = nr_slots_per_frame[scs];<br>const uint8_t nr_slots_per_frame[5] = {10, 20, 40, 80, 160};                       |
| **-t** | 可接受的有效吞吐量（百分比）<br>例如：-t33<br>表示：33% TP                                                      | 0.7                      | int                    |                                                                                                                                                                                            |
| **-w** | 将txdata写入二进制文件（一帧）（txdata.dat）                                                                    | NULL                     | file name              | 带参数没有意义                                                                                                                                                                             |
| **-T** | 启用PTRS<br>例如：-T 2 0 2<br>表示：后面有2个数据，L_PTRS是0，K_PTRS是2                                         | ptrs_arg[2] = {-1,-1}    | int8_t[2]              | 第一个参数：{1,2}<br>第二个参数（L_PTRS）：{0，1，2}<br>第三个参数（K_PTRS）：{2，4}                                                                                                       |
| **-U** | 更改DMRS配置<br>例如：-U 3 0 2 1<br>表示：后面有3个数据，DMRS类型是A，DMRS AddPos是2，DMRS Conf Type是1         | dmrs_arg[3] = {-1,-1,-1} | int8_t[3]              | 第一个参数：{1,2,3}<br>第二个参数（DMRS类型）：{0=A，1=B}<br>第三个参数（DMRS AddPos）：{0,1,2,3}<br>第四个参数（DMRS Conf Type）：{1:2}                                                   |
| **-X** | gNB线程池配置，n=>无线程                                                                                        |                          | char [128]             |                                                                                                                                                                                            |
| **-Y** | 在UE中运行初始同步                                                                                              | false(0)                 | -                      | 0:enable<br>1:disable                                                                                                                                                                      |


### 内部的调用（TBD）

#### 编译
* /home/jftt/work_jftt/lu/mtc-oai/CMakeLists.txt
```
add_executable(nr_dlsim
  ${OPENAIR1_DIR}/SIMULATION/NR_PHY/dlsim.c
  ${OPENAIR1_DIR}/SIMULATION/NR_PHY/nr_dummy_functions.c
  ${OPENAIR_DIR}/common/utils/nr/nr_common.c
  ${OPENAIR_DIR}/executables/softmodem-common.c
  ${OPENAIR2_DIR}/RRC/NAS/nas_config.c
  ${NR_UE_RRC_DIR}/rrc_nsa.c
  ${NFAPI_USER_DIR}/nfapi.c
  ${NFAPI_USER_DIR}/gnb_ind_vars.c
  ${PHY_INTERFACE_DIR}/queue_t.c
  ${T_SOURCE}
  ${SHLIB_LOADER_SOURCES}
  )
target_link_libraries(nr_dlsim PRIVATE
  -Wl,--start-group UTIL SIMU SIMU_ETH PHY_COMMON PHY_NR_COMMON PHY_NR PHY_NR_UE SCHED_NR_LIB SCHED_NR_UE_LIB MAC_NR MAC_UE_NR MAC_NR_COMMON nr_rrc CONFIG_LIB L2_NR HASHTABLE x2ap SECU_CN ngap -lz -Wl,--end-group
  m pthread ${ATLAS_LIBRARIES} ${T_LIB} ITTI ${OPENSSL_LIBRARIES} dl
  )
target_link_libraries(nr_dlsim PRIVATE asn1_nr_rrc_hdrs asn1_lte_rrc_hdrs)
```
```
  set(T_SOURCE
      ${OPENAIR_DIR}/common/utils/T/T_IDs.h
      ${OPENAIR_DIR}/common/utils/T/T.c
      ${OPENAIR_DIR}/common/utils/T/local_tracer.c)
```
```
set (SHLIB_LOADER_SOURCES
  ${OPENAIR_DIR}/common/utils/load_module_shlib.c
)
```
#### 全局变量
|     |     ||
| --- | --- | - |

## nr_pbchsim
### 手动运行
* 命令
    * 切换路径：      `cd cmake_targets/ran_build/build/`

| 测试                                                     | 命令                                                   |
| -------------------------------------------------------- | ------------------------------------------------------ |
| Test1: PBCH-only, 106 PRB                                | `sudo -E ./nr_pbchsim -s-11 -S-8 -n10 -R106`           |
| Test2: PBCH and synchronization, 106PBR                  | `sudo -E ./nr_pbchsim -s-11 -S-8 -n10 -o8000 -I -R106` |
| Test3: PBCH and synchronization, 106PBR, SSB SC OFFSET 6 | `sudo -E ./nr_pbchsim -s-11 -S-8 -n10 -R106 -O6`       |
| Test1: PBCH-only, 217 PRB                                | `sudo -E ./nr_pbchsim -s-10 -S-8 -n10 -R217`           |
| Test2: PBCH and synchronization, 217 RPB                 | `sudo -E ./nr_pbchsim -s-10 -S-8 -n10 -o8000 -I -R217` |
| Test1: PBCH-only, 273 PRB                                | `sudo -E ./nr_pbchsim -s-10 -S-8 -n10 -R273`           |
| Test2: PBCH and synchronization, 273 PRB                 | `sudo -E ./nr_pbchsim -s-10 -S-8 -n10 -o8000 -I -R273` |

* log 结果确认：`PBCH test OK`
### 参数说明
* help
`$ sudo -E ./nr_pbchsim -h`
`./nr_pbchsim -F input_filename -g channel_mod -h(elp) -I(nitial sync) -L log_lvl -n n_frames -M SSBs -n frames -N cell_id -o FO -P phase -r seed -R RBs -s snr0 -S snr1 -x transmission_mode -y TXant -z RXant`
**-F** Input filename (.txt format) for RX conformance testing
**-g** [A,B,C,D,E,F,G] Use 3GPP SCM (A,B,C,D) or 36-101 (E-EPA,F-EVA,G-ETU) models (ignores delay spread and Ricean factor)
**-h** This message
**-I** run initial sync with target error rate 0.1
**-L** set the log level (-1 disable, 0 error, 1 warning, 2 info, 3 debug, 4 trace)
**-m** Numerology index
**-M** Multiple SSB positions in burst
**-n** Number of frames to simulate
**-N** Nid_cell
**-o** Carrier frequency offset in Hz
**-O** SSB subcarrier offset
**-P** PBCH phase, allowed values 0-3
**-r** set the random number generator seed (default: 0 = current time)
**-R** N_RB_DL
**-s** Starting SNR, runs from SNR0 to SNR0 + 10 dB if not -S given. If -n 1, then just SNR is simulated
**-S** Ending SNR, runs from SNR0 to SNR1
**-x** Transmission mode (1,2,6 for the moment)
**-y** Number of TX antennas used in eNB
**-z** Number of RX antennas used in UE
`F:g:hIL:m:M:n:N:o:O:P:r:R:s:S:x:y:z:`

| 参数   | 说明                                                                       | 默认值              | 数据类型               | 取值范围                                                                                                                                                       |
| ------ | -------------------------------------------------------------------------- | ------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **-h** | 帮助文档                                                                   |                     | -                      |                                                                                                                                                                |
| **-F** | RX一致性测试的输入文件名（.txt格式）                                       | NULL                | file name              |                                                                                                                                                                |
| **-g** | channel_model                                                              | AWGN                | typedef enum {} SCM_t; | 'A':(3GPP SCM) SCM_A<br>'B':(3GPP SCM) SCM_B<br>'C':(3GPP SCM) SCM_C<br>'D':(3GPP SCM) SCM_D<br>'E':(36-101) E-EPA<br>'F':(36-101) F-EVA<br>'G':(36-101) G-ETU |
| **-I** | 运行初始同步，目标错误率为0.1<br>例如：:-I<br>表示：synchronization        | false(0)            | -                      | 0:enable<br>1:disable                                                                                                                                          |
| **-L** | 日志级别                                                                   | OAILOG_WARNING      | int                    | -1: OAILOG_DISABLE<br>0: OAILOG_ERR<br>1: OAILOG_WARNING<br>2: OAILOG_ANALYSIS<br>3: OAILOG_INFO<br>4: OAILOG_DEBUG<br>5: OAILOG_TRACE                         |
| **-m** | mu 数字索引                                                                | 1                   | int                    |                                                                                                                                                                |
| **-M** | 突发中的多个SSB位置                                                        | 0x01                | uint64_t               |                                                                                                                                                                |
| **-n** | 要模拟的帧数                                                               | 1                   | int                    |                                                                                                                                                                |
| **-N** | Nid_cell<br>LTE 一共定义了504 个不同的PCI（即NID cell，取值范围0 ~ 503）   | 0                   | uint16_t               |                                                                                                                                                                |
| **-O** | SSB子载波偏移<br>例如：:-O6<br>表示：SSB SC OFFSET 6                       | 0                   | int                    |                                                                                                                                                                |
| **-o** | 载波频率偏移（Hz）                                                         | 0                   | double                 |                                                                                                                                                                |
| **-P** | PBCH相位                                                                   | 0                   | unsigned char          | {0,1,2,3}                                                                                                                                                      |
| **-r** | 设置随机数生成器种子（默认值：0=当前时间）                                 | 0                   | int                    |                                                                                                                                                                |
| **-R** | N_RB_DL                                                                    | 273                 | int                    |                                                                                                                                                                |
| **-s** | 起始SNR，从SNR0运行到SNR0+10 dB（如果未给出-S）。<br>如果-n 1，则仅模拟SNR | -2.0                | double                 |                                                                                                                                                                |
| **-S** | 结束SNR，从SNR0运行到SNR1                                                  | snr0(-s的数值) + 10 | double                 |                                                                                                                                                                |
| **-x** | 传输模式                                                                   | 1                   | uint8_t                | {1,2,6}                                                                                                                                                        |
| **-y** | eNB中使用的TX天线数量                                                      | 1                   | uint8_t                | {1,2}                                                                                                                                                          |
| **-z** | UE中使用的RX天线数量                                                       | 1                   | uint8_t                | {1,2}                                                                                                                                                          |


### 内部的调用（TBD）
#### 编译
* /home/jftt/work_jftt/lu/mtc-oai/CMakeLists.txt
```
add_executable(nr_pbchsim
  ${OPENAIR1_DIR}/SIMULATION/NR_PHY/pbchsim.c
  ${OPENAIR1_DIR}/SIMULATION/NR_PHY/nr_dummy_functions.c
  ${OPENAIR_DIR}/common/utils/nr/nr_common.c
  ${T_SOURCE}
  ${SHLIB_LOADER_SOURCES}
  )
target_link_libraries(nr_pbchsim PRIVATE
  -Wl,--start-group UTIL SIMU PHY_COMMON PHY_NR_COMMON PHY_NR PHY_NR_UE SCHED_NR_LIB CONFIG_LIB MAC_NR_COMMON -Wl,--end-group
  m pthread ${ATLAS_LIBRARIES} ${T_LIB} ITTI dl
)
target_link_libraries(nr_pbchsim PRIVATE asn1_nr_rrc_hdrs asn1_lte_rrc_hdrs)
```
```
  set(T_SOURCE
      ${OPENAIR_DIR}/common/utils/T/T_IDs.h
      ${OPENAIR_DIR}/common/utils/T/T.c
      ${OPENAIR_DIR}/common/utils/T/local_tracer.c)
```
```
set (SHLIB_LOADER_SOURCES
  ${OPENAIR_DIR}/common/utils/load_module_shlib.c
)
```
#### 全局变量
|     |     ||
| --- | --- | - |
## nr_prachsim
### 手动运行
* 命令
    * 切换路径：      `cd cmake_targets/ran_build/build/`

| 测试                                           | 命令                                                              |
| ---------------------------------------------- | ----------------------------------------------------------------- |
| Test1: 30kHz SCS, 106 PRBs, Prach format A2    | `sudo -E ./nr_prachsim -a -s -30 -n 100 -p 63 -R 106`             |
| Test2: 30kHz SCS, 217 PRBs, Prach format A2    | `sudo -E ./nr_prachsim -a -s -30 -n 100 -p 63 -R 217`             |
| Test3: 30kHz SCS, 273 PRBs, Prach format A2    | `sudo -E ./nr_prachsim -a -s -30 -n 100 -p 63 -R 273`             |
| Test4: 30kHz SCS, 106 PRBs, Prach format 0     | `sudo -E ./nr_prachsim -a -s -30 -n 100 -p 63 -R 106     -c 4`    |
| Test5: 120kHz SCS, 32 PRBs, Prach format A2    | `sudo -E ./nr_prachsim -a -s -30 -n 100 -p 32 -R 32 -m 3 -c52`    |
| Test6: 120kHz SCS, 66 PRBs, Prach format A2    | `sudo -E ./nr_prachsim -a -s -30 -n 100 -p 32 -R 66 -m 3 -c52`    |
| Test7: 120kHz SCS, 66 PRBs, High Speed Enabled | `sudo -E ./nr_prachsim -a -s -30 -n 100       -R 66 -m 3 -c52 -H` |
| Test8: 15kHz SCS, 25 PRBs                      | `sudo -E ./nr_prachsim -a -s -30 -n 100 -p 99 -R 25 -m 0`         |

* log 结果确认：`PRACH test OK`
### 参数说明
* help
`$ sudo -E ./nr_prachsim -h`
`./nr_prachsim -h(elp) -a(wgn on) -p(extended_prefix) -N cell_id -f output_filename -F input_filename -g channel_model -n n_frames -s snr0 -S snr1 -x transmission_mode -y TXant -z RXant -i Intefrence0 -j Interference1 -A interpolation_file -C(alibration offset dB) -N CellId`
**-h** This message
**-a** Use AWGN channel and not multipath
**-n** Number of frames to simulate
**-s** Starting SNR, runs from SNR0 to SNR0 + 5 dB.  If n_frames is 1 then just SNR is simulated
**-S** Ending SNR, runs from SNR0 to SNR1
**-g** [A,B,C,D,E,F,G,I,N] Use 3GPP SCM (A,B,C,D) or 36-101 (E-EPA,F-EVA,G-ETU) or Rayleigh1 (I) or Rayleigh1_800 (N) models (ignores delay spread and Ricean factor)
**-z** Number of RX antennas used in gNB
**-N** Nid_cell
~~**-O** oversampling factor (1,2,4,8,16)~~
**-d** Channel delay 
**-v** Starting UE velocity in km/h, runs from 'v' to 'v+50km/h'. If n_frames is 1 just 'v' is simulated 
**-V** Ending UE velocity in km/h, runs from 'v' to 'V'-L rootSequenceIndex (0-837)
**-Z** NCS_config (ZeroCorrelationZone) (0-15)
**-H** Run with High-Speed Flag enabled 
**-R** Number of PRB (6,15,25,50,75,100)
**-F** Input filename (.txt format) for RX conformance testing
`hHaA:Cc:l:r:p:g:m:n:s:S:t:x:y:v:V:z:N:F:d:Z:L:R:E`

| 参数   | 说明                                                                        | 默认值                  | 数据类型               | 取值范围                                                                                                                                                                                                                                                                                             |
| ------ | --------------------------------------------------------------------------- | ----------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **-h** | 帮助文档                                                                    |                         | -                      |                                                                                                                                                                                                                                                                                                      |
| **-a** | 使用AWGN信道，而不是多路径                                                  | false(0)                | -                      | 0:enable<br>1:disable                                                                                                                                                                                                                                                                                |
| **-c** | config_index                                                                | 98                      | uint8_t                |                                                                                                                                                                                                                                                                                                      |
| **-l** | 日志级别                                                                    | OAILOG_INFO             | int                    | -1: OAILOG_DISABLE<br>0: OAILOG_ERR<br>1: OAILOG_WARNING<br>2: OAILOG_ANALYSIS<br>3: OAILOG_INFO<br>4: OAILOG_DEBUG<br>5: OAILOG_TRACE                                                                                                                                                               |
| **-r** | msg1_frequencystart                                                         | 0                       | uint8_t                |                                                                                                                                                                                                                                                                                                      |
| **-d** | 信道延迟                                                                    | 0                       | int                    |                                                                                                                                                                                                                                                                                                      |
| **-g** | channel_model                                                               |                         | typedef enum {} SCM_t; | 'A':(3GPP SCM) SCM_A<br>'B':(3GPP SCM) SCM_B<br>'C':(3GPP SCM) SCM_C<br>'D':(3GPP SCM) SCM_D<br>'E':(36-101) E-EPA<br>'F':(36-101) F-EVA<br>'G':(36-101) G-ETU<br>'H':Rayleigh8<br>'I': Rayleigh1<br>'J':Rayleigh1_corr<br>'K':Rayleigh1_anticorr<br>'L':Rice8<br>'M':Rice1<br>'N':Rayleigh1_800<br> |
| **-E** | threequarter_fs                                                             | 0                       | -                      |                                                                                                                                                                                                                                                                                                      |
| **-m** | mu                                                                          | 1                       | int                    | {0,1,3}                                                                                                                                                                                                                                                                                              |
| **-n** | 要模拟的帧数                                                                | 1                       | int                    |                                                                                                                                                                                                                                                                                                      |
| **-s** | 起始SNR，从SNR0运行到SNR0+5dB。如果n_frames(-n)为1，则仅模拟SNR             | -2.0                    | double                 |                                                                                                                                                                                                                                                                                                      |
| **-S** | 结束SNR，从SNR0运行到SNR1                                                   | snr0(-s的数值) + 5      | double                 |                                                                                                                                                                                                                                                                                                      |
| **-p** | preamble_tx                                                                 | 0                       | uint16_t               |                                                                                                                                                                                                                                                                                                      |
| **-v** | 起始UE速度（km/h）<br>从“v”到“v+50km/h”<br>如果n_frames(-n)为1，则仅模拟“v” | 0.0                     | double                 |                                                                                                                                                                                                                                                                                                      |
| **-V** | 终端UE速度（km/h）<br>从“V”到“V”                                            | ue_speed(-v的数值) + 50 | double                 |                                                                                                                                                                                                                                                                                                      |
| **-Z** | NCS_config（零相关区）                                                      | 0                       | int                    | [0,15]                                                                                                                                                                                                                                                                                               |
| **-H** | 启用高速标志的H Run<br>例如：:-H<br>表示：High Speed Enabled                | false(0)                | -                      | 0:enable<br>1:disable                                                                                                                                                                                                                                                                                |
| **-L** | rootSequenceIndex                                                           | 1                       | int                    | [0,837]                                                                                                                                                                                                                                                                                              |
| **-x** | 传输模式                                                                    | 1                       | uint8_t                | {1,2,6}                                                                                                                                                                                                                                                                                              |
| **-y** | UE中使用的TX天线数量（目前为1,2）                                           | 1                       | uint8_t                | {1,2}                                                                                                                                                                                                                                                                                                |
| **-z** | gNB中使用的RX天线数量（目前为1,2）                                          | 1                       | uint8_t                | {1,2}                                                                                                                                                                                                                                                                                                |
| **-N** | Nid_cell<br>LTE 一共定义了504 个不同的PCI（即NID cell，取值范围0 ~ 503）    | 0                       | uint16_t               |                                                                                                                                                                                                                                                                                                      |
| **-R** | N_RB_UL<br>PRB数量<br>例如：:-R 273<br>表示：273 PRBs                       | 106                     | int                    |                                                                                                                                                                                                                                                                                                      |
| **-F** | RX一致性测试的输入文件名（.txt格式）                                        | NULL                    | file name              |                                                                                                                                                                                                                                                                                                      |


* 子载波15KHz计算，一个PRB资源有12个子载波组成：

| 带宽 | prb数量 | 子载波 |
| ---- | ------- | ------ |
| 20   | 100     | 1200   |
| 15   | 75      | 900    |
| 10   | 50      | 600    |
| 5    | 25      | 300    |
| 3    | 15      | 180    |
| 1.4  | 6       | 72     |

### 内部的调用（TBD）
#### 编译
* /home/jftt/work_jftt/lu/mtc-oai/CMakeLists.txt
```
add_executable(nr_prachsim
  ${OPENAIR1_DIR}/SIMULATION/NR_PHY/prachsim.c
  ${OPENAIR1_DIR}/SIMULATION/NR_PHY/nr_dummy_functions.c
  ${OPENAIR_DIR}/common/utils/nr/nr_common.c
  ${T_SOURCE}
  ${SHLIB_LOADER_SOURCES})
target_link_libraries(nr_prachsim PRIVATE
  -Wl,--start-group UTIL SIMU PHY_COMMON PHY_NR_COMMON PHY_NR PHY_RU PHY_NR_UE MAC_NR_COMMON SCHED_NR_LIB CONFIG_LIB -lz -Wl,--end-group
  m pthread ${ATLAS_LIBRARIES} ${T_LIB} ITTI ${OPENSSL_LIBRARIES} dl)
target_link_libraries(nr_prachsim PRIVATE asn1_nr_rrc_hdrs asn1_lte_rrc_hdrs)
```
```
  set(T_SOURCE
      ${OPENAIR_DIR}/common/utils/T/T_IDs.h
      ${OPENAIR_DIR}/common/utils/T/T.c
      ${OPENAIR_DIR}/common/utils/T/local_tracer.c)
```
```
set (SHLIB_LOADER_SOURCES
  ${OPENAIR_DIR}/common/utils/load_module_shlib.c
)
```
#### 全局变量
|     |     ||
| --- | --- | - |




```graphviz
digraph structs {
    node[shape=record];
    graph[rankdir=LR];
    
    struct1[label="
    <f0> left|
    <f1> mid&#92; dle|
    <f2> right
    "];
    struct2[label="<f0> one|<f1> two"];
    struct3[label="hello&#92;nworld |{ b |{c|<here> d|e}| f}| g | h"];
    struct1:f1 -> struct2:f0;
    struct1:f2 -> struct3:here;
}
```