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


# 股票和指数的涨跌幅都是以昨日收盘价为基础，和当天开盘价无关
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

    '''
    农业银行 买入成本3.195  股息率5.6%左右(分红金额按照20年计算，成本按照买入成本计算)
    格力电器 安全市盈率在10左右
    海尔智家 安全市盈率在10左右 私有化之后的净利润率还有待观察
    '''

    stock_list = ['sh', 'sz', 'cyb', '601288', '000651', '600690', '601318', '512800', '159920', '513050', '600036',
                  '600048', '600900', '002044', '000538']
    df = ts.get_realtime_quotes(stock_list)
    e = df[['name', 'open', 'price', 'amount', 'pre_close']]
    # 对amount进行转换，单位为亿
    e['amount'] = format_amount(e['amount'])
    # 计算涨跌幅
    e['ratio'] = format_ratio(e['price'], e['pre_close'])
    print(e)
