* Type:
* Tags:
* Date: 2023-03-29 09:52:17
* Related:
* Reference:[]()

## EC2
EC2 = Elastic Compute Cloud
通过EC2提供基础架构服务

### 提供的服务
* 租用虚拟机（EC2）
* 在虚拟机上存储数据（EBS）
* 负载均衡（ELB）
* 扩展服务（ASG）

云可以在你需要时按时按需租用

### EC2配置
* 需用的虚拟机OS[Linux Windows Mac]
* CPU：多少算力和多少内核
* RAM：随机存取内存大小
* 存储空间大小
  * EBS ＆ EFS：网络
  * 硬件 EC2 Instance Store
* 网卡：网速 公共IP
* 防火墙规则：安全组
EC2用户数据脚本：引导脚本（第一次启动时配置实例）

### EC2 User Data
* 创建EC2实体 bootstrap 时，使用EC2 User Data
* bootstrap：在机器启动时启动命令
* 这个脚本仅在第一次创建实体时运行。
* 脚本中可以添加的操作
  * 安装更新
  * 安装软件
  * 下载文件
* EC2 User Data 只能通过 root 身份运行

## Instance
### 命名约定：
m5.2xlarge
m：实例类
5：版本
2xlarge：大小，越大占用的CPU越大


### [实例类型](https://aws.amazon.com/ec2/instance-types/)
* 通用 General Purpose （micro t2）
  * 各种不同的工作负载，需要平衡 计算、内存和网络资源。
  * Use cases
    * Web 服务器
    * 代码存储库
* 计算优化型 Compute Optimized
  * 非常出色的CPU和计算能力。
  * Use cases
    * 批处理工作负载
    * 媒体转码
    * 高性能 Web 服务器
    * 高性能计算 (HPC)High Performance Computing
    * 科学建模
    * 专用游戏服务器
    * 广告服务器引擎
    * 机器学习推理
    * 其他计算密集型应用程序
  * 命名（不需要记忆）
    * C：Compute
* 内存优化型 Memory Optimized
  * 在内存RAM中处理大型数据集的工作负载的性能。(数据库，缓存……)
  * Use cases
    * 高性能关系或非关系数据库
    * 内存数据库
    * 分布式web级缓存存储
    * 弹性缓存
    * 商业智能
    * BI（Business intelligence）优化的内存数据库
    * 执行大型非结构化数据库真实的应用程序
  * 命名（不需要记忆）
    * R:RAM
    * X
    * Z
* 加速计算 Accelerated Computing
  * 加速计算实例使用硬件加速器或协同处理器来执行浮点数计算、图形处理或数据模式匹配等功能，比使用在 CPU 上运行的软件更高效。
  * 这些实例适用于
* 存储优化 Storage Optimized
  * 对本地存储上的大型数据集进行高速连续读写访问的工作负载。
  * 它们经过了优化，每秒可以向应用程序交付数以万计的低延迟、随机 I/O 操作 (IOPS)。
  * Use cases
    * 高频率的在线事务处理 OLTP（Online transaction processing）
    * 关系数据库和NoSQL数据库
    * 内存中的数据库缓存（Redis）
    * 数据仓库应用程序
    * 分布式文件系统
  * 命名（不需要记忆）
    * I
    * G
    * H
* HPC优化（高性能计算优化）
  * 高性能计算（HPC）实例专为在 AWS 上大规模运行 HPC 工作负载提供最佳性价比而构建。HPC 实例特别适用于从高性能处理器（如大型复杂模拟和深度学习工作负载）中受益的应用程序。
* 实例特征  Instance Features
* 衡量实例性能  Measuring Instances Performance


### [实例比较](https://instances.vantage.sh/)

## Security
* 控制流量进出 EC2 实例
* 只包含允许规则
* 入栈出栈规则
* 规则可以包含其他规则
* 一个实例可以有多个安全组
* 一个安全组可以给多个实例使用

