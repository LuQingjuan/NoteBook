# IT2�������Z�b�g�A�b�v�菇

-windows PC
	IP�F10.38.161.73
	ID/PW: 00111036/Mobile1249!
-Linux
	IP�F10.37.190.71
	ID/PW: ubuntu/traffic
-samba�F
	X   \\10.37.190.71\share

1)samba install:
```
$ sudo apt-get insall samba samba-common
$ mkdir DUCP_IT
```

2)config�ǉ�:
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

3)share�f�B���N�g����windows��x�f�B�X�N�Ƀ}�E���g���܂�



- �悭�g��docker�R�}���h
```bash
$ docker container run �E�E�E                       : �R���e�i���쐬���ċN������
$ docker container ps -a                            : ���s���̃R���e�i���m�F����
$ docker container start [dockername]               : ��~���Ă���R���e�i���N������B
$ docker container exec -it [dockername] /bin/bash  : �R���e�i�ɓ���
$ docker container stop [dockername]                : �N�����̃R���e�i���m�F����
$ docker container rm [dockername]                  : �R���e�i���폜����
```

## ������
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [IT2�������Z�b�g�A�b�v�菇](#it2�������Z�b�g�A�b�v�菇)
  - [������](#������)
  - [1 DUCP docker�쐬](#1-ducp-docker�쐬)
- [**Change Version**](#change-version)
  - [2 �[���c�[�� docker�쐬](#2-�[���c�[��-docker�쐬)
  - [3 IT2���� �V�i���I���s](#3-it2����-�V�i���I���s)
  - [4 IT1���� ���O�擾�Ǝ����I��](#4-it1����-���O�擾�Ǝ����I��)
  - [4 IT2���� ���O�擾�Ǝ����I��](#4-it2����-���O�擾�Ǝ����I��)
  - [���l Wireshark�ɂ���](#���l-wireshark�ɂ���)

<!-- /code_chunk_output -->

## 1 DUCP docker�쐬

1)teraterm��192.168.99.101��l5gsa���[�U�Ń��O�C������ (l5gsa/l5gsa)

2)minami����os_common_config_xxxx_cu���擾����B
�ꏊ�͔C�ӂ����A�菇3 --env-file�I�v�V�����œǂݍ��ނ̂�l5gsa�̃z�[���f�B���N�g���ŗǂ��B

- scp�̃p�X���[�h�́A�ujftt_nijie�v
```bash
$ svn export --force --username jftt_nijie --password jftt_nijie  svn://10.167.14.10/2019/1909_5G_dev_mpc/02.work/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/6E/os_common_config_0307/os_common_config_0307_du1 .
$ svn export --force --username jftt_nijie --password jftt_nijie  svn://10.167.14.10/2019/1909_5G_dev_mpc/02.work/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/6E/os_common_config_0307/os_common_config_0307_du2 .
```

3)git����C���[�W�t�@�C�����擾�����[�h�B
�ꏊ�́u/home/images/�v�z���Œ�B

- �t�@�C�����̓����[�X�����Q�Ƃ��Ă��������B
- scp�̃p�X���[�h�́A�uFJT_user�v
```bash
$ cd images
$ scp -P 9418 FJT_user@minami.css.exnet.fujitsu.co.jp:/RANSoft/home/FJT/L5G/File/cu_cp_00_01_00.tar.gz ./
$ gzip -d cu_cp_00_01_00.tar.gz
$ docker load -i cu_cp_00_01_00.tar
$ cd ../
```
�����݂́ucu_cp_00_01_00.tar�v���g�p

4)�R���e�i���쐬���ċN������

--name �hdockername�h��ݒ肷��B���ɍ��킹�ďC�����������B���ȍ~��dockername�͎����̐ݒ�ɓǂݑւ��Ă��������B
-v local_dir:container_dir �Ńf�B���N�g�����}�E���g�\ ���ɍ��킹�ďC�����������B���ȍ~��container_dir�͎����̐ݒ�ɓǂݑւ��Ă��������B
--security-opt="seccomp=unconfined" gdb�g���ꍇ

--���ϐ��t�@�C����cu_cp�C���[�W�t�@�C����ς���ꍇ�́A�R���e�i�̍폜�A�č쐬�����蒼���K�v������܂��B
--�ȉ��̃R�}���h�œǂݍ��܂�Ă�����ϐ����m�F�ł��܂��B
--docker inspect --format='{{range .Config.Env}}{{println .}}{{end}}' [�R���e�i��]
--�܂��A�N�����̃R���e�i��ŁA���ϐ����ꎞ�I��export�R�}���h�ŕύX�\�ł��Bp�I�v�V�����ňꗗ�\���B
--��Fexport CAG_NUM_DU1="1"
--    export -p
--�������A�R���e�i���~����ƕύX�͌��ɖ߂�܂�
--�ꎞ�I�ɕύX���Ď��������{���鎞�́A00_login_DUCP_IT2.ttl��docker login����Ɋ��ϐ���ύX���܂��傤�B

```bash
$ mkdir DUCP_IT2
$ cd DUCP_IT2
$ docker container run -it -v ${PWD}/common/:/usr/local/container/common/ -v ${PWD}/build_ducp_it2/:/build_ducp_it2/ -v ${PWD}/sdm0:/sdm0 -v ${PWD}/logx:/var/log -v ${PWD}/storage/log:/storage/log -v /etc/localtime:/etc/localtime:ro --name build_ducp_it2 --env-file=os_common_config_0307_du1 --privileged --security-opt="seccomp=unconfined" cu_cp:00.01.00 /bin/bash
```

-����:max��:--env-file=os_common_config_0307_du2

5)�G�N�X�v���[���[����A�N�Z�X�\�Ȃ悤�ɃA�N�Z�X����t�^����B

```bash
$ chmod 777 build_ducp_it2
```

6)svn����IT2�����p�X�N���v�g���擾����B
-���� �ȉ�svn_username,svn_password��svn�A�J�E���g���w�肵�Ă��������B

```bash
$ cd build_ducp_it2/
$ svn export --force --username jftt_nijie --password jftt_nijie svn://sayuri.css.exnet.fujitsu.co.jp/svn/fNB/trunk/SWgNB/DU_CP/00_CARD/10_BUILD/cardlm_script_export.sh .
$ ll
$ drwxrwxrwx  2 root   root       4096 10��  1 14:05 ./
$ drwxrwxrwx 27 l5gsa  l5gsa      4096 10��  1 13:33 ../
$ -rwxr-xr-x 1 root root  553  8�� 12 10:15 cardlm_script_export.sh*
$ chmod 777 *
$ ./cardlm_script_export.sh jftt_nijie jftt_nijie 
$ chmod 777 -R scripts/
$ cd scripts/
$ svn export --force --username jftt_nijie --password jftt_nijie svn://sayuri.css.exnet.fujitsu.co.jp/svn/fNB/trunk/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/6E/script/ .
$ chmod 777 -R *
$ ll
$ drwxrwxrwx  4 nobody  132 4096  2�� 14 18:52 ./
$ drwxrwxrwx  3 nobody  132 4096  2�� 14 17:51 ../
-rwxrwxrwx  1 root   root 1012 11�� 16 17:08 01_clean_build_env.sh*
-rwxrwxrwx  1 root   root 1478 12�� 28 16:14 02_1_git_clone.sh*
-rwxrwxrwx  1 root   root 2178 11�� 16 17:08 02_2_svn_export_sg.sh*
-rwxrwxrwx  1 root   root 2618 12�� 28 16:14 03_lib_build.sh*
-rwxrwxrwx  1 root   root 1888 11�� 16 17:08 04_oal_build.sh*
-rwxrwxrwx  1 root   root 6723  1�� 14 18:05 05_card_build.sh*
-rwxrwxrwx  1 root   root 1608 11�� 16 17:08 06_L3_build.sh*
-rwxrwxrwx  1 root   root 3831  1�� 21 11:51 07_lm_copy.sh*
-rwxrwxrwx  1 nobody  132 1016  2�� 21 11:10 42_set_env_IT2.sh*
-rwxrwxrwx  1 nobody  132 1051  2�� 21 11:28 44_config_copy_IT2.sh*
-rwxrwxrwx  1 nobody  132 1036  1��  4 11:07 50_UEMR_only_build_LMcopy.sh*
-rwxrwxrwx  1 nobody  132  877  1��  4 11:07 66_svn_update.sh*
-rwxrwxrwx  1 nobody  132 1671  2�� 21 10:16 88_restart_all_script_IT2.sh*
-rwxrwxrwx  1 root   root 1979 12�� 28 16:14 99_all_script.sh*
-rwxrwxrwx  1 nobody  132 2269  2�� 21 09:20 99_all_script_IT2.sh*
-rwxrwxrwx  1 root   root 1716  1�� 21 11:51 setenv_branch.sh*
```

7)git�p�Ƀv���L�V�ݒ��ύX

- docker���Ŏ��s
```
$ docker ps -a
CONTAINER ID   IMAGE                               COMMAND                   CREATED        STATUS                      PORTS     NAMES
cc9fc8193668   cu_cp:00.01.00                      "/bin/bash"               2 weeks ago    Exited (0) 31 hours ago               build_ducp_it2_max
c7258539c402   cu_cp:00.01.00                      "/bin/bash"               2 weeks ago    Up 16 hours                           build_ducp_it2

$ docker exec -it c7258539c402 bash
root@c7258539c402:/# 
```
- ���L�菇��proxy�ɉ����ݒ肳��Ă��Ȃ���ԂɂȂ��OK

```bash
$ git config --global http.proxy ""
$ git config --global https.proxy ""
$ cat ~/.gitconfig
$ [http]
$         proxy =
$ [https]
$         proxy =
```

8)IT2�����p�X�N���v�g�����s����B��/msyssrv/��LM�̃R�s�[�܂Ŏ������{�B

- �����͉��L�̒ʂ�ݒ�
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
�������܂ŏo�͂�����OK
```
# **Change Version**
```
docker container exec -it build_ducp_it2 /bin/bash
cd /build_ducp_it2/scripts
scripts/��??�Ienv
./99_all_script_IT2.sh l5g_srcgetter l5g_srcgetter feature_reestablishment
./99_all_script_IT2.sh l5g_srcgetter l5g_srcgetter feature_F_OREC_FDD
chmod 777 -R /build_ducp_it2/scripts/
��?�ǐ���sdm0
```

9)ttl�X�N���v�g�̕ύX
```bash
$ cd env/ttl
$ sed -i 's/192.168.99.101/10.37.190.71/' SetEnvironment.ttl
$ sed -i 's/l5gsa@/ubuntu@/' SetEnvironment.ttl
$ sed -i 's/user=l5gsa \/passwd=l5gsa/user=ubuntu \/passwd=traffic/' SetEnvironment.ttl
```

-ttl�̃����[�g���s
-    sed -i 's/messagebox /;messagebox /' SetEnvironment.ttl
-    sed -i 's/passwd=traffic/passwd=traffic \/V/' SetEnvironment.ttl

-ttl�X�e�[�W���O�f�B���N�g��
-    svn://10.167.14.10/2019/1909_5G_dev_mpc/02.work/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/6E/ttl
-    svn://10.167.14.10/2019/1909_5G_dev_mpc/02.work/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/3E/ttl
-    svn://10.167.14.10/2019/1909_5G_dev_mpc/02.work/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/2E/ttl

## 2 �[���c�[�� docker�쐬

1)teraterm��10.37.190.71��ubuntu���[�U�Ń��O�C������ (ubuntu/traffic)

2)minami����os_common_config_xxxx_cu���擾����B��1 CUCP docker�쐬�菇�Q��

3)�R���e�i���쐬���ċN������

--name �hdockername�h��ݒ肷��B���ɍ��킹�ďC�����������B���ȍ~��dockername�͎����̐ݒ�ɓǂݑւ��Ă��������B
-v local_dir:container_dir �Ńf�B���N�g�����}�E���g�\ ���ɍ��킹�ďC�����������B���ȍ~��container_dir�͎����̐ݒ�ɓǂݑւ��Ă��������B
--���ϐ��t�@�C����pseudofb�C���[�W�t�@�C����ς���ꍇ�́A�R���e�i�̍폜�A�č쐬�����蒼���K�v������܂��B
--�N�����̃R���e�i��ŁA���ϐ����ꎞ�I��export�R�}���h�ŕύX�\�ł��B
--��Fexport CAG_NUM_DU1="1"
--�������A�R���e�i���~����ƕύX�͌��ɖ߂�܂�
--�܂��A�ȉ��̃R�}���h�œǂݍ��܂�Ă�����ϐ����m�F�ł��܂��B
--docker inspect --format='{{range .Config.Env}}{{println .}}{{end}}' [�R���e�i��]

```bash
docker container run -it -v ${PWD}/pseudo_it2:/pseudo_it2 -v /etc/localtime:/etc/localtime:ro --name pseudo_it2 --env-file=os_common_config_0307_du1 --privileged pseudofb:00.00.02 /bin/bash
```
-����:max��:--env-file=os_common_config_0307_du2

4)�G�N�X�v���[���[����A�N�Z�X�\�Ȃ悤�ɃA�N�Z�X����t�^����B

```bash
$ chmod 777 pseudo_it2
```

5)svn����IT2�[���c�[�����擾����B
�����݋^���c�[���V�i���I�������B

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


## 3 IT2���� �V�i���I���s

1)�ǃf�[�^���擾�E�i�[
�������́u/sdm0/�v�z���ɉ��L�ǃf�[�^���i�[
�@svn://sayuri.css.exnet.fujitsu.co.jp/svn/fNB/trunk/SWgNB/DU_CP/50_ADPT/05_IT2/scenario/01_CONV/6E/FJConfig
�@FJ_CONFIG_SWgNB_00_01_00_03_02.FGF
�@DU
�@��DU�̓t�H���_���Ɗi�[

Yang�p�����[�^(startup-cfg.xml)�͏�L��DU�z���ɔz�u����K�v������܂��B
http://sayuri.css.exnet.fujitsu.co.jp/gitlab/L5G_gNB_SW/DU-CP/wikis/DU-CP%E5%86%8D%E9%96%8B%E6%89%8B%E9%A0%86(SWgNB-PoC2'-3E%E5%90%91%E3%81%91)�Q��

2)�����pttl�����s
�u00_login_DUCP_IT2.ttl�v�����s�B
���Z���ݒ�E�Z���A�����b�N������ɁuCell Unlock Complete!! �����V�i���I�����s���Ă��������v�ƃ|�b�v�A�b�v���o��B

## 4 IT1���� ���O�擾�Ǝ����I��

3)�G�N�X�v���[���[���(\\10.37.190.71\share\DUCP_IT2\build_ducp_it2\scripts\env\ttl)��IT2�����V�i���I�����s����B
��)IT2_DUCP_AMF_InitiaAccess(���M-���M)_Release_ptn1.ttl

## 4 IT2���� ���O�擾�Ǝ����I��
1)IT1�����V�i���I���Ō�܂ŗ����ƁA�u��������!���O�擾���J�n���܂��v�̃|�b�v�A�b�v���o�͂���̂ŁA
  OK����������B

  ���Ƀ��O���i�[����܂��B�e��R�}���h���O��/msyssrv�z����var���O���ł߂����́B
  \\10.37.190.71\share\DUCP_IT2\build_ducp_it2\scripts\env\ttl\DUCP#Q

�������Ń��O�擾ttl�����s���Apkill -u root�Ńv���Z�X�I����teraterm�E�B���h�E���N���[�Y���܂��B

## ���l Wireshark�ɂ���
3E���A�擾����tcpDump.pcap��Wireshark�ɉ��L�ݒ肪�K�v�ƂȂ�܂��B

�u�ҏW�v�^�u �� �u�ݒ�v �� Protocols �� 1_INBOUND
�@���ꂼ�ꉺ�L�̒ʂ�ݒ�
�@
�@��͑Ώۃ|�[�g�ԍ��F50400,50800-50803,50805-50807,50850-50852,54000-54003,54005-54007,54050-54051
�@��M���O��͗pIP�A�h���X�F127.0.0.2
�@��M���O��͗p�|�[�g�ԍ��F31001��M���O��͗p�A�h���X
�@
�܂��AWireshark�̕\���t�B���^�͉��L�Őݒ�����肢���܂��B
�@ngap || f1ap || udp.port==54000


