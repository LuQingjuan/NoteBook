# IT2試験環境セットアップ手順

-windows PC
	IP：10.38.161.73
	ID/PW: 00111036/Mobile1249!
-Linux
	IP：10.37.190.71
	ID/PW: ubuntu/traffic
-samba：
	X   \\10.37.190.71\share

1)samba install:
```
$ sudo apt-get insall samba samba-common
$ mkdir DUCP_IT
```

2)config追加:
```
$ sudo vim /etc/samba/smb.conf
[share]
comment = share folder
browseable = yes
path = /home/ubuntu/DUCP_IT
create mask = 0700
directory mask = 0700
valid users = ubuntu
force user = ubuntu
force group = ubuntu
public = yes
available = yes
writable = yes
```

3)shareディレクトリをwindowsのxディスクにマウントします



- よく使うdockerコマンド
```bash
$ docker container run ・・・                       : コンテナを作成して起動する
$ docker container ps -a                            : 実行中のコンテナを確認する
$ docker container start [dockername]               : 停止しているコンテナを起動する。
$ docker container exec -it [dockername] /bin/bash  : コンテナに入る
$ docker container stop [dockername]                : 起動中のコンテナを確認する
$ docker container rm [dockername]                  : コンテナを削除する
```

## もくじ
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [IT2試験環境セットアップ手順](#it2試験環境セットアップ手順)
  - [もくじ](#もくじ)
  - [1 DUCP docker作成](#1-ducp-docker作成)
- [**Change Version**](#change-version)
  - [2 擬似ツール docker作成](#2-擬似ツール-docker作成)
  - [3 IT2試験 シナリオ実行](#3-it2試験-シナリオ実行)
  - [4 IT1試験 ログ取得と試験終了](#4-it1試験-ログ取得と試験終了)
  - [4 IT2試験 ログ取得と試験終了](#4-it2試験-ログ取得と試験終了)
  - [備考 Wiresharkについて](#備考-wiresharkについて)

<!-- /code_chunk_output -->

## 1 DUCP docker作成

1)teratermで192.168.99.101のl5gsaユーザでログインする (l5gsa/l5gsa)

2)minamiからos_common_config_xxxx_cuを取得する。
場所は任意だが、手順3 --env-fileオプションで読み込むのでl5gsaのホームディレクトリで良い。

- scpのパスワードは、「jftt_nijie」
```bash
$ svn export --force --username jftt_nijie --password jftt_nijie  svn://10.167.14.10/2019/1909_5G_dev_mpc/02.work/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/6E/os_common_config_0307/os_common_config_0307_du1 .
$ svn export --force --username jftt_nijie --password jftt_nijie  svn://10.167.14.10/2019/1909_5G_dev_mpc/02.work/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/6E/os_common_config_0307/os_common_config_0307_du2 .
```

3)git入りイメージファイルを取得＆ロード。
場所は「/home/images/」配下固定。

- ファイル名はリリース情報を参照してください。
- scpのパスワードは、「FJT_user」
```bash
$ cd images
$ scp -P 9418 FJT_user@minami.css.exnet.fujitsu.co.jp:/RANSoft/home/FJT/L5G/File/cu_cp_00_01_00.tar.gz ./
$ gzip -d cu_cp_00_01_00.tar.gz
$ docker load -i cu_cp_00_01_00.tar
$ cd ../
```
★現在は「cu_cp_00_01_00.tar」を使用

4)コンテナを作成して起動する

--name ”dockername”を設定する。環境に合わせて修正ください。※以降のdockernameは自環境の設定に読み替えてください。
-v local_dir:container_dir でディレクトリをマウント可能 環境に合わせて修正ください。※以降のcontainer_dirは自環境の設定に読み替えてください。
--security-opt="seccomp=unconfined" gdb使う場合

--環境変数ファイルやcu_cpイメージファイルを変える場合は、コンテナの削除、再作成からやり直す必要があります。
--以下のコマンドで読み込まれている環境変数を確認できます。
--docker inspect --format='{{range .Config.Env}}{{println .}}{{end}}' [コンテナ名]
--また、起動中のコンテナ上で、環境変数を一時的にexportコマンドで変更可能です。pオプションで一覧表示。
--例：export CAG_NUM_DU1="1"
--    export -p
--ただし、コンテナを停止すると変更は元に戻ります
--一時的に変更して試験を実施する時は、00_login_DUCP_IT2.ttlのdocker login直後に環境変数を変更しましょう。

```bash
$ mkdir DUCP_IT2
$ cd DUCP_IT2
$ docker container run -it -v ${PWD}/common/:/usr/local/container/common/ -v ${PWD}/build_ducp_it2/:/build_ducp_it2/ -v ${PWD}/sdm0:/sdm0 -v ${PWD}/logx:/var/log -v ${PWD}/storage/log:/storage/log -v /etc/localtime:/etc/localtime:ro --name build_ducp_it2 --env-file=os_common_config_0307_du1 --privileged --security-opt="seccomp=unconfined" cu_cp:00.01.00 /bin/bash
```

-注意:max環境:--env-file=os_common_config_0307_du2

5)エクスプローラーからアクセス可能なようにアクセス権を付与する。

```bash
$ chmod 777 build_ducp_it2
```

6)svnからIT2試験用スクリプトを取得する。
-注意 以下svn_username,svn_passwordはsvnアカウントを指定してください。

```bash
$ cd build_ducp_it2/
$ svn export --force --username jftt_nijie --password jftt_nijie svn://sayuri.css.exnet.fujitsu.co.jp/svn/fNB/trunk/SWgNB/DU_CP/00_CARD/10_BUILD/cardlm_script_export.sh .
$ ll
$ drwxrwxrwx  2 root   root       4096 10月  1 14:05 ./
$ drwxrwxrwx 27 l5gsa  l5gsa      4096 10月  1 13:33 ../
$ -rwxr-xr-x 1 root root  553  8月 12 10:15 cardlm_script_export.sh*
$ chmod 777 *
$ ./cardlm_script_export.sh jftt_nijie jftt_nijie 
$ chmod 777 -R scripts/
$ cd scripts/
$ svn export --force --username jftt_nijie --password jftt_nijie svn://sayuri.css.exnet.fujitsu.co.jp/svn/fNB/trunk/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/6E/script/ .
$ chmod 777 -R *
$ ll
$ drwxrwxrwx  4 nobody  132 4096  2月 14 18:52 ./
$ drwxrwxrwx  3 nobody  132 4096  2月 14 17:51 ../
-rwxrwxrwx  1 root   root 1012 11月 16 17:08 01_clean_build_env.sh*
-rwxrwxrwx  1 root   root 1478 12月 28 16:14 02_1_git_clone.sh*
-rwxrwxrwx  1 root   root 2178 11月 16 17:08 02_2_svn_export_sg.sh*
-rwxrwxrwx  1 root   root 2618 12月 28 16:14 03_lib_build.sh*
-rwxrwxrwx  1 root   root 1888 11月 16 17:08 04_oal_build.sh*
-rwxrwxrwx  1 root   root 6723  1月 14 18:05 05_card_build.sh*
-rwxrwxrwx  1 root   root 1608 11月 16 17:08 06_L3_build.sh*
-rwxrwxrwx  1 root   root 3831  1月 21 11:51 07_lm_copy.sh*
-rwxrwxrwx  1 nobody  132 1016  2月 21 11:10 42_set_env_IT2.sh*
-rwxrwxrwx  1 nobody  132 1051  2月 21 11:28 44_config_copy_IT2.sh*
-rwxrwxrwx  1 nobody  132 1036  1月  4 11:07 50_UEMR_only_build_LMcopy.sh*
-rwxrwxrwx  1 nobody  132  877  1月  4 11:07 66_svn_update.sh*
-rwxrwxrwx  1 nobody  132 1671  2月 21 10:16 88_restart_all_script_IT2.sh*
-rwxrwxrwx  1 root   root 1979 12月 28 16:14 99_all_script.sh*
-rwxrwxrwx  1 nobody  132 2269  2月 21 09:20 99_all_script_IT2.sh*
-rwxrwxrwx  1 root   root 1716  1月 21 11:51 setenv_branch.sh*
```

7)git用にプロキシ設定を変更

- docker内で実行
```
$ docker ps -a
CONTAINER ID   IMAGE                               COMMAND                   CREATED        STATUS                      PORTS     NAMES
cc9fc8193668   cu_cp:00.01.00                      "/bin/bash"               2 weeks ago    Exited (0) 31 hours ago               build_ducp_it2_max
c7258539c402   cu_cp:00.01.00                      "/bin/bash"               2 weeks ago    Up 16 hours                           build_ducp_it2

$ docker exec -it c7258539c402 bash
root@c7258539c402:/# 
```
- 下記手順でproxyに何も設定されていない状態になればOK

```bash
$ git config --global http.proxy ""
$ git config --global https.proxy ""
$ cat ~/.gitconfig
$ [http]
$         proxy =
$ [https]
$         proxy =
```

8)IT2試験用スクリプトを実行する。※/msyssrv/へLMのコピーまで自動実施。

- 引数は下記の通り設定
-     1. [Git ID]       : git account ID
-     2. [Git Password] : git account password
-     3. [Branch]       : git branch name

```bash
$ apt-get update
$ apt-get install vim expect iproute2 iproute2-doc 
$ ./99_all_script_IT2.sh l5g_srcgetter l5g_srcgetter develop_CG_work
$ 
$ -------------------------------
$   LM Copy!! End
$ -------------------------------
★ここまで出力されればOK
```
# **Change Version**
```
docker container exec -it build_ducp_it2 /bin/bash
cd /build_ducp_it2/scripts
scripts/下??的env
./99_all_script_IT2.sh l5g_srcgetter l5g_srcgetter feature_reestablishment
./99_all_script_IT2.sh l5g_srcgetter l5g_srcgetter feature_F_OREC_FDD
chmod 777 -R /build_ducp_it2/scripts/
替?局数据sdm0
```

9)ttlスクリプトの変更
```bash
$ cd env/ttl
$ sed -i 's/192.168.99.101/10.37.190.71/' SetEnvironment.ttl
$ sed -i 's/l5gsa@/ubuntu@/' SetEnvironment.ttl
$ sed -i 's/user=l5gsa \/passwd=l5gsa/user=ubuntu \/passwd=traffic/' SetEnvironment.ttl
```

