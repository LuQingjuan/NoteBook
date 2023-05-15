## Project
### 环境
![[Environment]]

### L1 SIM： dlschsim, dlsim, pbchsim, prachsim  的调查与强化**
* 资料
  * 代码：git clone -b feature_mmWave_nfapi_f1ap http://10.167.14.30:8081/gitlab/training/mtc-oai
  * 说明文档：
    * doc/L1SIM.md
* 编译
```
source oaienv 
cd openairinterface5g/cmake_targets/
./build_oai --phy_simulators
```
* CI
```
cd autotests
./run_exec_autotests.bash -c test_case_list.xml

cat cmake_targets/autotests/log/results_autotests.xml
```

[说明](https://gitlab.eurecom.fr/oai/openairinterface5g/-/wikis/OpenAirLTEPhySimul)
![[dlschsim#dlschsim|dlschsim]]


* dlschsim
@import "dlschsim.md"
* dlsim
* pbchsim
* prachsim