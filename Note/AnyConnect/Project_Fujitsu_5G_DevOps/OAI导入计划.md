## 环境构筑
- [ ] 安装操作系统（Ubuntu18.04）
 * 需要换内核（kernel version 5.0.0-23-generic）
- [ ] 安装docker
- [ ] 在docker下安装free5GC
  * [free5gc allinone环境构筑 参考资料](https://github.com/free5gc/free5gc/wiki)
- [ ] 编译OAI代码
  * [OAI环境构筑 参考资料](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/BUILD.md)

---

## 熟悉OAI
### 整体
- [ ] tcpdump 抓取 Cplane 的cap包，梳理流程
  * [OAI流程 参考资料](https://statics.teams.cdn.office.net/evergreen-assets/safelinks/1/atp-safelinks.html)
  * 配套图书：深入理解LTE-A.docx

- [ ] 熟悉整体架构
    * [TS 38.401 NG-RAN; Architecture description](https://www.3gpp.org/ftp/Specs/archive/38_series/38.401/38401-h30.zip)
    * 培训资料：\\\\10.167.14.8\public\BM_开发二部\zhaixin\5G NR社外培训\PART2\221016上午

### 分层
* 熟悉OAI代码，了解各层使用的协议，传输的消息及其作用。
  * **优先级**：RRC & NAS -> NGAP -> F1AP -> PDCP & MAC & RLC
  - [ ] MAC
    * [TS 38.321 NR; Medium Access Control (MAC) protocol specification](https://www.3gpp.org/ftp/Specs/archive/38_series/38.321/38321-h30.zip)
  - [ ] RLC
    * [TS 38.322 NR; Radio Link Control (RLC) protocol specification](https://www.3gpp.org/ftp/Specs/archive/38_series/38.322/38322-h20.zip)
  - [ ] PDCP
    * [TS 38.323 NR; Packet Data Convergence Protocol (PDCP) specification](https://www.3gpp.org/ftp/Specs/archive/38_series/38.323/38323-h30.zip)
  - [ ] RRC
    * [TS 38.331 NR; Radio Resource Control (RRC); Protocol specification](https://www.3gpp.org/ftp/Specs/archive/38_series/38.331/38331-g41.zip)
  - [ ] NAS
    * [TS 24.501 Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3](https://www.3gpp.org/ftp/Specs/archive/24_series/24.501/24501-h90.zip)
  - [ ] NGAP
    * [TS 38.413 NG-RAN; NG Application Protocol (NGAP)](https://www.3gpp.org/ftp//Specs/archive/38_series/38.413/38413-f80.zip)
  - [ ] F1AP
    * [TS 38.473 NG-RAN; F1 Application Protocol (F1AP)](https://www.3gpp.org/ftp//Specs/archive/38_series/38.473/38473-g31.zip)


### 操作
* 熟悉 Uplane 操作
  - [ ] ul ping
  - [ ] dl ping
  - [ ] ul iperf
  - [ ] dl iperf


**PS:**
3GPP资料检索方式：
XX 系列 ：https://www.3gpp.org/dynareport?code=<font color="red">XX</font>-series.htm
eg：
38 系列 ：https://www.3gpp.org/dynareport?code=<font color="red">38</font>-series.htm