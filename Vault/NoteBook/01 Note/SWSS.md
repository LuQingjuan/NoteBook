* Type:
* Tags:
* Date: 2023-03-28 13:08:45
* Related:
* Reference:[]()

## SWSS
SWSS （switch state service）是一套工具，用于协调所有SONiC模块之间、模块与redis引擎之间的通信。swss还承载以下服务，这些服务通过netlink与SONiC应用层交互（在其他容器中运行的进程除外，即fpmsyncd、teamsyncd和lldp_syncd）。下面的前三个服务（portsyncd、intfsyncd、neighsyncd）将状态推送到redis引擎，而最后三个服务（orchagent、intfMgrd、vlanMgrd）从引擎收集状态，并重新发布状态到应用。

    portsyncd :侦听与端口相关的netlink事件。当交换机启动时，portsyncd解析交换机的硬件配置文件以获取物理端口信息，然后将收集的状态推送到APPL_DB中。portsyncd 设置端口速度、lane和MTU，并将状态注入状态数据库。
    intfsyncd ：侦听与接口相关的netlink事件，并将收集的状态推送到APPL_DB中。intfsyncd还管理与接口关联的新的或更改的IP地址等元素。
    neighsyncd ：侦听新发现的邻居由于ARP处理而触发的与邻居相关的netlink事件，并将收集的状态推送到APPL_DB中。neighsyncd管理诸如MAC地址和邻居地址族之类的属性，并最终构建数据平面中用于二级重写目的所需的邻接表。
    teamd: 链接聚合（LAG）容器，它提供了在SONiC交换机上配置绑定的功能。teamd服务是LAG协议的一个基于Linux的开源实现。teamsyncd服务管理teamd和southbound子系统之间的交互。
    orchagent ：swss子系统中最关键的组件。orchagent提取各种syncd服务注入的所有相关状态，相应地处理和发送这些信息，最后将其推送到ASIC_DB。orchagent在这些服务中是独一无二的，因为它既是消费者（如从APPL_DB获取状态）又是生产者（如推进ASIC_DB）。
    intfMgrd ：对来自APPL_DB、CONFIG_DB和state_DB的状态作出反应，以配置Linux内核中的接口，前提是所监视的任何数据库中没有冲突或不一致的状态。
    vlanMgrd ：对来自APPL_DB、CONFIG_DB和state_DB的状态作出反应，以在Linux内核中配置VLAN，前提是所监视的任何数据库中没有冲突或不一致的状态。

相关的模块功能角色总结如下：

    xxx-mgrd ： 对来自APPL_DB、CONFIG_DB和state_DB的状态作出反应，以配置linux内核中的接口。
    xxx-syncd： 侦听与内核相关的netlink事件，并将收集的状态写入APP_DB。
    orchagent： swss子系统中最关键的组件。orchagent提取各种syncd服务注入的所有相关状态，相应地处理和发送这些信息，最后将其推送到ASIC_DB。orchagent在这些服务中是独一无二的，因为它既是消费者（如从APPL_DB获取状态）又是生产者（如推进ASIC_DB）。
