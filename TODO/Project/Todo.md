## Project
### 环境
![[Environment]]

任意语种翻译网站/APP

https://www.deepl.com/translator
https://regexper.com/#abc
https://github.com/Fireplusplus/Project
https://www.runoob.com/linux/linux-comm-awk.html
http://c.biancheng.net/

https://www.3gpp.org/ftp/Specs/2017-03/Rel-14/36_series/



### L1 SIM 调查与强化**
dlschsim, dlsim, pbchsim, prachsim



主要目的是 以后要对这些sim进行一些功能强化， 改造。得理解现在是怎么使用的， 可以带些什么参数 可以做哪些测试确认
所以 先搞清楚使用方法（编译， 执行命令 和命令参数， 执行过程和结果怎么确认）
然后是内部的调用（通过知道里面怎么调用 调用哪些函数 来知道可以测什么功能）
CI手顺 可以不用关注， 编译应该也简单的吧
-P | --phy_simulators)
            SIMUS_PHY=1
            echo_info "Will compile dlsim, ulsim, ..."
            shift;;
加上这个编译选项， 所有的dlsim ulsim prachsim都能生成
参考一下autotest或者ci_scripts里面的测试用例， 可以执行命令 和 一些命令参数，自己拿一两个试一下，看看是怎么执行， 执行结束后是怎么样的， 怎么判断测试OK NG。
然后看代码 每个参数表示什么意思。  里面怎么个调用


* 资料
  * 代码：git clone -b feature_mmWave_nfapi_f1ap http://10.167.14.30:8081/gitlab/training/mtc-oai


[说明](https://gitlab.eurecom.fr/oai/openairinterface5g/-/wikis/OpenAirLTEPhySimul)
![[dlschsim#dlschsim|dlschsim]]



@import "dlschsim_dlsim_pbchsim_prachsim.md"