# coding=utf8

'''
筛选符合市盈率条件的股票
'''

from base.stock import getStocks


def peFilter(stocks, peLimit):
    for code, stock in stocks.iterrows():
        if stock['pe'] <= 0 or stock['pe'] > peLimit:
            stocks.drop(code, inplace=True)
    return stocks


if __name__ == "__main__":
    stocks = getStocks()
    stocks = peFilter(stocks, 9)

    print "low pe stocks total has: %s" % len(stocks)

    for code, stock in stocks.iterrows():
        print code, stock['name'], stock['pe']
