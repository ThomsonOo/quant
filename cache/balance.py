# coding:utf8

from base.balance import getBalanceData
from utils.timeutil import getCurrentYear, getCurrentQuarter
from base.stock import getAStocks
from utils.timeutil import getLastWeekDay


import baostock as bs

if __name__ == "__main__":

    stocks = getAStocks(getLastWeekDay())

    currentYear = getCurrentYear()
    currentQuarter = getCurrentQuarter()
    lg = bs.login()

    for i in range(0, 2):
        year = currentYear - i

        quarters = 4 if year != currentYear else currentQuarter - 1  # 当年只查询到上一季度，往年查4个季度

        for j in range(0, int(quarters)):
            quarter = j + 1

            if quarter <= 0:
                break
            balances = None
            fileName = "%s_%s_balance_data.csv" % (year, quarter)

            for index, stock in stocks.iterrows():
                code = stock['symbol']
                area = "sz" if stock['ts_code'].find("SZ") > 0 else 'sh'
                code = area + "." + code

                print("query %s %s year %s quarter balance data..." % (code, year, quarter))

                balance = getBalanceData(code, year, quarter)
                if balances is None:
                    balances = balance
                else:
                    balances = balances.append(balance)

            print("save %s year %s quarter balance data to: %s" % (year, quarter, fileName))
            balances.to_csv(fileName, encoding="gbk", index=False)

    bs.logout()
