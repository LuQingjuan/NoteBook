## radisysCU_CI
10.38.161.30
branch: radisysCU_CI_dev
xml_files/du_outOfService.xml
/home/ubuntu/smbshare/work_jftt/yinc/CI_Scripts/radisysCU_WRCP


F1SIM:
ssh ubuntu@10.38.161.196 -p 10351
docker exec -it f1sim bash
/opt/oai5g_sa_du/cmake_targets

http://10.38.161.30:8080/job/radisysCU_CI/367/artifact/

### openairinterface5g
10.167.14.32  jftt/jftt
/home/jftt/work_jftt/wu/jftt_git/openairinterface5g/cmake_targets
1: 编译 sudo -E ./build_oai --gNB --nrUE -x -c -w None
#### RFSIM：
sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa --nokrnmod -O gnb.band261.tm1.66PRB.usrpn300.conf
sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem -r 66 --numerology 3 --band 261 -C 27547560000 --rfsim --sa --nokrnmod -O ue.conf --ssb 168

#### CU/DU分离+RFSIM：
sudo ./ran_build/build/nr-softmodem --rfsim --sa -O gNB_SA_CU_fr2.conf
sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa -O gNB_SA_DU_fr2.conf
sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem -r 66 --numerology 3 --band 261 -C 27547560000 --rfsim --sa --nokrnmod -O ue.conf --ssb 168

#### nFAPI分离+RFSIM：
sudo ./ran_build/build/nr-softmodem --sa -O gnb.band261.tm1.66PRB.nfapi.conf --nfapi VNF
sudo RFSIMULATOR=server ./ran_build/build/nr-softmodem --rfsim --sa -O oaiL1.nfapi.usrpx300.conf --nfapi PNF
sudo RFSIMULATOR=127.0.0.1 ./ran_build/build/nr-uesoftmodem -r 66 --numerology 3 --band 261 -C 27547560000 --rfsim --sa --nokrnmod -O ue.conf --ssb 168