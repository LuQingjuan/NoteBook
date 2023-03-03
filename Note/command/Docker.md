**[Home](../Menu.md)**
[TOC]
# Docker
## 介绍
### Docker 架构

1. 镜像（Image）:一个特殊的文件系统
Docker 镜像（Image），就相当于是一个 root 文件系统。比如官方镜像 ubuntu:16.04 就包含了完整的一套 Ubuntu16.04 最小系统的 root 文件系统。
2. 容器（Container）:镜像运行时的实体
镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的类和实例一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。
3. 仓库（Repository）:集中存放镜像文件的地方
仓库可看成一个代码控制中心，用来保存镜像。

### 工作流程
```graphviz
digraph demo{
  graph[]
  node[]
  edge[]
    仓库->仓库[label="search"]
    仓库->镜像[label="pull"]
    镜像->仓库[label="push"]
    镜像->容器[label="create"]
    镜像->启动的容器[label="run"]
    容器->容器[label="kill、rm"]
    容器->启动的容器[label="start、restart"]
    启动的容器->容器[label="stop"]
}
```

## 命令
### 容器生命周期管理
#### run
docker run [OPTIONS] IMAGE根据镜像新建并启动容器。IMAGE是镜像ID或镜像名称
OPTIONS说明：
--name=“容器新名字”：为容器指定一个名称
-d：后台运行容器，并返回容器ID，也即启动守护式容器
-i：以交互模式运行容器，通常与-t同时使用
-t：为容器重新分配一个伪输入终端，通常与-i同时使用
-p：随机端口映射
-p：指定端口映射，有以下四种格式：
ip:hostPort:containerPort
ip::containerPort
hostPort:containerPort
containerPort

* 创建并start容器：
$ docker run --name 容器名 -i -t imageid /bin/bash
* 创建容器
$ docker run -it ubuntu:18.04 -v 本地路径:容器路径 --name 容器名 image /bin/bash
* -t: 在新容器内指定一个伪终端或终端
* -i: 允许你对容器内的标准输入（STDIN）进行交互
* -v: 是将宿主机目录，必须为绝对路径，冒号后为容器内挂载的路径
* ––name: 这里注意是双短线，来命名容器，不然每次docker会对容器进行自动命名，容器多了就分不清楚到底不同容器之间的关系了。

[sudo] password for vranmec:
18a26aa93950a34b724321b43f94750dc620b7ef6a82578f95243ae854999cc7

运行一个应用程序`docker run ubuntu:15.10 /bin/echo "Hello world"`
对话 `docker run -it ubuntu:15.10 /bin/bash`

#### start
#### stop
#### restart
#### kill
强制停止容器
#### rm
删除容器
docker rm -f 容器ID或容器名称强制删除容器
docker rm -f $(docker ps -a -q)删除多个容器
#### pause
#### unpause
#### create
#### exec
### 容器操作
#### ps
列出当前所有正在运行的容器
docker ps -a列出所有的容器
docker ps -l列出最近创建的容器
docker ps -n 3列出最近创建的3个容器
docker ps -q只显示容器ID
docker ps --no-trunc显示当前所有正在运行的容器完整信息
* 查看容器
docker ps -a
```CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
18a26aa93950        ubuntu:18.04        "/bin/bash"         15 seconds ago      Created                                 dazzling_lamport
```
#### inspect
查看容器内部细节
#### top
查看容器内运行的进程
#### attach
进到容器内
#### events
进到容器内（更好）
#### logs
查看容器日志
如：docker logs -f -t --since=”2018-09-10” --tail=10 f9e29e8455a5
-f : 查看实时日志
-t : 查看日志产生的日期
--since : 此参数指定了输出日志开始日期，即只输出指定日期之后的日志
--tail=10 : 查看最后的10条日志
#### wait
#### export
`docker export 1e560fca3906 > ubuntu.tar`
#### port
### 容器rootfs命令
#### commit
-m "提交的描述信息" -a "作者" 容器ID 要创建的目标镜像名称:[标签名]提交容器使之成为一个新的镜像。
#### cp
从容器内拷贝文件到宿主机.
如：docker cp f9e29e8455a5:/tmp/yum.log /root
#### diff
### 镜像仓库
#### login
#### pull
从Docker Hub上下载ubuntu:18.04镜像
* 下载镜像：`docker pull ubuntu:18.04`
#### push
#### search
从Docker Hub上查找镜像
### 本地镜像管理
#### images
查看docker镜像
docker images -a列出本地所有的镜像
docker images -p只显示镜像ID
docker images --digests显示镜像的摘要信息
docker images --no-trunc显示完整的镜像信息

