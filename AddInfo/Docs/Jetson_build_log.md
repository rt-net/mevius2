# Jetson 環境構築確認箇所

## Jetson Orin NanoとキャリアボードA603の組立

#### Jetson Orin Nanoに取り付ける[Aluminum Heatsink with Fan](https://www.switch-science.com/products/9229?srsltid=AYCX9vIxZyWiOOXz0VBRDv8PHQl1QctZIeffKNlTrp1zQLGWcP7kaBxY)のケーブルが短くA603キャリアボードに取り付けできない。（赤矢印）

青矢印部分にあるねじ3か所を外し、ヒートシンクのFanを取り外す。向きをずらし取り付け直しケーブル出口を修正する。

![](../imgs/Picture(9).JPG)


![](../imgs/Picture(10).JPG)

#### 搭載するSSDはM.2SSD（サイズ2242）256GB使用。

![](../imgs/Picture(11).JPG)

#### JetPack OSのフラッシュ

A603キャリアボードへJetPack OSをフラッシュする。
[Seeed studioのWiki](https://wiki.seeedstudio.com/ja/reComputer_A603_Flash_System/)の手順に従う。

| Jetsonモジュール | JetPackバージョン |L4Tバージョン|
|----|----|----|
|Jetson Orin Nano 8GB|5.1.4|35.6.0|

ROS1(Noetic)環境で動かすため、Ubuntu20.04であること、USBCANモジュールを使用するため、GS_USBカーネルモジュールが標準で組み込まれていたため採用。
※JetPack6.0以降を使用する際はGS_USBはビルドする必要あり

赤矢印のフラッシュしたいバージョンのドキュメントに従う。
青矢印の圧縮されたドライバーファイルを展開する際、ファイルの置き換えを要求される。「A」を入力しENTERを推します。（JP5.1.1のドキュメントに記載あり）

![](../imgs/Picture(12).png)
![](../imgs/Picture(13).png)
（Seeed Studio Wikiより引用）


#### A603 CANインターフェースについて
A603キャリアボードには、CANトランシーバーが搭載されているが、MEVIUS2を動作させるにあたり使用しないので、[Wikiに記載のある有効化の作業](https://wiki.seeedstudio.com/ja/reComputer_A603_Flash_System/#can-%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%95%E3%82%A7%E3%83%BC%E3%82%B9)は行わない。


