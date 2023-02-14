import os

import cv2
import wx

from package.Filtering import FilteringMain

# メイン関数
def Main():
    app = wx.App()
    dialog = wx.FileDialog(None, u'動画像を選択してください。')
    dialog.ShowModal()

    # 画像処理
    ImageProcessing(dialog.GetPath())


# メッセージ出力
def OutPutMessage():
    message =   u'''
■操作説明
Enter：終了
1：フィルタリング再設定
                '''
    print(message)


# 画像処理
def ImageProcessing(file_path):
    __, ext = os.path.splitext(file_path)

    if  os.path.exists(file_path) and\
        ext == '.mp4':
        # 操作が分かるようにメッセージを出す
        OutPutMessage()

        cap_file = cv2.VideoCapture(file_path)

        update_module_cnt = 1
        update_flg = [True] * update_module_cnt
        
        while True:
            __, frame = cap_file.read()
            cv2.imshow("BaseImg", frame)

            # ①フィルタリング
            img_filter = FilteringMain(frame, update_flg[0])
            cv2.imshow("Filtering", img_filter)

            key = cv2.waitKey(30)
            # enterキーで
            # 閉じるようにしてみる
            if key == 13:
                break
            elif key == 49:
                update_flg[0] = True
            
            update_flg = [False] * update_module_cnt


if __name__ == '__main__':
    Main()
