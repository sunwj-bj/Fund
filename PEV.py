# 第一个入参是内含价值，第二个入参是PEV,第三个是总股本
def get_price(ev, pev, count):
    price = ev * pev / count
    return price


# 根据估价计算PEV
def get_pev(price, count, ev):
    pev = price * count / ev
    return pev


# 获取年复合增长率
def get_cagr(start, end, years):
    return pow(end / start, 1 / years) - 1


# 用年复合增长率测算n年后利润
def get_final(start, years, cagr):
    return start * pow(1 + cagr, years)


# 计算市盈率
def get_pe(total, profit_this_year):
    return total / profit_this_year


if __name__ == "__main__":
    # 计算年复合增长率
    start = 4.28
    end = 13.79
    years = 5
    cagr = get_cagr(start, end, years)
    final_profit = get_final(13.79, 5, cagr)
    pe = get_pe(2873.11, final_profit)
    print("年复合增长率为：{}".format(cagr))
    print("根据当前年复合增长率测算的利润为：{}".format(final_profit))
    print("根据测算利润来计算当前市盈率为：{}".format(pe))

    # 中国平安总股本182.8亿
    pingan_stock_count = 18280000000
    # 估算2020年底平安寿险和健康险内含价值一万亿
    pingan_ev = 1000000000000
    # 当前最新报告中的平安内涵价值
    pingan_current_ev = 805374000000
    # 给予中国平安的PEV
    pingan_pev = 1.3
    pingan_current_price = 81.85
    # 估算股票合理价位
    print(get_price(pingan_ev, pingan_pev, pingan_stock_count))
    # 计算当前时刻PEV
    print(get_pev(pingan_current_price, pingan_stock_count, pingan_current_ev))
