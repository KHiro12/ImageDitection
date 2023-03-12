import cv2
import numpy as np


# ガンマ補正メイン
def GammaMain(img,  use_filter_val):
    img_out = img.copy()

    if use_filter_val & 1:
        # ガンマゲインを補正する
        gain = CalcGammaValue(img)
        img_out = GammaCorrection(img, gain)
    elif use_filter_val & 2:
        # ガンマ補正値固定
        img_out = GammaCorrection(img, 1.5)
    elif use_filter_val & 4:
        # ガンマ補正値固定
        img_out = GammaCorrection(img, 0.5)
    else:
        # 何もしない
        pass

    return img_out


# ガンマ補正値を計算(画面輝度から計算してみる)
def CalcGammaValue(img):
    gain = 1.0
    gain_range = {'MIN': 0.1,
                  'MAX': 2.0}

    # 画像の輝度中央値を算出
    kido_mid = np.median(img)

    # 中央値が低いと明るく、高いと暗くなるように補正
    gain_diff = gain_range['MAX'] - gain_range['MIN']
    gain = gain_range['MAX'] - (kido_mid * (gain_diff / 255))

    return gain


# ガンマ補正
def GammaCorrection(img, gamma):
    # ガンマ補正用数値計算
    img2gamma = np.zeros((256, 1), dtype='uint8')

    for i in range(256):
        img2gamma[i][0] = 255 * pow(float(i)/255, 1.0/gamma)

    # γ変換
    img_out = cv2.LUT(img, img2gamma)

    return img_out
