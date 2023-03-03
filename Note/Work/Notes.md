[TOC]
# Web 资源
## 网站资源
[联网网页](http://10.167.250.50:90/login)
[3GPP](http://www.3gpp.org/ftp/specs/latest/rel-14/36_series/)
[群](https://lync.cn.fujitsu.com/Meet/wu.jing/SVDQTD0P)

## 代理
* 中国
    - 系统
    export http_proxy=http://centos5g:1249124912@rep.proxy.nic.fujitsu.com:8080 
    export https_proxy=https://centos5g:1249124912@rep.proxy.nic.fujitsu.com:8080
    export http_proxy=http://panzhiyang:9694891676@10.76.29.8:8080
    export https_proxy=https://panzhiyang:9694891676@10.76.29.8:8080

    - IE代理
    http://10.167.10.143/access.pac

* 日本
    - 系统
    export  http_proxy=http://mos9test1:1766024495@10.0.58.8:8080
    export  https_proxy=https://mos9test1:1766024495@10.0.58.8:8080
    export http_proxy=http://centos5g:1249124912@10.0.58.88:8080
    export https_proxy=https://centos5g:1249124912@10.0.58.88:8080
    centos5g:1249124912
    http.proxy http://centos5g:1249124912@10.128.145.88:8080
    https.proxy http://centos5g:1249124912@10.128.145.88:8080
    - IE代理
    http://pac.int.nic.fujitsu.com/auth.pac
    上网账号：mos9test1 密码：1766024495

---
# Windows
## 远程访问
1. 在windows上通过 win + R 组合键，打开 "运行" 窗口，输入远程桌面连接命令 mstsc
2. 在出现的远程桌面连接窗口的 "计算机(C)" 那一栏里输入IP地址： 10.38.161.115
3. 待"Login to xrdp"登录窗口出现之后，Module 选择 "sesman-Xvnc", username 和 password 是 ubuntu 和 1249
4. 登录成功之后，会出现ubuntu的桌面，右键选择Application中的WebBrowser，FireFox浏览器会打开。
5. 在FireFox的地址栏里输入 http://10.37.145.15/redmine 访问RedMine。
---
