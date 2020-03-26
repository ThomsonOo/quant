# coding=utf8

'''
积极型策略：
    pe <= 9
    pb <=1.2
    创办时间>5年
    持续5年盈利
    去年利润大于5年前同期利润
    流动比率 >= 1.5
'''

from base.stock import getAStocks
from config import POSITIVE_PE_LIMIT, POSITIVE_FOUNDING_TIME_LIMIT, POSITIVE_PROFIT_YEAR_LIMIT, \
    POSITIVE_GROW_YEAR_LIMIT, POSITIVE_PB_LIMIT, POSITIVE_RATIO_LIMIT
from filters.founding_time import foundingTimeFilter
from filters.pe import peFilter
from filters.pb import pbFilter
from filters.profit import profitFilter
from filters.grow import growFilter
from filters.ratio import ratioFilter

from utils.timeutil import getLastWeekDay


def positiveFilter(stocks):
    stocks = peFilter(stocks, POSITIVE_PE_LIMIT)

    stocks = pbFilter(stocks, POSITIVE_PB_LIMIT)

    stocks = foundingTimeFilter(stocks, POSITIVE_FOUNDING_TIME_LIMIT)

    stocks = profitFilter(stocks, POSITIVE_PROFIT_YEAR_LIMIT)

    stocks = growFilter(stocks, POSITIVE_GROW_YEAR_LIMIT)

    stocks = ratioFilter(stocks, POSITIVE_RATIO_LIMIT)

    return stocks


if __name__ == "__main__":

    stocks = getAStocks(getLastWeekDay())

    stocks = positiveFilter(stocks)

    print("total stocks numbers is:%s" % len(stocks))

    for code, stock in stocks.iterrows():
        print(code, stock['name'], stock['peTTM'], stock['pbMRQ'], stock['list_date'])
