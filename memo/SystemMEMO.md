# ラズパイベース電気錠



## システム構成
```mermaid
flowchart TD;
    subgraph コントローラー
        RaspberryPi1B;
        電流増幅＆スイッチング回路;
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
    5V電源===電流増幅＆スイッチング回路;
    NFCカードリーダー--->|USBシリアル|RaspberryPi1B;
    RaspberryPi1B-.デジタルI/O-.->電流増幅スイッチング回路;
    電流増幅＆スイッチング回路====ステッピングモーター;
    RaspberryPi1B-.GPIO-.->ステッピングモーター;
    RaspberryPi1B-.GPIO-.->LED1;
    RaspberryPi1B-.GPIO-.->LED2;
    RaspberryPi1B-.GPIO-.->LED3;
```

```mermaid
graph TD;
     USER--"arg1:IPBSM scan file"-->IPBSMscanDATAconvertLoop.sh;
     USER--"arg2:output directory name"-->IPBSMscanDATAconvertLoop.sh;
     IPBSMscanDATAconvertLoop.sh--"Fringe scan file (binary)"-->IPBSMdataConvertBinToText.sh;
     IPBSMdataConvertBinToText.sh--"Create converted dat file"-->IPBSMscanDATAconvertLoop.sh;
     IPBSMdataConvertBinToText.sh-->Node0[Python Process.];
     Node0---Node2[Intenisty dependence parameter Fit.];
     Node0---Node1[Modulation Fit.];
```
