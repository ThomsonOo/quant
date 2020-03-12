# coding=utf8

'''
积极型策略：
    pe <= 9
    创办时间5年内
'''

from base.stock import getStocks
from config import POSITIVE_PE_LIMIT, POSITIVE_FOUNDING_TIME_LIMIT,POSITIVE_PROFIT_YEAR_LIMIT
from filters.founding_time import foundingTimeFilter
from filters.pe import peFilter
from filters.profit import profitFilter

def positiveFilter(stocks):
    stocks = peFilter(stocks, POSITIVE_PE_LIMIT)

    stocks = foundingTimeFilter(stocks, POSITIVE_FOUNDING_TIME_LIMIT)

    stocks = profitFilter(stocks,POSITIVE_PROFIT_YEAR_LIMIT)

    return stocks


if __name__ == "__main__":

    stocks = getStocks()

    stocks = positiveFilter(stocks)

    print "total stocks numbers is:%s" % len(stocks)

    for code, stock in stocks.iterrows():
        print code, stock['name'], stock['pe'], stock['timeToMarket']
