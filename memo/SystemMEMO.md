# ラズパイベース電気錠



## システム構成
### 環境
- python ver.
### python ライブラリ
- 内部ライブラリ
   - binascii
   - RPi.GPIO
   - time
   - datetime
   - numpy
- 外部ライブラリ
   - nfc
   - pandas

### 使用機材
- Raspberry Pi 1B
- ステッピングモーター（）
- NFCカードリーダー（）

```mermaid
flowchart TD;
    subgraph コントローラー
        CntNode0[Raspberry Pi 1B];
        CntNode1[電流増幅・スイッチング回路];
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
     
     UsrNode0->SysNode0 
     
```