-ttlのリモート実行
-    sed -i 's/messagebox /;messagebox /' SetEnvironment.ttl
-    sed -i 's/passwd=traffic/passwd=traffic \/V/' SetEnvironment.ttl

-ttlステージングディレクトリ
-    svn://10.167.14.10/2019/1909_5G_dev_mpc/02.work/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/6E/ttl
-    svn://10.167.14.10/2019/1909_5G_dev_mpc/02.work/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/3E/ttl
-    svn://10.167.14.10/2019/1909_5G_dev_mpc/02.work/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/2E/ttl

## 2 擬似ツール docker作成

1)teratermで10.37.190.71のubuntuユーザでログインする (ubuntu/traffic)

2)minamiからos_common_config_xxxx_cuを取得する。※1 CUCP docker作成手順参照

3)コンテナを作成して起動する

--name ”dockername”を設定する。環境に合わせて修正ください。※以降のdockernameは自環境の設定に読み替えてください。
-v local_dir:container_dir でディレクトリをマウント可能 環境に合わせて修正ください。※以降のcontainer_dirは自環境の設定に読み替えてください。
--環境変数ファイルやpseudofbイメージファイルを変える場合は、コンテナの削除、再作成からやり直す必要があります。
--起動中のコンテナ上で、環境変数を一時的にexportコマンドで変更可能です。
--例：export CAG_NUM_DU1="1"
--ただし、コンテナを停止すると変更は元に戻ります
--また、以下のコマンドで読み込まれている環境変数を確認できます。
--docker inspect --format='{{range .Config.Env}}{{println .}}{{end}}' [コンテナ名]

