# 第一个入参是内含价值，第二个入参是PEV,第三个是总股本
def get_price(ev, pev, count):
    price = ev * pev / count
    return price


# 根据估价计算PEV
def get_pev(price, count, ev):
    pev = price * count / ev
    return pev


if __name__ == "__main__":
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
