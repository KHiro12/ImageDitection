import cv2


# フィルタリングメイン関数
def FilteringMain(img,  use_filter_val):
    out_img = img.copy()

    if use_filter_val & 1:
        new_img = out_img.copy()

        # 移動平均フィルタ
        out_img = AveragingFiltering(new_img)

    return out_img


# 移動平均フィルタ
def AveragingFiltering(img):
    return cv2.blur(img, (5, 5))
