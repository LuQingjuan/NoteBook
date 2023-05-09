* Type:
* Tags:
* Date: 20230507
* Related:
* Reference:[]()

## AMI
AMI = Amazon Machine Image
* Amazon机器映像，是EC2实例的定制。
  * 创建自己的AMI时，可以定制自己的软件、配置、操作系统、监视工具
  * boot和配置时间更快，因为我们希望安装到EC2实例上的所有软件都将通过AMI预打包。
* 必须在**specific region**（与所有的Region都不一样）构建AMI
  * 为了可以跨区域复制它们。
* 从不同类型的AMI启动EC2实例。
  * 公共AMI：由AWS提供。（Amazon Linux）
  * 自己提供的：我们可以创建自己的AMI，自己创建和维护它们。（一些工具可以实现自动化）。
  * AWS Marketplace AMI：其他人创建的AMI，可能由其他人销售。
    * AWS上的供应商通常会创建自己的AMI或具有良好配置的软件等，然后他们将通过AMI市场进行销售。
    * 普通用户也可以在AWS市场上创建一个销售AMI的业务。

EC2实例中的AMI进程是如何工作的？
* 我们将启动一个EC2实例，并对其进行自定义。
* 停止该实例，以确保数据完整性正确。
* 根据该实例构建AMI，还可以在后台创建EBS快照。
* 从其他AMI启动实例，

