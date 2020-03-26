# coding=utf8

from base.stock import getAStocks
from utils.timeutil import getLastWeekDay
from tactics.positive import positiveFilter

if __name__ == "__main__":
    stocks = getAStocks(getLastWeekDay())
    stocks = positiveFilter(stocks)

    print("total stocks numbers is:%s" % len(stocks))

    for code, stock in stocks.iterrows():
        print(code, stock['name'], stock['peTTM'], stock['pbMRQ'], stock['list_date'])
