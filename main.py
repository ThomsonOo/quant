# coding=utf8

from base.stock import getStocks
from tactics.positive import positiveFilter


if __name__ == "__main__":
    stocks = getStocks()
    stocks = positiveFilter(stocks)

    print "total stocks numbers is:%s" % len(stocks)

    for code, stock in stocks.iterrows():
        print code, stock['name'], stock['pe'], stock['timeToMarket']