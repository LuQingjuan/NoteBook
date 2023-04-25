
## token
### github生成token
1. 进入个人github账户setting
2. 点击Developer settings
3. 选择Personal access tokens
4. 点击 Generate new token
5. Note 为你创建的token添加描述
6. Expiration 选择token有效期时间。可以选择永不过期
7. 为token赋予权限。如果从命令行操作仓库，至少选中repo
8. 点击生成。生成之后先复制下来，后面会用到。注意：离开这个页面，之后你将看不见这个token的明文了。
### 使用token
```
$ vi .git/config
     url = https://<your_token>@github.com/<USERNAME>/<REPO>
    <your_token>：换成你自己得到的token
    <USERNAME>：是你自己github的用户名
    <REPO>：是你的仓库名称
```
test