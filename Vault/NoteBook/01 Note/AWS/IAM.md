* Type:
* Tags:
* Date: 2023-03-29 09:52:20
* Related:
* Reference:[]()

## IAM
IAM  = Identity and Access Management, Global service

Root account：自动创建，不使用，不分享。
Users：可以加入多个Group，可以不加入Group。
Groups：仅包含User，不包含Group。

权限
Users & Groups通过Json文件设置权限
只给用户需要的最小权限

* Consists of 
  * Version: policy language version, always include “2012-10-17”
  * Id: an identifier for the policy (optional) 
  * Statement: one or more individual statements (required)
* Statements consists of 
  * Sid: an identifier for the statement (optional) 
  * Effect: whether the statement allows or denies access (Allow, Deny)
  * Principal: account/user/role to which this policy applied to 
  * Action: list of actions this policy allows or denies 
  * Resource: list of resources to which the actions applied to 
  * Condition: conditions for when this policy is in effect (optional)

To access AWS, you have three options:
* AWS Management Console (protected by password + [[MFA#MFA|MFA]])
* AWS Command Line Interface ([[CLI#CLI|CLI]]): protected by access keys
* AWS Software Developer Kit ([[SDK#SDK|SDK]]) - for code: protected by access key

IAM Roles for Services 
* Some AWS service will need to perform actions on your behalf
* To do so, we will assign permissions to AWS services with IAM Roles
* Common roles:
  * EC2 ([[Amazon EC2#Amazon EC2|Amazon EC2]]) Instance Roles
  * Lambda ([[AWS Lambda#AWS Lambda|AWS Lambda]]) Function Roles
  * Roles for CloudFormation ([[AWS CloudFormation#AWS CloudFormation|AWS CloudFormation]])