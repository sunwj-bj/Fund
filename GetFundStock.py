# coding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import datetime
import requests
from lxml import etree

"""
chromedriver报错解决方案
https://blog.csdn.net/weixin_41990913/article/details/90936149
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


def get_code(url):
    html = requests.get(url, headers=headers)
    html.encoding = 'gbk'
    document = etree.HTML(html.text)

    info = document.xpath('// *[ @ id = "code_content"] / div / ul / li / div / a[1] /text()')
    i = 0
    for fund in info:
        str = fund.split('）')[0]
        code = str.split('（')[1]
        with open('fund_url.txt', 'a+') as u:
            fund_url = 'http://fundf10.eastmoney.com/ccmx_%s.html' % code
            u.write(fund_url + '\n')
        i = i + 1
    print('i:', i)


def get_code_list(fundlist):
    i = 0
    u = open('fund_url.txt', 'a+')
    u.seek(0)
    u.truncate()
    for code in fundlist:
            fund_url = 'http://fundf10.eastmoney.com/ccmx_%s.html' % code
            u.write(fund_url + '\n')


def get_info(url):
    print(url)
    opt = webdriver.ChromeOptions()
    opt.headless = True
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    day = datetime.date.today()
    today = '%s' % day

    with open('jijin1.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    time.sleep(1)
    file = open('jijin1.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(file, 'lxml')

    try:
        fund = soup.select('#bodydiv > div > div > div.basic-new > div.bs_jz > div.col-left > h4 > a')[0].get_text()
        scale = soup.select('#bodydiv > div > div.r_cont > div.basic-new > div.bs_gl > p > label > span')[2].get_text().strip().split()[0]
        table = soup.select('#cctable > div > div > table')
        trs = table[0].select('tbody > tr')
        for tr in trs:
            code = tr.select('td > a')[0].get_text()
            name = tr.select('td > a')[1].get_text()
            price = tr.select('td > span')[0].get_text()
            ratio = tr.select('td')[6].get_text()
            try:
                round(float(price), 2)
            except ValueError:
                price = 0
            num = tr.select('td.tor')[3].get_text()
            market = float(num.replace(',', '')) * float(price)

            data = {
                'code': code,
                'fund': fund.split(' (')[0],
                'scale': scale,
                'name': name,
                'ratio':ratio,
                #'price': round(float(price), 2),
                #持股数(万股)
                'num': round(float(num.replace(',', '')), 2),
                #'market_value': round(market, 2),
                #'fund_url': url
            }
            print(data)
    except IndexError:
        info = {
            'url': url
        }
        print("获取数据错误！URL:"+info)


"""
获取基金的最新持仓情况
"""
if __name__ == "__main__":
    #url = 'http://fund.eastmoney.com/allfund.html'
    #get_code(url)
    fund_list = ['003096','161005']
    get_code_list(fund_list)
    with open('fund_url.txt', 'r') as f:
        i = 0
        for url in f.readlines():
            get_info(url)
            time.sleep(random.randint(0, 2))
            i = i + 1
        print('run times:', i)