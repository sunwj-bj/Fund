"""
get_today_all返回值说明：
code：代码
name:名称
changepercent:涨跌幅
trade:现价
open:开盘价
high:最高价
low:最低价
settlement:昨日收盘价
volume:成交量
turnoverratio:换手率
amount:成交金额
per:市盈率
pb:市净率
mktcap:总市值
nmc:流通市值
"""
import os
import tushare as ts
import baostock as bs
import time
import pickle
from pandas import Series
import pandas as pd

# data = ts.get_today_all()
# data['code'].astype('str')
# data.to_csv("full_stock_data.csv", encoding="gbk", index=False)
raw_data = pd.read_csv("full_stock_data.csv", encoding="gbk", converters={'code': str, 'mktcap': float, 'per': float})

# 市盈率30以下，盘子规模300亿以上
final_data = raw_data.loc[raw_data["per"] <= 30].loc[raw_data["mktcap"] >= 3000000].loc[raw_data["per"] > 0]
final_data[final_data['name'].astype(str).str.find("银行") < 0].to_csv("final_data.csv", encoding="gbk", index=False)
