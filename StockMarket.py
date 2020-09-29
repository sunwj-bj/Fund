import os
import tushare as ts
import baostock as bs
import time
from pandas import Series
import warnings

# 忽略警告
warnings.filterwarnings("ignore")


# 获取当前时间并格式化
# now = time.strftime("%Y-%m-%d", time.localtime())


def format_amount(amount):
    tmp_list = []
    for i, v in amount.items():
        tmp_list.append(str(round(float(v) / 100000000, 2)) + "亿")
    return Series(tmp_list)


def format_ratio(price, pre_close):
    tmp_price = []
    tmp_open = []
    final_list = []
    for i, v in price.items():
        tmp_price.append(v)
    for i, v in pre_close.items():
        tmp_open.append(v)
    for index in range(len(tmp_price)):
        final_list.append(
            str(round(((float(tmp_price[index]) - float(tmp_open[index])) / float(tmp_open[index])) * 100, 2)) + "%")
    return Series(final_list)


if __name__ == "__main__":
    # 6位数字股票代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
    # 可输入的类型：str、list、set或者pandas的Series对象
    stock_list = ['sh', 'sz', 'cyb']
    df = ts.get_realtime_quotes(stock_list)
    e = df[['name', 'open', 'price', 'amount', 'pre_close']]
    e['turn_volume'] = format_amount(e['amount'])
    e['ratio'] = format_ratio(e['price'], e['pre_close'])
    print(e)