```bash
docker container run -it -v ${PWD}/pseudo_it2:/pseudo_it2 -v /etc/localtime:/etc/localtime:ro --name pseudo_it2 --env-file=os_common_config_0307_du1 --privileged pseudofb:00.00.02 /bin/bash
```
-注意:max環境:--env-file=os_common_config_0307_du2

4)エクスプローラーからアクセス可能なようにアクセス権を付与する。

```bash
$ chmod 777 pseudo_it2
```

5)svnからIT2擬似ツールを取得する。
★現在疑似ツールシナリオ準備中。

```bash
$ cd pseudo_it2
$ svn export --force --username jftt_nijie --password jftt_nijie svn://sayuri.css.exnet.fujitsu.co.jp/svn/fNB/trunk/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/5E/pseudoReplySnd/99_set_pseudo_IT2.sh .
$ chmod 777 *
$ ./99_set_pseudo_IT2.sh jftt_nijie jftt_nijie
$ ll
$ drwxrwxrwx 4 root   root   4096 Feb 15 19:17 ./
$ drwxr-xr-x 1 root   root   4096 Feb 15 16:16 ../
$ -rwxrwxrwx 1 nobody  132 1964 Feb 16 20:49 99_set_pseudo_IT2.sh*
$ drwxrwxrwx 5 root   root 4096 Feb 16 20:49 PseudoAMF_GNB_CU/
$ drwxrwxrwx 5 root   root 4096 Feb 16 20:49 PseudoFB_SWgNB/
```


