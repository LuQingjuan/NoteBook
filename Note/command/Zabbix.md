**[Home](../Menu.md)**
[TOC]
# zabbix
环境：Ubuntu
## 安装
1. 下载安装包
```
wget http://repo.zabbix.com/zabbix/3.2/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.2-1+xenial_all.deb
如果错误，在下面网页找到版本路径下载
http://repo.zabbix.com/zabbix
```
2. 安装
```
sudo dpkg -i zabbix-release_3.2-1+xenial_all.deb
sudo dpkg -i *.deb
```
3. 更新安装工具
`sudo -E apt-get update`
4. 安装
`sudo -E apt-get install -y zabbix-agent`
5. 检测是否安装成功
`/etc/init.d/zabbix-agent start`