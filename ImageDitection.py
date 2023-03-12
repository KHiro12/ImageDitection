import json
import os

import cv2
import wx

from package.Gamma import GammaMain
from package.Filtering import FilteringMain


# メイン関数
def Main():
    _ = wx.App()
    dialog = wx.FileDialog(None, u'動画像を選択してください。')
    dialog.ShowModal()

    # 画像処理
    ImageProcessing(dialog.GetPath())


# メッセージ出力
def OutPutMessage():
    message = u'''
■操作説明
Enter：終了
                '''
    print(message)


# 設定ファイルを読み込む
def ReadSetting(setting_target):
    output_dict = dict(zip(setting_target, [0]*len(setting_target)))
    update_flg = False

    if os.path.exists('.\\setting.json'):
        with open('.\\setting.json') as f:
            df = json.load(f)

            if len(output_dict) == len(df):
                output_dict = df
                update_flg = True

    if not update_flg:
        with open('.\\setting.json', 'w') as f:
            json.dump(output_dict, f, indent=2)

    return output_dict


# 画像処理
def ImageProcessing(file_path):
    __, ext = os.path.splitext(file_path)

    if os.path.exists(file_path) and\
       ext == '.mp4':
        # 操作が分かるようにメッセージを出す
        OutPutMessage()

        cap_file = cv2.VideoCapture(file_path)

        setting_target = ['Gamma',
                          'Filtering']

        # 設定読み込み
        setting_dict = ReadSetting(setting_target)

        while True:
            __, frame = cap_file.read()
            cv2.imshow("BaseImg", frame)

            # ①ガンマ補正
            img_gamma = GammaMain(frame, setting_dict['Gamma'])
            cv2.imshow("Gamma", img_gamma)

            # ②フィルタリング
            img_filter = FilteringMain(img_gamma, setting_dict['Filtering'])
            cv2.imshow("Filtering", img_filter)

            key = cv2.waitKey(30)
            # enterキーで
            # 閉じるようにしてみる
            if key == 13:
                break


if __name__ == '__main__':
    Main()