* 查看镜像：`docker images`
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              18.04               775349758637        13 days ago         64.2MB
```
#### rmi
从Docker中删除hello-world镜像
docker rmi -f hello-world从Docker中强制删除hello-world镜像
docker rmi -f hello-world nginx从Docker中强制删除hello-world镜像和nginx镜像
docker rmi -f $(docker images -p)通过docker images -p查询到的镜像ID来删除所有镜像
#### tag
#### build
#### history
#### save
#### load
#### import
`cat docker/ubuntu.tar | docker import - test/ubuntu:v1`
### 信息
#### info
查看docker详细信息
#### version
查看docker版本
#### --help
查看docker命令

## Dockerfile
Dokerfile是用来构建docker镜像的文件！命令参数脚本！
构建步骤：
编写一个dockerfile文件
docker build构建一个镜像
docker run运行镜像
docker push发布镜像（DockerHub、阿里云镜像仓库）

### 基础知识
Dockerfile指令说明简洁版：

FROM
构建镜像基于哪个镜像

MAINTAINER
镜像维护者姓名或邮箱地址

RUN
构建镜像时运行的指令

CMD
运行容器时执行的shell环境

VOLUME
指定容器挂载点到宿主机自动生成的目录或其他容器

USER
为RUN、CMD、和 ENTRYPOINT 执行命令指定运行用户

WORKDIR
为 RUN、CMD、ENTRYPOINT、COPY 和 ADD 设置工作目录，就是切换目录

HEALTHCHECH
健康检查

ARG
构建时指定的一些参数

EXPOSE
声明容器的服务端口（仅仅是声明）

ENV
设置容器环境变量

ADD
拷贝文件或目录到容器中，如果是URL或压缩包便会自动下载或自动解压

COPY
拷贝文件或目录到容器中，跟ADD类似，但不具备自动下载或解压的功能

ENTRYPOINT
运行容器时执行的shell命令




















---
## 更改容器name
$ docker rename dazzling_lamport eNB

## 启动容器
sudo docker start 18a26aa93950

## 进入容器
sudo docker exec -it 18a26aa93950 /bin/bash

## 导出镜像（跨服务器导出镜像）
sudo docker save -o oai_base.tar oai_base:1.0
sudo scp ubuntu@10.38.161.190:/home/ubuntu/oai_base.tar /home/vranmec/images
sudo docker load --input oai_base.tar


## apt代理设置
echo "Acquire::http::proxy \"http://mos9test1:1766024495@10.0.58.8:8080\";" > /etc/apt/apt.conf
echo "Acquire::ftp::proxy \"http://mos9test1:1766024495@10.0.58.8:8080\";" >> /etc/apt/apt.conf


## 查看详细信息
docker inspect 44fc0f0582d9

## 添加网卡
docker network create --subnet 192.168.20.1/24 test_NetWork
docker network connect --ip 192.168.20.20 test_NetWork 6ba735d42d8a
docker network disconnect --ip 192.168.20.40 test_NetWork 96006473dab8
docker network rm 96006473dab8





## 新建selenium_pyautogui
0. 登录环境
ssh glte9729@10.38.2.115 glte9729/glte9729
1. 查看image
$ docker images
2. 创建容器
$ docker create -it python-selenium-on-docker-master_app /bin/bash



                "Source": "",
                "Destination": "",