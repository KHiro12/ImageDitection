Use_Filter_Val = 0  # フィルタリングを行う判定用の数値


# フィルタリングメイン関数
def FilteringMain(img, change_flg):
    global Use_Filter_Val

    out_img = img.copy()
    filter_val = ChangeMode(change_flg, Use_Filter_Val)

    Use_Filter_Val = filter_val

    return out_img


# フィルタリング設定
def ChangeMode(change_flg, before_val):
    output_val = before_val

    if change_flg:
        message = '''
フィルタリング
'''
        output_val = input(message)
    return output_val
