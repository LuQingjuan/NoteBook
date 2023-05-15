## Project
### 2023-04-26
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

    **UL ping**
    `ping -I oaitun_ue1 10.100.200.2`

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

### 2023-04-06
资料做成：
	测试手顺资料做成
		D:\SVN\01-ワークライブラリー\vRAN\07_検討資料\18_CI自動化\05_Radisys\Radisys_試験項目_8E_CIシナリオ.xlsx
	项目说明材料做成：
		D:\Git\L5G_CI\doc\L5GC_CI2_dev_6a2dbc32b26ea31fece3b33a93fa81e88cb9a845\pythonスクリプト構造資料_20230411.xlsx

### 2023-03-08
今連絡しようとしていました。CI#1系を使用してもらって大丈夫です。(今から使ってもらって大丈夫です。)環境は10.38.223.151の以下のパスにあるconfig.iniのままで大丈夫とのことです。/home/l5g/CI_Config/CI1 先週確認してもらった、以下の2件について本番のブランチ(L5G_ST_CI1)にマージして動作確認をしてほしいです。　
- [x] ログ取得時にCI試験で使用したCIconfigとxmlを一緒に回収するようにする(本番ブランチへのマージ)　
branch:L5G_ST_CI1
commit:315896bee7a2573af389b0305c0ccfeced8670a9
http://10.38.223.151:8080/job/L5G_ST_CI1/8699/

- [x] iperf結果のグラフ名を変更する(グラフの並びが試験内容ごとに固まって表示されるようにする)。
branch:L5G_ST_CI1
commit:2f5f7a9948ffb96aa8e30405d83b36f159c83f7f
http://10.38.223.151:8080/job/L5G_ST_CI1/8700/

あと、CI#1系は今日使用予定ないみたいなので、継続して使うことは可能です。 以下の件について、お試しで動かす時は本番ブランチではなく、開発用のブランチ（L5G_ST_CI1_dev）で試して下さい。
- [x] (**ok**)端末温度の取得。今は端末の電池残量を出力してる。それ以外に、端末の温度も出力したい。
branch:L5G_ST_CI1
commit:d06340833aed94e00a031121b42761b312ea9eec
http://10.38.223.151:8080/job/L5G_ST_CI1/8701/console
```
New Test Action:
Show UE Battery:             UE_Battery
Show UE Battery Temperature: UE_Battery_Temperature
```
```
[2023-03-08 15:05:35,057] root:INFO: ADB[10.38.2.199]    UE[5c3b02a] Battery Temperature: 23.0℃
[2023-03-08 15:05:35,176] root:INFO: ADB[10.38.2.199]    UE[97703146] Battery Temperature: 23.5℃
```

- [x] 1145(**ok**)複数シナリオ(xml)を指定、実行できるようにする(見積り)
branch:L5G_ST_CI1
commit:4a0a38488a959c7a873468c56ccb9debe70673dc
http://10.38.223.151:8080/job/L5G_ST_CI1/8704/console
config file need change
```
FROM:
----------------------------------------------------------------------------
[ADB_Service_Info]
IPAddress = 10.38.2.102,10.38.2.199
Port = 
UserName = ubuntu,ubuntu
Password = traffic,traffic
SourceCodePath = 
XmlFile = xml_files/test_case_1.xml,xml_files/test_case_2.xml
----------------------------------------------------------------------------
TO:
----------------------------------------------------------------------------
[ADB_00_Service_Info]
IPAddress = 10.38.2.102
Port = 
UserName = ubuntu
Password = traffic
SourceCodePath = 
XmlFile = xml_files/lu_test_case_0.xml,xml_files/lu_test_case_1.xml

[ADB_01_Service_Info]
IPAddress = 10.38.2.199
Port = 
UserName = ubuntu
Password = traffic
SourceCodePath = 
XmlFile = xml_files/lu_test_case_0.xml,xml_files/lu_test_case_2.xml
----------------------------------------------------------------------------
```
---

### 2023-03-07
原日方需求，现在的状态：
- [x] 1112(**ok**)外部スクリプト実行時のメッセージをJenkinsコンソールに表示する(見積り)
既存代码有这个功能

- [x] 1110(**ok**)端末異常が発生し、iperfが途中で中断された場合にCI上でNGに見えない件の対応(見積り)
commit：6597b3f5d6e07d59f4c911736ee4450c48f7ba3a

- [x] 1111(**ok**)iperf結果のグラフを端末毎にまとめて表示する(見積り)
根据日方需求，只修改名字

- [x] 1144(**ok**)ログ取得時に試験で使用したconfigとxmlを一緒に回収するようにする(見積り)
commit：1becfbe93e7ff4eefe52c7f28eff33378ce77147

- [x] 1113(**ok**)バッテリー残量表示のAction追加(見積り)
- [x] 1114(**ok**)バッテリー残量表示コマンド発行でタイムアウトしてもAbortしないようにする(見積り)
commit：5858bb491f121888c2ce7003f9bba51ff72ca5a1

### 2023-03-06
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

