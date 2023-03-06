# ラズパイ駆動の電気錠


## システム構成
### 使用機材
- Raspberry Pi 1B
- ステッピングモーター（MG90S）
- NFCカードリーダー（"PaSoRi" RC-S380/S ??）
- 電流増幅/スイッチング回路（自作）

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

<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215906.jpg">

| | | |
|:-----------|------------:|:------------:|
|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215801.jpg">|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215803.jpg">|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215817.jpg">|
|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215901.jpg">|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215914.jpg">|<img width="400" src="https://github.com/YUKI-SOKENDAI/SmartLock/blob/master/fig/IMG_20230221_215921.jpg">|

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

## 処理の流れ
```mermaid
sequenceDiagram
    participant user as 開発者
    participant user1 as ユーザー
    participant raspi as ラズパイ
    participant nfc as NFCリーダー
    participant servo as サーボモーター
    participant circuit as 電流増幅/スイッチング・インジケーター回路
    
    # hoge
    Note over user: 登録IDリストの作成
    user->>+raspi: 電源ON
    Note over raspi : Run python script
    Note over raspi : python script：初期処理
    
    raspi->>nfc: Connect NFC
    raspi->>circuit: LED1 OFF (Power status)
    raspi->>circuit: トランジスタON
    circuit-->>servo: Power ON (send PWM signal)
    raspi->>servo: Close
    raspi->>circuit: トランジスタOFF
    raspi->>circuit: LED3 OFF (Door open/close status)
    Note over raspi : NFCIDリストの読み込み
    raspi->>-circuit: LED2 ON (電気錠システム稼働状態通知)
    circuit-->>user: 運転状況の確認
    
    loop ループ処理
        user1->>nfc: NFCカードタッチ
        nfc-->>raspi:ID取得
        Note over raspi: 登録IDリスト参照
        alt 登録IDリストとマッチ
            raspi->>circuit: トランジスタON
            circuit-->>servo: Power ON
            raspi->>servo: Open/Close (send PWM signal)
            raspi->>circuit: トランジスタOFF
            raspi->>circuit: LED3 ON/OFF (Door open/close status) 
        end
    
        Note over user1 : 施術・開錠の確認
        alt 施錠
            Note over user1 :退室
        else 開錠
            Note over user1 :入室
        end
    end
    
    #raspi-->>user: こんにちは！！

```