## 3 IT2試験 シナリオ実行

1)局データを取得・格納
試験環境の「/sdm0/」配下に下記局データを格納
　svn://sayuri.css.exnet.fujitsu.co.jp/svn/fNB/trunk/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/6E/FJConfig
　FJ_CONFIG_SWgNB_00_01_00_03_02.FGF
　DU
　※DUはフォルダごと格納

Yangパラメータ(startup-cfg.xml)は上記にDU配下に配置する必要があります。
http://sayuri.css.exnet.fujitsu.co.jp/gitlab/L5G_gNB_SW/DU-CP/wikis/DU-CP%E5%86%8D%E9%96%8B%E6%89%8B%E9%A0%86(SWgNB-PoC2'-3E%E5%90%91%E3%81%91)参照

2)試験用ttlを実行
「00_login_DUCP_IT2.ttl」を実行。
★セル設定・セルアンロック完了後に「Cell Unlock Complete!! 試験シナリオを実行してください」とポップアップが出る。

## 4 IT1試験 ログ取得と試験終了

3)エクスプローラー上で(\\10.37.190.71\share\DUCP_IT2\build_ducp_it2\scripts\env\ttl)のIT2試験シナリオを実行する。
例)IT2_DUCP_AMF_InitiaAccess(着信-発信)_Release_ptn1.ttl

## 4 IT2試験 ログ取得と試験終了
1)IT1試験シナリオが最後まで流れると、「試験完了!ログ取得を開始します」のポップアップが出力するので、
  OKを押下する。

  ↓にログが格納されます。各種コマンドログと/msyssrv配下とvarログを固めたもの。
  \\10.37.190.71\share\DUCP_IT2\build_ducp_it2\scripts\env\ttl\DUCP#Q

★自律でログ取得ttlを実行し、pkill -u rootでプロセス終了とteratermウィンドウをクローズします。

## 備考 Wiresharkについて
3Eより、取得するtcpDump.pcapはWiresharkに下記設定が必要となります。

「編集」タブ ⇒ 「設定」 ⇒ Protocols ⇒ 1_INBOUND
　それぞれ下記の通り設定
　
　解析対象ポート番号：50400,50800-50803,50805-50807,50850-50852,54000-54003,54005-54007,54050-54051
　受信ログ解析用IPアドレス：127.0.0.2
　受信ログ解析用ポート番号：31001受信ログ解析用アドレス
　
また、Wiresharkの表示フィルタは下記で設定をお願いします。
　ngap || f1ap || udp.port==54000


