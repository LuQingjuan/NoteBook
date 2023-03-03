https://www.zhihu.com/question/390350642











|       |                              |                                                                 |
| ----- | ---------------------------- | --------------------------------------------------------------- |
| CU    | Centralized Unit             | 中心控制单元                                                    |
|       | SDAP                         |
|       | RRC                          |
|       | PDCP                         | 分组数据汇聚协议（Packet Data Convergence Protocol）            |
| DU    | Distributed Unit             | 分布式工作单元                                                  |
|       | ADPT                         | 自动化数据处理/电信Automated Data Processing/Telecommunications |
|       | RLC                          | 无线链路控制(Radio Link Control)                                |
|       | MAC                          |
| NR-DC | New Radio-Dual Connectivity) |
| Cell  |
主基站是LTE的基站称为MeNB（Master eNodeB）；
主基站是5G NR的基站称为MgNB（Master gNodeB）；
辅基站是LTE的基站称为SeNB（Secondary eNodeB）；
辅基站是5GNR的基站称为SgNB（Secondary gNodeB）。
NR，其全称为New Radio，也被称为新无线/新空口，就是5G的无线网。
DC,Dual Connectivity -- 双连接
Discontinuous Reception -- 非连续性接收 / 间断接收机制







## 缩写
|        |                                                               |                      |
| ------ | ------------------------------------------------------------- | -------------------- |
| AUSF   | Authentication Server Function                                | 认证服务功能         |
| AMF    | Access and Mobility Management Function                       | 访问移动管理功能     |
| DN     | Data Network                                                  | 数据网络             |
|        | e.g. operator services, Internet access or 3rd party services |                      |
| UDSF   | Unstructured Data Storage Function                            | 非结构化数据存储功能 |
| NEF    | Network Exposure Function                                     | 网络曝光功能         |
| I-NEF  | Intermediate NEF                                              | 中级网络曝光功能     |
| NRF    | Network Repository Function                                   | 网络存储功能         |
| NSSF   | Network Slice Selection Function                              | 网络切片选择功能     |
| PCF    | Policy Control Function                                       | 策略管理功能         |
| SMF    | Session Management Function                                   | 会话管理功能         |
| UDM    | Unified Data Management                                       | 统一数据管理         |
| UDR    | Unified Data Repository                                       | 统一数据存储         |
| UPF    | User Plane Function                                           | 用户面功能           |
| UCMF   | UE radio Capability Management Function                       | UE无线点能力管理功能 |
| AF     | Application Function                                          | 应用功能             |
| UE     | User Equipment                                                | 用户设备             |
| (R)AN  | (Radio) Access Network                                        | （无线电）接入网     |
| 5G-EIR | 5G-Equipment Identity Register                                | 5G设备身份注册       |
| NWDAF  | Network Data Analytics Function                               | 网络数据分析功能     |
| CHF    | Charging Function                                             | 充电功能             |

|       |                               |                                                                                                                                                           |
| ----- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MR-DC | Multi-Radio Dual Connectivity | 是把LTE双连接技术扩展到其他RAT，让UE可以同时接入LTE和NR，MN和SN之间通过网络接口连接起来，至少MN要与核心网连接，SN可以与核心网连接，也可以不跟核心网连接。 |
| MN    | Master Node                   | MN提供到核心网的控制面连接，                                                                                                                              |
| SN    | Secondary Node                | SN不提供与核心网的控制面连接，只为UE提供额外的资源。                                                                                                      |








https://blog.csdn.net/zhonglinzhang/article/details/104347486

|         |                                              |
| ------- | -------------------------------------------- |
| Namf    | Service-based interface exhibited by AMF.    |
| Nsmf    | Service-based interface exhibited by SMF.    |
| Nnef    | Service-based interface exhibited by NEF.    |
| Npcf    | Service-based interface exhibited by PCF.    |
| Nudm    | Service-based interface exhibited by UDM.    |
| Naf     | Service-based interface exhibited by AF.     |
| Nnrf    | Service-based interface exhibited by NRF.    |
| Nnssf   | Service-based interface exhibited by NSSF.   |
| Nausf   | Service-based interface exhibited by AUSF.   |
| Nudr    | Service-based interface exhibited by UDR.    |
| Nudsf   | Service-based interface exhibited by UDSF.   |
| N5g-eir | Service-based interface exhibited by 5G-EIR. |
| Nnwdaf  | Service-based interface exhibited by NWDAF.  |
| Ni-nef  | Service-based interface exhibited by I-NEF.  |
| Nchf    | Service-based interface exhibited by CHF.    |
| Nucmf   | Service-based interface exhibited by UCMF.   |


|         |                                               |                                                                                                                                        |
| ------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| PLMN    | Public Land Mobile Network，                  | 公共陆地移动网络                                                                                                                       |
| RPLMN   | Registered PLMN                               | 已登记PLMN                                                                                                                             |
| HPLMN   | Home PLMN                                     | 归属PLMN，终端 USIM 卡上的 IMSI 号中包含的 MCC 和 MNC 与 HPLMN上 的 MCC 和 MNC 是一致的                                                |
| VPLMN   | Visited PLMN                                  | 访问 PLMN，为终端用户访问的 PLMN。其 PLMN 和存在 SIM卡 中的 IMSI 的 MCC，MNC 是不完全相同的。当移动终端丢失覆盖后，一个 VPLMN 将被选择 |
| W-AGF   | Wireline Access Gateway Function              | 无线接入网关功能                                                                                                                       |
| 5G MOCN | 5G Multi-Operator Core Network                |
| TNAP    | Trusted Non-3GPP Access Point                 |
| TNGF    | Trusted Non-3GPP Gateway Function             |
| ATSSS   | Access Traffic Steering, Switching, Splitting | 接入流量导向，转换，拆分                                                                                                               |
| MPTCP   | MultiPath TCP                                 |
| PMF     | Performance Measurement Functionality         |
| TSN     | Time-Sensitive Networking                     |
| EAB     | Extended Access Barring                       | 扩展访问限制                                                                                                                           |
| PPD     | Paging Policy Differentiation                 |
| PPI     | Paging Policy Indicator                       |
| DRX     | Discontinuous Reception                       | 不连续的接收                                                                                                                           |
| NPLI    | Network Provided Location Information         |
| SSC     | Session and Service Continuity Mode           | 会话和服务连续模式                                                                                                                     |
| SSCMSP  | SSC mode selection policy                     |











