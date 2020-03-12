# coding=utf8

'''
获取股票列表
'''
import tushare as ts


# 获取所有A股列表
def getStocks():
    stocks = ts.get_stock_basics()
    return stocks

if __name__ == "__main__":

    stocks = getStocks()

    print "stocks total has: %s"%len(stocks)

    for code,stock in stocks.iterrows():
        print code,stock['name'],stock['pe']