# coding:utf8

from utils.timeutil import getCurrentYear, getCurrentQuarter

from base.stock import getAStocks
from base.profit import getProfit
from utils.timeutil import getLastWeekDay


# 持续盈利过滤
def profitFilter(stocks, years):
    currentYear = getCurrentYear()
    currentQuarter = getCurrentQuarter()

    loss = dict()

    for i in range(0, years):
        year = currentYear - i

        quarters = 4 if year != currentYear else currentQuarter - 1  # 当年只查询到上一季度，往年查4个季度

        for j in range(0, int(quarters)):
            quarter = j + 1

            if quarter <= 0:
                break

            for index, stock in stocks.iterrows():

                print("query %s year %s quarter profit..." % (year, quarter))

                code = stock['symbol']
                area = "sz" if stock['ts_code'].find("SZ") > 0 else 'sh'
                code = area + "." + code

                profit = getProfit(code, year, quarter)

                if profit is not None:
                    try:
                        netProfit = float(profit['netProfit'])
                    except Exception:
                        netProfit = 0  # 未找到对应数据
                else:
                    netProfit = 0


                if netProfit == 0:
                    print("=======loss %s profit========"%code)
                    try:
                        loss[code] = loss[code] + 1
                    except:
                        loss[code] = 1


                if netProfit < 0:
                    print(stock['name'], "%s year %s quarter net profit < 0" % (year, quarter))
                    stocks.drop(index, inplace=True)

            print(loss)
    return stocks


if __name__ == '__main__':
    stocks = getAStocks(getLastWeekDay())

    profitFilter(stocks, 5)
