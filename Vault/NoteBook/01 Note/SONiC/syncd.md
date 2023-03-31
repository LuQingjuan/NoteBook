* Type:
* Tags:
* Date: 2023-03-28 13:10:01
* Related:
* Reference:[]()

## syncd
将交换机的网络状态与ASIC同步，这包括ASIC当前状态的初始化、配置和收集。主要逻辑组件包括：

    syncd：执行同步逻辑的进程。在编译时，syncd与ASIC SDK库链接，并将从接口收集的状态注入ASIC。syncd订阅ASIC_DB以接收来自swss参与者的状态，并将来自硬件的状态推回ASIC_DB。
    SAI API：交换机抽象接口（SAI）定义了API，以提供独立于供应商的方式来控制转发元素，如交换ASIC、NPU或软件交换机。
    ASIC SDK：驱动ASIC所需SDK的SAI兼容实现。SDK钩住syncd，syncd 负责驱动其执行。
