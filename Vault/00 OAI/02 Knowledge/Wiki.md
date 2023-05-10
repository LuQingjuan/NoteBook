
## mmWave(band257) RFSIM
10.167.14.32 jftt/jftt

### ビルド
git clone http://10.167.14.30:8081/gitlab/training/mtc-oai.git
cd openairinterface5g
git checkout feature_mmWave_nfapi_f1ap
source oaienv
cd cmake_targets
sudo -E ./build_oai --gNB --nrUE -x -c -w None

### free5GC起動
cd ~/work_jftt/xues/free5gc-compose
docker-compose -f docker-compose-build.yaml up

* AMF IPアドレス確認
docker inspect amf ※AMFのIPアドレスをgNB(CU) configファイルの「【amf_ip_address = ( { ipv4 =】に設定

* UPF IPアドレス確認
docker inspect upf　　　※UPFのIPアドレスをU-Plane疎通時に使用

### 分離なし+RFSIM
* OAI-gNB:
sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa --nokrnmod -O gnb.band257.tm1.66PRB.usrpn300.conf --log_config.ASN1_debug
* OAI-nrUE:
sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem -r 66 --numerology 3 --band 257 -C 27947520000 --rfsim --sa --nokrnmod -O ue.conf --ssb 576 --log_config.ASN1_debug

### CUDU分離＋RFSIM
* OAI-CU：
sudo ./ran_build/build/nr-softmodem --rfsim --sa -O gNB_SA_CU_fr2_band257.conf --log_config.ASN1_debug
* OAI-DU:
sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa -O gNB_SA_DU_fr2_band257.conf --log_config.ASN1_debug
* OAI-nrUE:
sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem -r 66 --numerology 3 --band 257 -C 27947520000 --rfsim --sa --nokrnmod -O ue.conf --ssb 576 --log_config.ASN1_debug

### nFAPI分离(L1/L2分離)+RFSIM：
* OAI-gNB(VNF):
sudo ./ran_build/build/nr-softmodem --sa -O gnb.band257.tm1.66PRB.nfapi.conf --nfapi VNF --log_config.ASN1_debug
* OAI-gNB(PNF):
sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa -O oaiL1.nfapi.usrpx300.conf --nfapi PNF --log_config.ASN1_debug
* OAI-nrUE:
sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem -r 66 --numerology 3 --band 257 -C 27947520000 --rfsim --sa --nokrnmod -O ue.conf --ssb 576 --log_config.ASN1_debug

### CU* DU分離＋DU(nFAPI分離)＋RFSIM：
* Proxy起動
git clone http://10.167.14.30:8081/gitlab/training/episci.git
cd oai-lte-multi-ue-proxy
git checkout mtc-oai-episci
make ※１回のみ実施
sudo -E ./build/proxy 1 --nr ※1 は起動UE数
* OAI-CU：
sudo ./ran_build/build/nr-softmodem --sa -O gNB_SA_CU_fr2_band257.conf --log_config.ASN1_debug
* OAI-DU（VNF)：
sudo ./ran_build/build/nr-softmodem --sa -O gNB_SA_DU_fr2_band257_nfapi.conf --nfapi VNF --emulate-l1 --log_config.ASN1_debug
* OAI-nrUE(PNF):
sudo -E ./ran_build/build/nr-uesoftmodem -O proxy_ue.conf --nfapi STANDALONE_PNF --node-number 2 --sa --emulate-l1 --nokrnmod 1 --numerology 3 -r 66 --ssb 576 -C 27947520000 --log_config.ASN1_debug

### 参数
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
