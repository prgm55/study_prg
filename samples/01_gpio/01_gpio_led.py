# coding: utf-8

# pythonのモジュールをインポート
import pigpio
import time

# pigpio初期化
pi = pigpio.pi()

PIN = 17
# 指定したピンを出力モードに設定
pi.set_mode(PIN, pigpio.OUTPUT)

COUNT = 5
# forループを5回繰り返す
for _ in range(COUNT):
    # 変数「 _ 」には、何回目のループかという回数が格納されている
    #print(_)

    # 指定したピンをON状態にする
    pi.write(PIN, True)
    # 1秒間待機
    time.sleep(1.0)
    # 指定したピンをOFF状態にする
    pi.write(PIN, False)
    # 1秒間待機
    time.sleep(1.0)

