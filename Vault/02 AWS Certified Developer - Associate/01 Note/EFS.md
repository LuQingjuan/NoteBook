* Type:
* Tags:
* Date: 20230505
* Related:
* Reference:[]()

## EFS
EFS = Elastic File System

* EFS管理挂载在很多EC2实例上的NFS(network file system) 
* 这些EC2实例也可以位于不同的AZ中。
* 高可用性､可扩展性
* 价格昂贵（gp2 EBS卷的三倍），而且是按次付费。
为EFS文件系统设置了一个安全组。
不同AZ中的实例可以通过EFS同时连接到同一个网络文件系统。

* Use case:
  * 内容管理
  * Web服务
  * 数据共享
  * WordPress
* 内部使用NFSv4.1协议。
* 需要设置一个安全组，用来控制对EFS的访问
* 只兼容基于Linux的AMI，而不兼容Windows。**要注意**
* 可以使用KMS在EFS驱动器中启用静态加密，（KMS是Linux上的标准文件系统。）

* POSIX文件系统（Linux），它有一个标准的文件API。
* EFS将自动扩展容量，EFS中使用的每GB数据都是按使用付费。不需要提前计划容量

* EFS规模：
  * 1000s并发NFS客户端和10GB以上的吞吐量。
  * 自动扩展网络文件系统。
* 性能模式（在EFS网络文件系统创建时设置）
  * General Purpose (default) ：低延迟，如web服务器､cms等。
  * Max I/O：最大限度的提高吞吐量，而且高度并行，但是高延迟。可以满足大数据应用程序或媒体处理需求。
* 吞吐量模式
  * Bursting：1TB意味着 50MiB/s + 加上 100MiB/s的突发。（不必记住这些数字，但只是让你有一个想法。）
  * Provisioned：希望设置吞吐量而不考虑存储大小。
上一个版本的吞吐量随着存储的增加而增长，（通过调配，1 TB的存储达到 1 GiB/s的速度）（可以将吞吐量与存储解除了关联。）
* Elastic：根据工作负载自动向上和向下扩展吞吐量。
  * 读取速度可达3GiB/s，写入速度可达1GiB/s。
  * 工作负载不可预测的情况下使用


存储类：
* Storage Tiers（存储层)
  * 在几天后将文件移动到不同的层。
    * 标准层：用于频繁访问的文件。
    * 不频繁访问层 (EFS-IA)：文件存储在EFS-IA上时，更便宜。
        * 要启用EFS-IA，您必须使用生命周期策略。
        * 假设我们有一些EFS标准的常用文件，但其中一个文件超过60天未被访问。
        * 然后，由于我们共同设置的生命周期策略，文件将移动到不同层中的EFS-IA。
* Availability and durability
  * Standard： Multi-AZ，适合生产场景使用。如果可用性区域关闭，不会影响EFS文件系统。
  * One Zone：适合开发场景使用。仅在一个AZ中，默认启用备份。而且它仍然与不常访问的存储层兼容。

可节省约90%的成本。