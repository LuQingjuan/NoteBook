#環境(OS)
Ubuntu

# ソフトパッケージ
## Python3をインストールする
```
$ apt-get install python3
$ python3 --version

$ apt-get install python3-pip
$ pip3 --version
```

## グラフ作成が必要なmatplotlibをインストールする
```
$ pip3 install matplotlib
$ pip3 list | grep "matplotlib"
```

## 数計算要用numpyをインストールする
	$ pip3 install numpy
	$ pip3 list | grep "numpy"

---
-rw-rw-r-- 1 ubuntu ubuntu 2512931 Jan 11 07:02 '
-rw-rw-r-- 1 ubuntu ubuntu 1963870 Jan 11 07:01 '
-rw-rw-r-- 1 ubuntu ubuntu  374252 Jan 11 07:02 '

# スクリプトの使い方
　main.pyとcu statsのログファイルを同じ場所に格納しておく。
* 例： log：cu_stats_22_12_12_11_07_04.txt
`$ python3 main.py cu_stats_22_12_12_11_07_04.txt`

* 例： log：cu_cp_stats_23_01_10_19_40_55.txt cu_up_stats_23_01_10_19_40_52.txt
`$ python3 main.py cu_cp_stats_23_01_10_19_40_55.txt cu_up_stats_23_01_10_19_40_52.txt`

* グラフファイルが作成される：
  * cu_stats_22_12_12_11_07_04_DDDS RCVD.png　　　　　　　　　　　　　　　　　//PDCPのDDDSデータ量　　
  * cu_stats_22_12_12_11_07_04_DL UL Iperf Throughput.png　　　　//UDP側ののデータ量
  * cu_stats_22_12_12_11_07_04_DL UL Iperf EGTPU.png　　　　　　　　　//EGTPU側ののデータ量

# グラフの見方
## cu_stats_22_12_12_11_07_04_DDDS RCVD.png
* 
上のグラフには：すべてのUEのDDDS合計
下のグラフ以降は：UEごとのDDDS情報
　　左側は：Rateで、右側はCntです。
* データの取得元は：
X0： PDCP RX [0] STATISTICS中のDDDS-RCVD-Rate　とDDDS-RCVD-CNT
X0： PDCP TX [0] STATISTICS中のDDDS-RCVD-Rate　とDDDS-RCVD-CNT
X1： PDCP TX [1] STATISTICS中のDDDS-RCVD-Rate　とDDDS-RCVD-CNT
X2： PDCP TX [2] STATISTICS中のDDDS-RCVD-Rate　とDDDS-RCVD-CNT

## cu_stats_22_12_12_11_07_04_DL UL Iperf Throughput.png
* 
左側は：DLスループットで、右側は：ULスループットです
* データの取得元は：
UL (UDP RX STATISTICS)：UDP RX STATISTICS中のUDP-UL-Rx
DL (UDP RX STATISTICS)：UDP RX STATISTICS中のUDP-DL-Rx
DL 8 (UDP TX STATISTICS)：UDP TX STATISTICS中のDL-8のThroughput
DL 9 (UDP TX STATISTICS)：UDP TX STATISTICS中のDL-9のThroughput
DL 10 (UDP TX STATISTICS)：UDP TX STATISTICS中のDL-10のThroughput
UL 11 (UDP TX STATISTICS)；UDP TX STATISTICS中のUL-11のThroughput

## cu_stats_22_12_12_11_07_04_DL UL Iperf EGTPU.png
* 
上のグラフには：すべてのUEのスループット合計
下のグラフ以降は：UEごとのスループット
左側は：DLスループットで、右側は：ULスループットです
* データの取得元は：
EGTPU UPPER RX (5GC -> CU)：EGTPU UPPER RX STATISTICS中のTX (Mbps)
EGTPU LOWER TX (CU -> DU)：EGTPU LOWER TX STATISTICS中のTX (Mbps)
EGTPU LOWER RX (DU -> CU)：EGTPU LOWER RX STATISTICS中のTX (Mbps)
EGTPU UPPER TX (CU -> 5GC)：EGTPU UPPER TX STATISTICS中のTX (Mbps)