# coding:utf-8
import cv2
import time

'''
手順
1. sudo apt install libopencv-dev
2. sudo apt install python-opencv
3. USBにカメラを挿す
'''

# カメラキャプチャ成功フラグ
cam_opened = False

while (cam_opened == False):
    # システムに接続されているビデオデバイスをキャプチャする
    cap = cv2.VideoCapture(-1)
    # キャプチャに成功したか確認
    cam_opened = cap.isOpened()
    if cam_opened:
        print("cam capture success!!")
    else:
        print("cam capture error. please wait ...")
    time.sleep(1)

while (cam_opened):
    # 画像を読み込む
    # retは画像の取得成功フラグ
    ret, img = cap.read()

    # 画像をリサイズ
    img = cv2.resize(img, (340, 240))

    # グレイスケール化（モノクロ画像にしている）
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # エッジ検出
    # img = cv2.Canny(img, 100, 200)

    # 画像を表示する
    cv2.imshow('cam capture', img)

    # キーボード入力待ち(10msec)
    # 「& 0xFF」は論理積（アンド演算）で下位8bitのみ取り出す処理
    key = cv2.waitKey(10) & 0xFF

    # qが押された場合は終了する
    # 「ord()」文字列をASCIIのコード(整数)に変換
    if key == ord('q'):
        break
    # sが押された場合は保存する
    if key == ord('s'):
        path = "photo.jpg"
        cv2.imwrite(path, img)

# キャプチャを解放する
cap.release()
# ウィンドウをすべて消す
cv2.destroyAllWindows()
