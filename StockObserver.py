import tushare as ts
import pandas as pd
import time

var = 1

print("价格监控开始...")
while var == 1:
    # 这里表示3秒钟循环一次
    time.sleep(3)
    stock_list = ['600258', '600036', '512800', '000002', '601933', '600600', '159920', '600887', '600048']
    df = ts.get_realtime_quotes(stock_list)
    # 首旅酒店
    if float(df[df['code'] == '600258']['price']) <= 15.8:
        print(df[df['code'] == '600258'])
    # 招商银行
    if float(df[df['code'] == '600036']['price']) <= 36:
        print(df[df['code'] == '600036'])
    # 银行ETF
    if float(df[df['code'] == '512800']['price']) <= 1.06:
        print(df[df['code'] == '512800'])
    # 万科A
    if float(df[df['code'] == '000002']['price']) <= 26.5:
        print(df[df['code'] == '000002'])
    # 永辉超市(7.5进入观察，买点在7.5以下)
    if float(df[df['code'] == '601933']['price']) <= 7.5:
        print(df[df['code'] == '601933'])
    # 青岛啤酒(按照2020年中报TTM市盈率30估算的合理价格)
    if float(df[df['code'] == '600600']['price']) <= 45.9:
        print(df[df['code'] == '600600'])
    # 恒生ETF
    if float(df[df['code'] == '159920']['price']) <= 1.3:
        print(df[df['code'] == '159920'])
    # 伊利股份 预测2020归母利润70.49亿，30倍PE价格应为35
    if float(df[df['code'] == '600887']['price']) <= 35:
        print(df[df['code'] == '600887'])
    # 保利地产
    if float(df[df['code'] == '600048']['price']) <= 15.45:
        print(df[df['code'] == '600048'])
