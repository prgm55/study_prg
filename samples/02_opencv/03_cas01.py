# coding:utf-8
import cv2
import cv2.cv as cv
import time

'''
手順
1. sudo apt install libopencv-dev
2. sudo apt install python-opencv
3. wget http://eclecti.cc/files/2008/03/haarcascade_frontalface_alt.xml
4. USBにカメラを挿す
'''

# カスケード分類器の顔検出
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

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


while (cam_opened) :
    # 画像を読み込む
    # retは画像の取得成功フラグ
    ret, img = cap.read()

    # 画像をリサイズ
    img = cv2.resize(img, (340, 240))

    # グレイスケール化（モノクロ画像にしている）
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # カスケード分類器による顔検出を実行
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30),
        flags=cv.CV_HAAR_SCALE_IMAGE
    )

    # 検出した顔の位置に矩形を描画
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # 画像を表示する
    cv2.imshow('cam capture detect', img)

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

