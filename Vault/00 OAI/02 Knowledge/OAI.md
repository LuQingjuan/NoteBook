[mermaid](https://juejin.cn/post/6893436635476819982)
## Build
git clone http://10.167.14.30:8081/gitlab/training/mtc-oai.git
cd openairinterface5g
git checkout feature_mmWave_nfapi_f1ap
source oaienv
cd cmake_targets
sudo -E ./build_oai --gNB --nrUE -x -c -w None
### Parameter
```mermaid
graph LR
    gNB         -->nr-softmodem
    nrUE        -->nr-uesoftmodem
    Common      -->params_libconfig
    Common      -->coding
    Common      -->rfsimulator
    gNB         -->nr-cuup

    eNB         -->lte-softmodem
    UE          -->lte-uesoftmodem
```
### nr-softmodem
```mermaid
  sequenceDiagram
    participant oai as build_oai
    participant help as build_helper
    oai->>help:source "$THIS_SCRIPT_PATH"/tools/build_helper
    Note right of help:set_openair_env()
```
### nr-uesoftmodem
```mermaid
  sequenceDiagram
    participant A as Alice
    participant J as John
    A->J: Hello John, how are you?
    Note left of A : Bob thinks
    J->A: Great!

    Alice->Bob: Hello Bob, how are you?
    alt is sick
        Bob->>Alice: Not so good :(
    else is well
        Bob->>Alice: Feeling fresh like a daisy
    end
    opt Extra response
        Bob->>Alice: Thanks for asking
    end
```

链接：https://juejin.cn/post/6893436635476819982