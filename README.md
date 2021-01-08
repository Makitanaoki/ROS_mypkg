# ロボットシステム学　第２回課題「ROS」

## 概要

・ROSを用いて複数のプログラム間でデータのやり取りをする

・count.pyとthree.pyからtwice.pyに数字を送り、twice.pyで×2をする


## 動作環境

・Raspberry Pi 3

・Ubuntu 20.04

## 実行手順

#### Ⅰ. パッケージ作成

端末1で実行。ROS_PACKAGE_PATHがセットされているディレクトリ内でパッケージ作成

例：catkin_ws/srcで実行

```
catkin_create_pkg test rospy
```

#### Ⅱ プログラムダウンロード

端末1で実行

```
cd test
svn checkout https://github.com/Makitanaoki/ROS_mypkg/trunk/scripts
```

#### Ⅲ パーミッション設定

端末1で実行

```
cd scripts
chmod +x count.py
chmod +x twice.py
chmod +x three.py
```

#### Ⅳ 実行

端末1で実行

```
roscore &
```

端末2で実行

```
rosrun test count.py
```

端末3で実行

```
rosrun test three.py
```

端末4で実行

```
rosrun test twice.py
```

#### Ⅴ 結果確認

端末1で実行

```
rostopic echo /twice
```

#### Ⅵ 終了手順

端末2,3,4でCTRL+C

端末1でroscoreのプロセス番号を確認し、killコマンドで停止

```
ps
kill [プロセス番号]
```

## ライセンス

BSD 3-Clause License
