**[Home](../Menu.md)**
[TOC]

# ELK简介

![](../../Resource/image/tool/ELK%20Kinana_2.png)
ELK是三个开源软件的缩写，分别表示：Elasticsearch , Logstash, Kibana , 它们都是开源软件。新增了一个FileBeat，它是一个轻量级的日志收集处理工具(Agent)，Filebeat占用资源少，适合于在各个服务器上搜集日志后传输给Logstash，官方也推荐此工具。
## Elasticsearch
Elasticsearch 是个开源分布式搜索引擎，提供搜集、分析、存储数据三大功能。它的特点有：分布式，零配置，自动发现，索引自动分片，索引副本机制，restful风格接口，多数据源，自动搜索负载等。
## Logstash
Logstash 主要是用来日志的搜集、分析、过滤日志的工具，支持大量的数据获取方式。一般工作方式为c/s架构，client端安装在需要收集日志的主机上，server端负责将收到的各节点日志进行过滤、修改等操作在一并发往elasticsearch上去。
## Kibana
Kibana 也是一个开源和免费的工具，Kibana可以为 Logstash 和 ElasticSearch 提供的日志分析友好的 Web 界面，可以帮助汇总、分析和搜索重要数据日志。
[原文链接](https://blog.csdn.net/baiwenjiebwj/article/details/119781642)
## 关系
![](../../Resource/image/tool/ELK%20Kinana_1.png)

$ sudo /usr/share/logstash/bin/logstash -f <font color="red">accesslog.conf</font>
[accesslog.conf](#1)中配置
源   : CSV数据
目的 : Elasticsearch服务器信息

---
# 环境构筑
## 安装JDK
[comment]:-----------------------------------------------------
[comment]:[JDK安装](JDK.md)
**安装**
`$ sudo -E apt install openjdk-8-jre-headless openjdk-8-jdk-headless`
**查看 openjdk-8-jre-headless**
`$ java`
```
The program 'java' can be found in the following packages:
 * default-jre
 * gcj-5-jre-headless
 * openjdk-8-jre-headless
 * gcj-4.8-jre-headless
 * gcj-4.9-jre-headless
 * openjdk-9-jre-headless
Try: sudo apt install <selected package>
```
**查看 openjdk-8-jdk-headless**
`$ javac`
```
The program 'javac' can be found in the following packages:
 * default-jdk
 * ecj
 * gcj-5-jdk
 * openjdk-8-jdk-headless
 * gcj-4.8-jdk
 * gcj-4.9-jdk
 * openjdk-9-jdk-headless
Try: sudo apt install <selected package>
```
[comment]:[JDK安装](JDK.md)
[comment]:-----------------------------------------------------

## 非固定版本安装
`$ sudo apt-get install elasticsearch kibana logstash`
[Elasticsearch安装手顺](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html)
[kibana安装手顺](https://www.elastic.co/guide/en/kibana/current/deb.html)
[logstash安装手顺](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

## 固定版本安装
### 下载软件
`$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.5.0.deb`
`$ wget https://artifacts.elastic.co/downloads/kibana/kibana-5.5.0-amd64.deb`
`$ wget https://artifacts.elastic.co/downloads/logstash/logstash-5.5.0.deb`

### 安装 Elasticsearch
**下载软件**
`$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.5.0.deb`
**安装**
`$ sudo dpkg -i elasticsearch-5.5.0.deb`
**插看版本**
`$ dpkg -l|grep elasticsearch`

### 安装 Logstash
**下载软件**
`$ wget https://artifacts.elastic.co/downloads/logstash/logstash-5.5.0.deb`
**安装**
`$ sudo dpkg -i logstash-5.5.0.deb`
**插看版本**
`$ dpkg -l|grep logstash`

### 安装 Kibana
**下载软件**
`$ wget https://artifacts.elastic.co/downloads/kibana/kibana-5.5.0-amd64.deb`
**安装**
`$ sudo dpkg -i kibana-5.5.0-amd64.deb`
**插看版本**
`$ dpkg -l|grep kibana"`

---
## 配置
### 配置 Elasticsearch
**修改配置项**
`$ sudo vi /etc/elasticsearch/elasticsearch.yml`
```
#network.host: "localhost" 
↓
network.host: 0.0.0.0
#http.cors.enabled: true
```
### 配置 Kibana
**修改配置项**
`$ sudo vi /etc/kibana/kibana.yml`
```
#server.host: "localhost"
↓
server.host: "0.0.0.0"
```

---
## 卸载
**查看安装情况**
`$ dpkg -l|grep -E "kibana|logstash|elasticsearch"`

**关闭服务**
`$ sudo /etc/init.d/kibana stop`
`$ sudo /etc/init.d/elasticsearch stop`

**卸载软件**
`$ sudo dpkg -P kibana`
`$ sudo dpkg -P logstash`
`$ sudo dpkg -P elasticsearch`

**查看卸载情况**
`$ dpkg -l|grep -E "kibana|logstash|elasticsearch"`

---
# 数据收集
## Logstash 收集数据
**[配置文件]#(1)**
accesslog.conf
```
input {
    file {
        path => "/home/jftt/work_jftt/lu/Kibana/data.csv"
        start_position => "beginning"
    }
}
filter {
    csv {
        columns => ["first_data", "second_data"]
        separator => ","
    }
    mutate {
        convert => {
            first_data => "integer"
            second_data => "integer"
        }
    }
}
output {
    stdout { codec => rubydebug }
    elasticsearch {
        hosts => ["10.167.14.30:9200"]
    }
}
```

**生成数据工具**
```
#/bin/bash
i=1
while [ $i -le 5 ]
do
	echo "Creating data"
	for j in {1..$[$RANDOM%20+1]}
	do
		echo "$[$RANDOM%100],$[$RANDOM%100]" >>data.csv 
	done
	sleep $[$RANDOM%5]
done
```

## 启动 Elasticsearch
`$ sudo /etc/init.d/elasticsearch start`
此时: 可以访问：http://10.167.14.30:9200/

`$ sudo /etc/init.d/elasticsearch status`

## 启动 Kibana
`$ sudo /etc/init.d/kibana start`
此时: 可以访问：http://10.167.14.30:5601/
`$ sudo /etc/init.d/kibana status`

## 启动 Logstash
**收集数据**
`$ sudo /usr/share/logstash/bin/logstash -f accesslog.conf`


---
# 插件
## 3D插件 area3d_vis
**下载软件**
`$ git clone https://github.com/JuanCarniglia/area3d_vis.git`
**准备**
`$ sudo cp -r area3d_vis/releases/5.5/ /usr/share/kibana/src/core_plugins/area3d_vis`
**修改index.js**
`$ sudo vi area3d_vis/index.js `
```
'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

exports.default = function (kibana) {

  return new kibana.Plugin({
    uiExports: {
      visTypes: ['plugins/area3d_vis/area3d_vis']
    }
  });
};

module.exports = exports['default'];

```
**关闭 Kibana**
`$ sudo /etc/init.d/kibana stop`
**安装**
```
$ nodejs -v
$ npm -v
$ sudo -E apt install nodejs npm
$ npm config set proxy=http://mos9test1:1766024495@10.0.58.8:8080/
$ sudo npm install vis
```
**启动Kibana**
`$ sudo /etc/init.d/kibana start`

**插看版本**
此时: 访问：http://10.38.161.86:5601/
可以在**Visualize**中看到**Area3D**