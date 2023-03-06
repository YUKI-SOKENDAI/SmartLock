# ラズパイ駆動の電気錠


## システム構成
### 使用機材
- Raspberry Pi 1B
- ステッピングモーター（MG90S）
- NFCカードリーダー（"PaSoRi" RC-S380/S ??）

```mermaid
flowchart TD;
    subgraph コントローラー
        CntNode0[Raspberry Pi 1B];
        CntNode1[電流増幅/スイッチング回路];
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


### 環境
- python3
- ラズパイOS（rasbian ）
### python ライブラリ
- 内部ライブラリ
   - binascii
   - RPi.GPIO
   - time
   - datetime
   - numpy
- 外部ライブラリ
   - nfc （NFCリーダー制御用ライブラリ）
   - pandas


## 設置外観

| Left align | Right align | Center align |
|:-----------|------------:|:------------:|
|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215801.jpg">|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215803.jpg">|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215817.jpg">|
|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215901.jpg">|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215914.jpg">|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215921.jpg">|

<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215906.jpg">




## 処理の流れ
```mermaid
graph TD;
     subgraph user_side
       UsrNode0[Boot Raspberry Pi]
       UsrNode1[Card touch]
     end
     
     subgraph system_side
       SysNode0[Initial process]
     end
     
     subgraph process_side
       ProcNode0[Initial process]
     end
     
     UsrNode0--->SysNode0 
     
```
