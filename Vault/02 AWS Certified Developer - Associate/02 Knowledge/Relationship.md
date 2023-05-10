## Relationship

```mermaid
graph TB
    subgraph Section_3
        Regions                                     --1:n<br>n>=2-->                                       AZ[AZ<br>availability zone]
        AZ                                          --1:n-->                                               DC[discrete data centers]
    end
    subgraph CLI_Command
        查看版本-->cli0[aws --version]
        列出用户-->cli1[aws iam list-users]
    end
    subgraph Section_4
        IAM[IAM<br>Identity and Access Management]  --Policies Json文件分配权限-->                          User
        IAM                                         --Policies Json文件分配权限-->                          Groups
        User                                        --1:n n>=0<br>n:1 n>=0-->                              Groups
        IAM                                         -->                                                    Roles
        User                                        --VS<br>User是人使用<br>Roles是服务使用-->              Roles
        MFA[MFA<br>Multi Factor Authentication]     -->                                                    密码和安全设备组合的方式实现账号安全
        SDK[SDK<br>Software Developer Kit]          --Access Key 访问-->                                   AWS
        
        MC[Management Console]         q             --网页密码 + MFA打开-->                                 ACS[AWS CloudShell]
        ACS                                         -->                                                    CLI
        CLI[CLI<br>Command Line Interface]          --Access Key访问-->                                    AWS
        CLI                                         -->                                                    CLI_Command

        IAM                                         -->                                                    ST[Security Tools]
        ST                                          --Credentials Report-->                                了解账户的安全性
        ST                                          --Access Advisor-->                                    了解服务的使用情况
    end
```

[mermaid](https://juejin.cn/post/6893436635476819982)