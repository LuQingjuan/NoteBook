## TODO
### 项目组
#### L5G CI
- [x] L5G CI 同时查看手机电池和CPU温度
    xml中`UE_Battery_Temperature`变为`UE_Temperature`
    ```
    branch:L5G_CI_develop
    commit:66c835966a5269d8c43e2cee54d47e6a70509d22
    ```
    - [ ] 验证命令`adb -s ' + device_id + ' shell dmesg | grep temperature | awk '{print $6}'`
    - [ ] 验证机能
- [x] L5G CI 查看手机电量、电池和CPU温度的时候，如果结果获取失败，显示命令执行的输出信息
    ```
    branch:L5G_CI_develop
    commit:d5007fdd949219160aa63d066366c91c477dcfec
    ```
    - [ ] 验证机能
#### 环境
![[Environment]]

### 云奥
#### SONiC
- [ ] ![[SONiC#SONiC|SONiC]]
#### AWS
- [ ] ![[AWS Certified Developer Associate#笔记|AWS Certified Developer Associate]]

- [ ] ![[Amazon EC2#Amazon EC2|Amazon EC2]]
- [ ] ![[Amazon ECR#Amazon ECR|Amazon ECR]]
- [ ] ![[Amazon ECS#Amazon ECS|Amazon ECS]]
- [ ] ![[AWS Elastic Beamstalk#AWS Elastic Beamstalk|AWS Elastic Beamstalk]]
- [ ] ![[AWS Lambda#AWS Lambda|AWS Lambda]]
- [ ] ![[Elastic Load Balancing#Elastic Load Balancing|Elastic Load Balancing]]
- [ ] ![[Amazon CloudFront#Amazon CloudFront|Amazon CloudFront]]
- [ ] ![[Amazon Kinesis#Amazon Kinesis|Amazon Kinesis]]
- [ ] ![[Amazon Route 53#Amazon Route 53|Amazon Route 53]]
- [ ] ![[Amazon S3#Amazon S3|Amazon S3]]
- [ ] ![[Amazon RDS#Amazon RDS|Amazon RDS]]
- [ ] ![[Amazon Aurora#Amazon Aurora|Amazon Aurora]]
- [ ] ![[Amazon DynamoDB#Amazon DynamoDB|Amazon DynamoDB]]
- [ ] ![[Amazon ElasticCache#Amazon ElasticCache|Amazon ElasticCache]]
- [ ] ![[Amazon SQS#Amazon SQS|Amazon SQS]]
- [ ] ![[Amazon SNS#Amazon SNS|Amazon SNS]]
- [ ] ![[AWS Step Functions#AWS Step Functions|AWS Step Functions]]
- [ ] ![[Auto Scaling#Auto Scaling|Auto Scaling]]
- [ ] ![[Amazon API Gateway#Amazon API Gateway|Amazon API Gateway]]
- [ ] ![[Amazon SES#Amazon SES|Amazon SES]]
- [ ] ![[Amazon Cognito#Amazon Cognito|Amazon Cognito]]
- [ ] ![[Amazon CloudWatch#Amazon CloudWatch|Amazon CloudWatch]]
- [ ] ![[Amazon EC2 Systems Manager#Amazon EC2 Systems Manager|Amazon EC2 Systems Manager]]
- [ ] ![[AWS CloudFormation#AWS CloudFormation|AWS CloudFormation]]
- [ ] ![[AWS CloudTrail#AWS CloudTrail|AWS CloudTrail]]
- [ ] ![[AWS CodeCommit#AWS CodeCommit|AWS CodeCommit]]
- [ ] ![[AWS CodeBuild#AWS CodeBuild|AWS CodeBuild]]
- [ ] ![[AWS CodeDeploy#AWS CodeDeploy|AWS CodeDeploy]]
- [ ] ![[AWS CodePipline#AWS CodePipline|AWS CodePipline]]
- [ ] ![[AWS X-Ray#AWS X-Ray|AWS X-Ray]]
- [ ] ![[AWS KMS#AWS KMS|AWS KMS]]
- [ ] ![[AWS KMS#AWS KMS|AWS KMS]]
- [ ] ![[CLI#CLI|CLI]]
- [ ] ![[SDK#SDK|SDK]]
#### NoteBook 项目

### 生活

---
## 2023-04-06
### 项目
资料做成：
	测试手顺资料做成
		D:\SVN\01-ワークライブラリー\vRAN\07_検討資料\18_CI自動化\05_Radisys\Radisys_試験項目_8E_CIシナリオ.xlsx
	项目说明材料做成：
		D:\Git\L5G_CI\doc\L5GC_CI2_dev_6a2dbc32b26ea31fece3b33a93fa81e88cb9a845\pythonスクリプト構造資料_20230411.xlsx
### Note