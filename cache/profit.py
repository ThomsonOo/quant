# coding:utf8

from base.profit import getProfit
from utils.timeutil import getCurrentYear, getCurrentQuarter
from base.stock import getAStocks
from utils.timeutil import getLastWeekDay

import baostock as bs

if __name__ == "__main__":

    stocks = getAStocks(getLastWeekDay())

    currentYear = getCurrentYear()
    currentQuarter = getCurrentQuarter()
    lg = bs.login()

    for i in range(0, 10):
        year = currentYear - i

        quarters = 4 if year != currentYear else currentQuarter - 1  # 当年只查询到上一季度，往年查4个季度

        for j in range(0, int(quarters)):
            quarter = j + 1

            if quarter <= 0:
                break
            profits = None
            fileName = "%s_%s_profit_data.csv" % (year, quarter)

            for index, stock in stocks.iterrows():
                code = stock['symbol']
                area = "sz" if stock['ts_code'].find("SZ") > 0 else 'sh'
                code = area + "." + code

                print("query %s %s year %s quarter profit..." % (code, year, quarter))

                profit = getProfit(code, year, quarter)
                if profits is None:
                    profits = profit
                else:
                    profits = profits.append(profit)

            print("save %s year %s quarter profit to: %s" % (year, quarter, fileName))
            profits.to_csv(fileName, encoding="gbk", index=False)

    bs.logout()
