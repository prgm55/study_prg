# coding:utf-8
import cv2

'''
手順
1. sudo apt install libopencv-dev
2. sudo apt install python-opencv
3. USBにカメラを挿す
'''

# システムに接続されているビデオデバイスをキャプチャする
cap = cv2.VideoCapture(-1)
# キャプチャに成功したか確認
if (cap.isOpened() is False):
    print("cam capture error. please try again!!")

while (cap.isOpened()):
    # 画像を読み込む
    # retは画像の取得成功フラグ
    ret, img = cap.read()

    # 画像をリサイズ
    img = cv2.resize(img, (340, 240))

    # 画像を表示する
    cv2.imshow('cam capture', img)

    # キーボード入力待ち(10msec)
    key = cv2.waitKey(10)

    if key == 27:  # ESCキーで終了
        break

# キャプチャを解放する
cap.release()
# ウィンドウをすべて消す
cv2.destroyAllWindows()
