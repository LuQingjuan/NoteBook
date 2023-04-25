## Relationship

* Management Console
  * CloudShell
  * IAM
    * User
      * root
        * MFA
      * Policies
        * Json 
      * Access Key
    * Group
    * Role
* SDK
* CLI
  * aws --version
  * aws iam list-users

```mermaid
graph TB
    subgraph AWS
        subgraph IAM
            /*Group\n仅包含用户
            User\n允许不属于任何Group*/
            Group
            User-->root
            Policies-->User
            Policies-->Group
            User-->AccessKey
            Role
        end
        MFA-->root
        CloudShell-->CLI
    end

    ManagementConsole--User Password-->AWS
    SDK--Access Key-->AWS
    CLI--Access Key-->AWS

    CLI--aws iam-->IAM
```

[mermaid](https://juejin.cn/post/6893436635476819982)