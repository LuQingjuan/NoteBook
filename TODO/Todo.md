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

#### 20230426
试一下 用 http://10.167.14.30:8081/gitlab/training/mtc-oai/tree/feature_mmWave_nfapi_f1ap 代码跑一下DL:2Layer， UL :2Layer的RFSIM 和 iperf
- [X] 先用band78， 可以参考 ci-scripts\conf_files\gnb.band78.sa.fr1.106PRB.2x2.usrpn310.conf 这个配置文件。
    **编译**
    `sudo -E ./build_oai --gNB --nrUE -x -c -w None`
    **启动RFSIM**
    ```
    $ sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa --nokrnmod -O gnb.band78.sa.fr1.106PRB.2x2.usrpn310.conf
     --gNBs.[0].min_rxtxtime 5 --usrp-tx-thread-config 1 --tune-offset 30000000 --thread-pool 1,3,5,7,9,11,13,15 --gNBs.[0].min_rxtxtime 5

    $ sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3319680000 --rfsim --sa --nokrnmod -O ue.conf
    ```
    **DL**
    ```
    $ iperf -s -u -i 1 -B 60.60.0.1 -p 5001

    $ docker exec -it upf bash
    $ iperf -u -b 80M -t 5 -i 1 -p 5001 -c 60.60.0.1

    34M
    ```
    **UL**
    ```
    $ docker exec -it upf bash
    upfd# iperf -s -u -i 1 -p 5001

    $ iperf -u -b 128M -t 5 -i 1 -p 5001 -c 10.100.200.2 -B 60.60.0.6

    12.4M
    ```

- [X] 再试试 在 cmake_targets\gnb.band257.tm1.66PRB.usrpn300.conf 这个文件上改一个 DL:2Layer， UL:2Layer的config文件 试试band257的2x2 的 RFSIM 和iperf
    **启动RFSIM**
    ```
    $ sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa --nokrnmod -O gnb.band257.tm1.66PRB.2x2.usrpn300.conf --log-mem gnb
    
    $ sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem -r 66 --numerology 3 --band 257 -C 27947520000 --rfsim --sa --nokrnmod -O ue.conf --ssb 576 --ue-nb-ant-rx 2  --ue-nb-ant-tx 2 --log-mem ue
    ```
    **DL**
    ```
    $ iperf -s -u -i 1 -B 60.60.0.8 -p 5001

    $ docker exec -it upf bash
    $ iperf -u -b 8M -t 10 -i 1 -p 5001 -c 60.60.0.8

    8M
    ```
    **UL**
    ```
    $ docker exec -it upf bash
    upfd# iperf -s -u -i 1 -p 5001

    $ iperf -u -b 2M -t 10 -i 1 -p 5001 -c 10.100.200.3 -B 60.60.0.8

    2M
    ```

## 云奥

## 学习
#### SONiC
- [ ] ![[SONiC#SONiC|SONiC]]

#### AWS
- [ ] ![[AWS Certified Developer Associate#笔记|AWS Certified Developer Associate]]

## 生活