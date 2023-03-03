[TOC]
# 环境
* 环境初始化
1. 设置代理
`# vi ~/.bashrc`
	```
	export http_proxy=http://centos5g:1249124912@10.128.145.88:8080/
	export https_proxy=http://centos5g:1249124912@10.128.145.88:8080/
	```
2. 代理生效
`# source ~/.bashrc`
3. 更新
`$ sudo -E apt update`
`$ sudo -E apt-get update`
4. 安装pip3
`sudo apt install python3-pip`