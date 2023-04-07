## Ubuntu版本升级
1. 查看系统版本：`cat /etc/os-release`
```
```
2. 更新软件包的索引：`sudo apt-get update`
```
```
3. 更新软件包：`sudo apt-get dist-upgrade -y`
```
```
4. 安装更新管理内核：`sudo apt-get install -y update-manager-core`
```
```
5. 确认LTS版本：`sudo nano /etc/update-manager/release-upgrades`
```
```
6. 升级至下一个版本：`sudo do-release-upgrade`
```
```
7. 重启系统：``
```
```
8. 查看系统版本：`cat /etc/os-release`
```
```

### 参考资料:
[Ubuntu 版本升级](https://blog.csdn.net/carefree2005/article/details/129022768)