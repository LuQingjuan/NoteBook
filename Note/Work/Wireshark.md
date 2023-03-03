|               |                    |
| ------------- | ------------------ |
| iflog.pcap    | DU内部（卡间消息） |
| iflogF1C.pcap | DU-CU间消息        |
| invd_UEMR.log | 异常log            |
| seq_uemr.log  | DU内部log          |


|     |     |                                |                                                   |                      |
| --- | --- | ------------------------------ | ------------------------------------------------- | -------------------- |
| F1C | 4   | RRC Setup Request              | frame.time == "2022-11-30 17:01:36.483067+0800"   |
| F1C | 17  | RRC Release                    |
| F1C | 18  | UEContextReleaseComplete       | frame.time == "2022-11-30   17:01:36.853641+0800" |
| F1C | 20  | RRC Setup Request              | frame.time == "2022-11-30   17:01:37.642081+0800" |
| F1C | 30  | RRC Reconfiguration Complete   | frame.time == "2022-11-30   17:01:37.861081+0800" |
|     | 101 | L1 Sgnb Add UE Set Indication  | frame.time == "Nov 30, 2022 17:03:49.895994000"   |
|     | 103 | SCD Sgnb Add UE Set Indication | frame.time == "Nov 30, 2022 17:03:49.896059000"   | frame[92:2] == 02:00 |
| F1C | 35  | RRC Reestablishment Request    | frame.time == "2022-11-30   17:03:49.897136+0800" |
| F1C | 37  | RRC Reestablishment Complete   | frame.time == "2022-11-30   17:03:49.956179+0800" |
| F1C | 40  | RRC Release                    |




```mermaid
graph LR %%left->right
A(过滤器) --> B(抓包过滤器) & C(显示过滤器)
```
|                        |               |                 |              |                               |      |      |     |
| ---------------------- | ------------- | --------------- | ------------ | ----------------------------- | ---- | ---- | --- |
| 抓包过滤器             |               |                 |              |                               |
| 类型Type               | 主机（host）  | 网段（net）     | 端口（port） |
| 方向Dir                | 源地址（src） | 目标地址（dst） |              |
| 协议Proto 各种网络协议 | ether         | ip              | tcp          | udp                           | http | icmp | ftp |
| 逻辑运算符             | 与（ && ）    | 或（\|\| ）     | 非（ ！）    |
| 显示过滤器             |               |                 |              |                               |      |      |
| IP地址                 | ip.addr       | ip.src          | ip.dst       |
| 端口                   | tcp.port      | tcp.srcport     | tcp.dstport  |
| 协议                   | tcp           | udp             | http         |
| 比较运算符             | >             | <               | ==           | >=                            | <=   | !=   |
| 逻辑运算符             | and           | or              | not          | xor（有且仅有一个条件被满足） |
