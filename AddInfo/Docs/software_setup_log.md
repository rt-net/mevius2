# ソフトウェア環境構築確認箇所

## <ROS（Noetic）の環境構築>

#### ROS（Noetic）のインストールについては[公式サイト](https://wiki.ros.org/ja/noetic/Installation/Ubuntu)を参照。

・Desktop-Fullをインストール。

## <Python依存ライブラリ>
#### 下記のPython依存ライブラリをインストール

- pytorch
- scipy
- can
- mujoco
- mujoco-python-viewer
- urdf_parser_py

## <PS4コントローラー>

#### Bluetoothにて使用する場合下記ライブラリをインストール
- ds4drv

※動作確認した環境ではBluetoothにて接続し操作ができなかった。有線駆動を前提にコントローラーをUSBケーブルにてJetsonと接続し、認識されていたら本ライブラリのインストールは不要。

## <GS_USBの確認>
USB-CANデバイスを2つJetsonと接続したうえで下記コマンドにて確認

```
lsmod | grep gs_usb
```

```
ip link show
```
にてCAN0とCAN1が確認できる。

### USBCANの固定化はMEVIUS2のREADME[（Setup Can Devices)](https://github.com/haraduka/mevius2#setup-can-devices)を参照する。

#### ※CAN0＝前方（モーターID1.2.3.4.5.6）
#### ※CAN1＝後方（モーターID7.8.9.10.11.12）

parameters.pyのモーターIDとCANIDの指定の変更が必要。

## <Livox_ros_driver2の確認>


