* Type:
* Tags:
* Date: 20230424
* Related:
* Reference:[]()

## MFA
MFA = Multi Factor Authentication
多因素身份验证

MFA可以保护root账号及其他IAM用户
MFA 通过密码和安全设备组合的方式实现账号安全
如果密码泄露，因为没有安全设备（比如手机）所以也不能登陆

### MFA设备
* Virtual MFA device（虚拟）
  * Google Authenticator（一次只能在一部手机上工作）
  * Authy（多个账号在一个设备上使用）
* Universal 2nd Factor（U2F）Security Key（物理）
  * YubicoKey（Yubico是AWS第三方提供的，不是AWS提供的）
* Hardware Key Fob MFA Device
  * AWS第三方提供
* Hardware Key Fob MFA Device for AWS GovCloud（US）