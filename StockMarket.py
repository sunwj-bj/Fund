import os
import tushare as ts
import baostock as bs
import time


#获取当前时间并格式化
#now = time.strftime("%Y-%m-%d", time.localtime())

#6位数字股票代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板），可输入的类型：str、list、set或者pandas的Series对象
while 1 == 1:
    time.sleep(3)
    stock_list = ['sh','sz','cyb']
    df = ts.get_realtime_quotes(stock_list)
    e = df[['code','name','open','price','amount','time']]
    print(e)


