# coding=utf8

'''
筛选符合市盈率条件的股票
'''

from base.stock import getAStocks
from utils.timeutil import getLastWeekDay


def peFilter(stocks, peLimit):
    for code, stock in stocks.iterrows():
        pe = float(stock['peTTM'])
        if pe <= 0 or pe > peLimit:
            stocks.drop(code, inplace=True)
    return stocks


if __name__ == "__main__":
    stocks = getAStocks(getLastWeekDay())
    stocks = peFilter(stocks, 9)

    print("low pe stocks total has: %s" % len(stocks))

    for code, stock in stocks.iterrows():
        print(code, stock['name'], stock['peTTM'])