* Inbound rules（入站规则）：允许外部连接到EC2实例的规则
* OutBound rules（出站规则）：
* 可以将任意多个安全组附加到一个安全组
* 可以将任意多个EC2 实例附加到一个安全组

### 采购选项

| Type                  |                  | 工作负载           | discount |                                                                          | Use Case           |                                                                                                                               |     |
| --------------------- | ---------------- | ------------------ | -------- | ------------------------------------------------------------------------ | ------------------ | ----------------------------------------------------------------------------------------------------------------------------- | --- |
| On Deemand            | 按需实例         | 短期               | 100%     | 可预测的定价<br>按秒支付                                                 |                    | coming and staying in resort whenever we like, we pay the full price                                                          |
| Reserved              | 保留实例         | 长期 (1 & 3 years) | 72%      |                                                                          | 要长时间运行数据库 | like planning ahead and if we plan to stay for a long time, we may get a good discount.                                       |
| Convertible Reserved  | 可转换的保留实例 | 长期 (1 & 3 years) | 66%      | 随时间推移改变                                                           |                    |
| Savings Plans         | 储蓄计划         | 长期(1 & 3 years)  | 72%      | 它们更加现代化，为不是承诺特定的实例类型，而是承诺以美元为单位的特定使用量 |                    | pay a certain amount per hour for certain period and stay in any room type (e.g.，King, Suite, Sea View，...)                 |
| Spot Instances        | 现货实例         | 非常短             | 90%      | 非常非常便宜<br>可靠性差:随时都可能丢失这些实例                          |                    | the hotel allows people to bid for the empty rooms and the highest bidder keeps the rooms. You can get kicked out at any time |
| Dedicated Hosts       | 专用主机         |                    | 最昂贵   | 最贵<br>整个物理服务器<br>控制实例位置                                   |                    | We book an entire building of the resort                                                                                      |
| Dedicated Instances   | 专用实例         |                    |          | 没有其他客户会共享您的硬件                                               |                    |
| Capacity Reservations | 容量预存         |                    |          | 在特定AZ中为任何持续时间预留容量                                         |                    | you book a room for a period with full price even you don’t stay in it                                                        |


#### On Demand（按需实例 | 短期）
* 为使用的东西付费。
  * Linux或Windows，在第一分钟后按秒计费
  * 其他操作系统，按小时计费。
* 它的成本最高，但没有预付款，也没有长期承诺。
* Use Case
  * 对于短期和不间断的工作负载，(无法预测应用程序的行为)

#### Reserved（保留实例 | 长期 (1 & 3 years)）
* 提供72%的折扣。
* 保留了一个特定的实例属性。(实例类型､区域､租赁､OS)
* 预订期(Reservation Period)：一年或三年，时间越长折扣大
* 预付款(Payment Options)：支付越多折扣越大（不预支付、部分预支付、全额预支付）
* 范围(Scope)： Regional or Zonal ？在特定的AZ（Availability Zone）中保留容量。
* Use Case
  * 稳定状态使用的应用程序，例如，用于数据库。
* 可以在市场中买卖保留实例

#### Convertible Reserved（可转换的保留实例 | 长期 (1 & 3 years)）
* 可以更改实例类型（实例系列 操作系统､ 范围和租约）
* 灵活性更大，所以折扣更少，最多可获得66%的折扣。

#### Savings Plans（储蓄计划 | 长期(1 & 3 years)）
* 与保留实例一样，提供72%的折扣。
* 储蓄计划，在未来1 & 3 years每小时花费一定的金额（$10/hour）
* 超出储蓄计划的使用都将以按需(On Deemand)价格计费。

* 被锁定到特定的实例家庭和地区。(在us-east-1中建立M5类型的例证族群。)
* 灵活选择
  * 实例大小（在m5.xlarge, m5.2xlarge等之间切换）
  * 操作系统（在Linux和Windows等之间切换）
  * 租赁（在主机､ 专用、默认之间切换）

