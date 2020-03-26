# coding=utf8

'''
获取股票列表
'''
import tushare as ts
import baostock as bs
import os

from config import DEBUG_TOKEN
from utils.timeutil import getLastWeekDay
from config import DEBUG_STOCK_CACHE, DEBUG_CACHE_DIR
from utils.datautil import csv2DateFrame


# 获取所有A股列表
def getAStocks(day):
    fileName = str(day) + "-" + "stock.csv"
    filePath = DEBUG_CACHE_DIR + fileName

    if DEBUG_STOCK_CACHE and os.path.exists(filePath):
        stocks = csv2DateFrame(filePath)

    else:

        pro = ts.pro_api(DEBUG_TOKEN)

        stocks = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

        stocks['peTTM'] = ''
        stocks['pbMRQ'] = ''
        stocks['psTTM'] = ''
        stocks['pcfNcfTTM'] = ''

        lg = bs.login()

        for index, stock in stocks.iterrows():
            stock['peTTM'] = 0
            stock['pbMRQ'] = 0
            stock['psTTM'] = 0
            stock['pcfNcfTTM'] = 0

            if not lg.error_code == 0:  # 登录成功
                code = stock['symbol']
                area = "sz" if stock['ts_code'].find("SZ") > 0 else 'sh'
                code = area + "." + code

                print("query %s k data" % code)

                rs = bs.query_history_k_data_plus(code,
                                                  "peTTM,pbMRQ,psTTM,pcfNcfTTM",
                                                  start_date=str(day), end_date=str(day),
                                                  frequency="d", adjustflag="3")
                try:
                    if rs.error_code == '0':
                        data = rs.get_row_data()
                        stock['peTTM'] = data[0]
                        stock['pbMRQ'] = data[1]
                        stock['psTTM'] = data[2]
                        stock['pcfNcfTTM'] = data[3]
                except:
                    pass

        bs.logout()

    return stocks


if __name__ == "__main__":
    stocks = getAStocks(getLastWeekDay())

    print(stocks)
