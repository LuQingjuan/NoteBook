## Project
### 环境
![[Environment]]

- [x] L5G CI 同时查看手机电池和CPU温度
    xml中`UE_Battery_Temperature`变为`UE_Temperature`
    ```
    branch:L5G_CI_develop
    commit:66c835966a5269d8c43e2cee54d47e6a70509d22
    ```
    - [ ] 验证命令`adb -s ' + device_id + ' shell dmesg | grep temperature | awk '{print $6}'`
    - [ ] 验证机能
- [x] L5G CI 查看手机电量、电池和CPU温度的时候，如果结果获取失败，显示命令执行的输出信息
    ```
    branch:L5G_CI_develop
    commit:d5007fdd949219160aa63d066366c91c477dcfec
    ```
    - [ ] 验证机能

## 云奥

## 学习
#### SONiC
- [ ] ![[SONiC#SONiC|SONiC]]

#### AWS
- [ ] ![[AWS Certified Developer Associate#笔记|AWS Certified Developer Associate]]

## 生活