#### Spot Instances（现货实例 | 短期）
* 提供90%的折扣。
* 可靠性差:随时都可能丢失这些实例，如果现货实例价格超过你愿意为现货实例支付的最高价格，那么你就会失去它。
* 是AWS中最经济高效的实例，如果您的工作负载具有故障恢复能力，它们将非常有用。
* Use Case
  * 批处理作业
  * 数据分析
  * 图像处理
  * 任何类型的分布式工作负载
  * 具有灵活的开始和结束时间的工作负载
* 不适合关键的工作或数据（考试将在这方面对你进行测试。）Not suitable for critical jobs or databases

#### Dedicated Hosts（专用主机 | 短期 or 长期(1 & 3 years)）
* 可以独享一台具有EC2实例容量的物理服务器
* 有合规性要求
* 需要使用现有的服务器绑定软件许可证
* 基于每插槽､ 每内核､每虚拟机软件许可证进行计费
* 购买
  * 按需购买，按秒付费
  * 预订一年或三年（不预支付、部分预支付、全额预支付）
* 最昂贵，因为您实际上需要预留一台物理服务器。
* Use Case
  * 您的软件采用自带许可证的许可模式。
  * 您的公司有很强的法规或合规性需求。

#### Dedicated Instances（专用实例）
* 实例运行在专用于您的硬件上，这与物理服务器不同。
* 与同一帐户中的其他实例共享硬件，并且无法控制实例的位置。
* Dedicated Hosts **VS** Dedicated Instances
  * 专用实例意味着你在自己的硬件上有自己的实例。
  * 专用主机意味着你可以访问物理服务器本身，它让你可以看到较低级别的硬件。

#### Capacity Reservations（预留容量）
* 没有折扣。
* 可以在任意持续时间内保留特定AZ中的按需实例。
* 可以在需要时随时访问该容量。
* 您可以随时保留容量或取消保留。
* 唯一的目的是保留容量。
* 要将其与区域保留实例或您的储蓄计划相结合，可以获得计费折扣。
* 无论实例是否运行，都需要为预留容量按需付费。
* 非常适合需要在特定AZ中运行的短期不间断工作负载。

#### 哪种购买选择适合我
拿度假村来打个比方：
**On Demand**：付全价，你可以随时来度假村。
**Reserved**：你提前预定固定服务（房型，温泉……），一年，三年，得到一个很好的折扣，因为我知道你会呆很长时间；根据你的预支付方式（不预支付、部分预支付、全额预支付）可以给你一个很好的折扣
**Convertible Reserved**：你提前预定可调节的服务，度假过程中可以改变房间类型等。
**Savings Plans**：我承诺在度假村每个时间断花费固定金额，过程中可以改变房间类型等，超出部分另外支付。
**Spot**：度假村清库存空房间，捡漏，折扣较大，但是如果有人愿意为你的房间付比你所付的更多的钱，你随时都可以被踢出去。
**Dedicated Hosts**：把度假村包场了，我的地盘我说了算。
**Dedicated Instances**：度假村包了部分场地，被安排在一块区域，私密性比较好。
**Capacity Reservations**：全款订专属包间，我不去房间也给我留着。可以结合Reserved和Savings Plans得到一点折扣


| Price Type                             | Price (per hour)                           |
| -------------------------------------- | ------------------------------------------ |
| On-Demand                              | $0.10                                      |
| Dedicated Host                         | On-Demand Price                            |
| Capacity Reservations                  | On-Demand Price                            |
| Dedicated Host Reservation             | Up to 70% off                              |
| Reserved Convertible Instance (1 year) | $0.071 (No Upfront) - $0.066 (All Upfront) |
| Reserved Instance (1 year)             | $0.062 (No Upfront) - $0.058 (All Upfront) |
| EC2 Savings Plan (1 year)              | $0.062 (No Upfront) - $0.058 (All Upfront) |
| Reserved Instance (3 years)            | $0.043 (No Upfront) - $0.037 (All Upfront) |
| Spot Instance (Spot Price)             | $0.038 - $0.039 (up to 61% off)            |
