# coding=utf8

'''
积极型策略：
    pe <= 9
    创办时间>5年
    持续5年盈利
'''

from base.stock import getAStocks
from config import POSITIVE_PE_LIMIT, POSITIVE_FOUNDING_TIME_LIMIT,POSITIVE_PROFIT_YEAR_LIMIT
from filters.founding_time import foundingTimeFilter
from filters.pe import peFilter
from filters.profit import profitFilter
from utils.timeutil import getLastWeekDay

def positiveFilter(stocks):

    stocks = peFilter(stocks, POSITIVE_PE_LIMIT)

    stocks = foundingTimeFilter(stocks, POSITIVE_FOUNDING_TIME_LIMIT)

    stocks = profitFilter(stocks,POSITIVE_PROFIT_YEAR_LIMIT)

    return stocks


if __name__ == "__main__":

    stocks = getAStocks('2020-03-23')

    stocks = positiveFilter(stocks)

    print("total stocks numbers is:%s" % len(stocks))

    for code, stock in stocks.iterrows():
        print(code, stock['name'], stock['peTTM'], stock['list_date'])
