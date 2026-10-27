# ハードウェア変更点

## ・メカロック位置変更
公開されているMEVIUS2[［STEP］](https://drive.google.com/file/d/1VVRDvQnQ7rvskTo5p29nU_5rZEmNpDMs/view?usp=drive_link)はURDFと可動範囲が異なったため、メカロックの位置を下記のように変更した。

### Front scapula Link(LR)
 
 従来の取り付け位置から約45度下方向へオフセットして取り付ける。（左右同様）

![](../imgs/Picture(1).png)

### Rear scapula Link(LR)

 従来の取り付け位置から約45度上方向へオフセットして取り付ける。（左右同様）

![](../imgs/Picture(2).png)


## ・Thigh-Baseの取り付けネジの変更
キャップボルトM4x10-6本で取り付けるが、モーターの背面カバーと干渉していたためフランジボルトM4x10[（FCFB-0410E）](https://wilco.jp/products/F/FCFB-E.html?srsltid=AYCX9vK7_wGaloyCi-u5aTNBCZpLVzGsnpHLx0r82s3PjJWDfJF5lQU6#page2)へ変更した。

![](../imgs/Picture(3).png)

※実機の取り付けは可能であるが、フランジボタンボルトへ交換後もCADモデルにおいて0.3㎜の干渉がある。 [スーパーローヘッド小頭ボルト](https://wilco.jp/products/F/FSLCJ.html#page2)であれば干渉回避可能（未確認）

![](../imgs/Picture(4).png)


## ・C1カメラUSB3.0変換キット取り付け位置追加
胴体下部のMID360取り付けマウント部品上部へC1カメラに使用するGMSL2-USB3.0変換器を取り付けた。そのため、マウント部品を写真のように修正。取り付けは[バインドタッピングねじ(FPB-0308N)](https://wilco.jp/products/F/FPB-N.html#page3)4本。MID360取り付けた後に変換器を取り付ける。

![](../imgs/Picture(6).png)
![](../imgs/Picture(5).jpg)


## ・LANハブポケット追加
Jetson Orin NanoとMID360の間の空間へ[LANハブ](https://www.elecom.co.jp/products/EHC-G05PA2-SB.html)を差し込むためのポケットを作る部品を作成。デフォルトのJetson_Mount_Partsと友締めして使用する。電源はUSBケーブル（L字右向き）にてJetsonより供給。

![](../imgs/Picture(7).png)
![](../imgs/Picture(8).jpg)


## ・パワーリレー変更
電源を集約させるハブ基板を自作した都合により、MEVIUSで採用されていた24V仕様の[G9EA-1-B-DC24](https://www.mouser.jp/ja/ProductDetail/Aratas/G9EA-1-B-DC24?qs=kyocjfxn8IpTNiEC0SG84w%3D%3D&srsltid=AfmBOop8Fsg62AKT4ep_9ZintpOjsWtRhvrL3rlpx6m-nCIsB1G8fSEH)へ変更。


