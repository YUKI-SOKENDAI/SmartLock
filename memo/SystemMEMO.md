# ラズパイベース電気錠



## システム構成
```mermaid
flowchart TD;
    subgraph コントローラー
        CntNode0[Raspberry Pi 1B];
        CntNode1[電流増幅&スイッチング回路];
    end
    subgraph 電源
        100V単相;
        5V電源;
    end
    subgraph 制御デバイス
        ステッピングモーター;
        LED1;
        LED2;
        LED3;
    end
    subgraph 読み取りデバイス
        NFCカードリーダー;
    end
    100V単相===5V電源;
    5V電源===CntNode1;
    NFCカードリーダー--->|USBシリアル|CntNode0;
    CntNode0-.GPIO-.->CntNode1;
    CntNode1====ステッピングモーター;
    CntNode0-.GPIO-.->ステッピングモーター;
    CntNode0-.GPIO-.->LED1;
    CntNode0-.GPIO-.->LED2;
    CntNode0-.GPIO-.->LED3;
```


import binascii
import RPi.GPIO as GPIO
import time
import datetime
#from retry import retry
import numpy as np

## external library
import nfc
import pandas as pd

## 処理の流れ
```mermaid
graph TD;
     BootRaspberryPi->Initial 
     USER--"card touch"-->;
     USER--"arg2:output directory name"-->IPBSMscanDATAconvertLoop.sh;
     IPBSMscanDATAconvertLoop.sh--"Fringe scan file (binary)"-->IPBSMdataConvertBinToText.sh;
     IPBSMdataConvertBinToText.sh--"Create converted dat file"-->IPBSMscanDATAconvertLoop.sh;
     IPBSMdataConvertBinToText.sh-->Node0[Python Process.];
     Node0---Node2[Intenisty dependence parameter Fit.];
     Node0---Node1[Modulation Fit.];
```
