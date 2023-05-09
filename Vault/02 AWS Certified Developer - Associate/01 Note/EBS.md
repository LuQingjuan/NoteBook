* Type:
* Tags:
* Date: 20230505
* Related:
* Reference:[]()

## EBS Volume
EBS Volume = Elastic Block Store Volume
弹性块存储，是一个网络驱动器。看作**网络U盘**


* 在实例运行时将其连接到实例上
* 在实例终止后，可以重新创建一个实例，并装载到之前的EBS卷，然后我们就可以取回EBS卷上的数据
* 在CCP级别，这些EBS卷一次只能装载到一个实例。
* 我们不能创建EBS卷，它被绑定到特定的可用性区域。
* 该功能为我们每月提供30 GB的免费EBS存储。


在本课程中，我们将在GP2到GP3卷中使用此功能。
现在让我们来看看。
* EBS卷是网络驱动程序，而不是物理驱动器
  * 通过网络与其他的实例通信，存在延时。
  * 但是可以非常快速地从一个实例分离并连接到另一个实例。
    * 当您要执行故障切换时，这会使它变得非常方便。
* EBS卷被锁定到特定的AZ(Availability Zone可用性区域)，
  * 它是在us-east-1a中创建的，则无法连接到us-east-1b
  * 通过快照，在不同的可用性区域之间移动卷。

* 当EC2实例被终止时，它控制EBS行为。（Termination attribute）
  * 根EBS卷将与被终止的实例一起删除，因为默认情况下它是启用的
  * 其他连接的EBS卷都不会被删除，因为默认情况下它是禁用的。
* 我们可以控制是否要启用或禁用终止时删除。
  * 如果您希望在终止实例时保留根卷（例如，为了保存一些数据），
  * 可以禁用根卷的终止时删除，这样就可以很好地进行操作。
  这可能是**考试**时的一个**考试**场景。

### EBS Types
* 通用SSD卷（General purpose SSD volume）
  * 针对各种工作负载平衡而设计。性价比高。
  * gp2
  * gp3
* 高性能SSD卷（Highest-performance SSD volume）
  * 性能最高，针对用于关键型､ 低延迟和高吞吐量的工作而设计。
  * io1
  * io2
* 其低成本HDD卷（Low cost HDD volume）
  * 针对频繁访问的吞吐量密集型工作负载而设计。
  * stl
* （Lowest cost HDD volume）
  * 成本最低，针对访问频率较低的工作负载而设计。
  * scl

* EBS卷选择需要从大小､ 吞吐量和IOPS, IOPS (I/O Ops Per Sec)这个因素考虑，
* 如果有疑问，可以查阅文档。
* 对于EC2实例，只有gp2和gp3以及io1和io2可以用作引导卷。
这意味着根操作系统将在哪里运行。
现在，让我们更深入地了解一下gp2､ gp3､ io1､ io2和其他一些函数。
但是gp2､ 通用和调配的IOPS将是您**考试**中最重要的部分。

| Type                         |                                                                                                                                      | Size             | EC2 instances | Throughput             | IOPS         | © Stephane Maarek |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------- | ---------------------- | ------------ |
| General Purpose SSD          | 高性价比、低延迟的存储<br>可用于系统启动卷､虚拟桌面､ 开发和测试环境。                                                                |                  |               |                        |              |
| gp3                          | 较新一代的卷<br>可以独立设置IOPS和吞吐量                                                                                             | 1 GiB - 16 TiB   |               | 125 MiB/s - 1000 MiB/s | 3000 - 16000 |
| gp2                          | 较旧的版本<br>IOPS和卷大小是相互关联 3IOPS:1GB                                                                                       | < 5334GB         |               |                        | < 16000      |
| Provisioned IOPS (PIOPS) SSD | 需要持续IOPS性能的关键业务<br>或需要16000 IOPS以上的应用程序<br>适合数据库工作负载（对存储性能和一致性敏感）<br>支持EBS Multi-attach |                  |               |                        |              |
| io1/io2                      | 可以独立于存储大小增加PIOPS<br>io2具有更高的耐用性和更高的IOPS/GiB（与io1价格相同）                                                  | 4 GiB - 16 TiB   | Nitro         |                        | < 64000      |
|                              |                                                                                                                                      |                  |               |                        | < 32000      |
| io2 Block Express            | Sub-millisecond延迟<br>IOPS和卷大小是相互关联 1000IOPS:1GB                                                                           | 4 GiB–64 TiB     |               |                        | < 256000     |
| st1                          | 不能做启动卷<br>适合大数据､数据仓库存储和日志处理                                                                                                                         | 125 GiB - 16 TiB |               | < 500 MiB/s            | < 500        |
| sc1                          | 不能做启动卷<br>                                                                                                                         | 125 GiB - 16 TiB |               | < 250 MiB/s            | < 250        |
**考试**中请记住:
* 如果您需要持续IOPS性能的关键业务应用程序或需要超过**16000 IOPS**的应用程序，从gp2或gp3卷切换到io1或io2卷。
* 如果想获得超过**32000 IOPS**的性能，则需要使用带io1或io2的EC2 Nitro。
* [详细数据](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)

### EBS Multi-Attach
* 同一个AZ上IO1和IO2系列的EBS卷可以连接多个EC2实例。
* 这些实例可以同时对这个EBS Volume 进行读写操作。
* Use case
  * 在集群Linux应用程序中实现更高的应用程序可用性（例如：Teradata）
  * 应用程序必须管理并发写入操作
* 一次最多可以附加16个EC2实例。（这是**考试**时必须知道的。所以要小心这个16号。）
* 文件系统必须支持集群。（不是XFS, EXT4）
