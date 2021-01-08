# ロボットシステム学　第２回課題「ROS」

## 概要

ROSを用いて複数のプログラム間でデータのやり取りをする

count.pyとthree.pyからtwice.pyにデータを送り、twice.pyで計算をする。

## 動作環境

・Raspberry Pi 3

・Ubuntu 20.04

## 実行手順

#### Ⅰ. パッケージ作成

端末１で実行。ROS_PACKAGE_PATHがセットされているディレクトリ内でパッケージ作成

例：catkin_ws/srcで実行

```
catkin_create_pkg test rospy
```

#### Ⅱ プログラムダウンロード

端末１で実行

```
cd test
svn checkout https://github.com/Makitanaoki/ROS_mypkg/trunk/scripts
```

#### Ⅲ パーミッション設定

端末１で実行

```
cd scripts
chmod +x count.py
chmod +x twice.py
chmod +x three.py
```

#### Ⅳ 実行

端末１で実行

```
roscore &
```

端末２で実行

```
rosrun test count.py
```

端末３で実行

```
rosrun test three.py
```

端末４で実行

```
rosrun test twice.py
```

#### Ⅴ 結果確認

端末１で実行

```
rostopic echo /twice
```
