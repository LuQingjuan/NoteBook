## [mtc-oai代码](http://10.167.14.30:8081/gitlab/training/mtc-oai/tree/feature_mmWave_nfapi_f1ap)
### 编译
`sudo -E ./build_oai --gNB --nrUE -x -c -w None`

### 运行
#### RFSIM：
GNB
`sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa --nokrnmod -O gnb.band257.tm1.66PRB.2x2.usrpn300.conf --log-mem gnb`
UE
`sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem --rfsim --sa --nokrnmod -O ue.conf -r 66 --numerology 3 --band 257 -C 27947520000 --ssb 576 --ue-nb-ant-rx 2  --ue-nb-ant-tx 2 --log-mem ue`

#### CU/DU分离+RFSIM：
CU
`sudo ./ran_build/build/nr-softmodem --rfsim --sa -O gNB_SA_CU_fr2.conf`
DU
`sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa -O gNB_SA_DU_fr2.conf`
UE
`sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem --rfsim --sa --nokrnmod -O ue.conf -r 66 --numerology 3 --band 261 -C 27547560000 --ssb 168`

#### nFAPI分离+RFSIM：
VNF
`sudo ./ran_build/build/nr-softmodem --sa -O gnb.band261.tm1.66PRB.nfapi.conf --nfapi VNF`
PNF
`sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa -O oaiL1.nfapi.usrpx300.conf --nfapi PNF`
UEUE
`sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem --rfsim --sa --nokrnmod -O ue.conf -r 66 --numerology 3 --band 261 -C 27547560000 --ssb 168`

#### 参数
* **common**
    * --rfsim    : RFSIM
    * --sa       : 独立组网
    * --nokrnmod :
    * -O **.conf : 配置文件
    * --log-mem  : 显示log [gnb ue]
* **gnb**
* **ue**
    * -r 106
        ```
        grep "dl_carrierBandwidth" gnb.band78.sa.fr1.106PRB.2x2.usrpn310.conf 
                dl_carrierBandwidth                                            = 106;
        ```
    * --numerology 3
        ???
    * --band 78
        ```
        jftt@jftt:~/work_jftt/lu/mtc-oai/cmake_targets$ grep "bands" gnb.band78.sa.fr1.106PRB.2x2.usrpn310.conf
                bands          = [78];
        ```
    * -C 3319680000
        ```
        [NR_MAC]   Set RX antenna number to 2, Set TX antenna number to 2 (num ssb 1: 80000000,0)
        [NR_MAC]   Setting TDD configuration period to 6
        [NR_MAC]   TDD has been properly configurated
        DL frequency 3319680000: band 77, UL frequency 3319680000
        ```
    * --ue-nb-ant-rx 2
        对应 GNB config 中 `RUs` `nb_rx`
    * --ue-nb-ant-tx 2
        对应 GNB config 中 `RUs` `nb_tx`
    * --ssb 168
        ???
    ```
#### Iperf
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

#### Ping
**UL ping**
`ping -I oaitun_ue1 10.100.200.2`
    