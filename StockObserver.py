import tushare as ts
import pandas as pd
import time

var = 1

print("价格监控开始...")
while var == 1:
    # 这里表示3秒钟循环一次
    time.sleep(10)
    stock_list = ['600258', '600036','512800','000002','601933']
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
    if float(df[df['code'] == '000002']['price']) <= 24.9:
        print(df[df['code'] == '000002'])
    # 万科A
    if float(df[df['code'] == '601933']['price']) <= 7.9:
        print(df[df['code'] == '601933'])
