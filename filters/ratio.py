# coding:utf8

from utils.timeutil import getCurrentYear, getCurrentQuarter
from base.balance import getBalanceData

from base.stock import getAStocks
from utils.timeutil import getLastWeekDay


# 流动比率过滤
def ratioFilter(stocks, ratioLimit):
    currentYear = getCurrentYear()
    currentQuarter = getCurrentQuarter()

    lastQuarter = currentQuarter - 1  # 最近上个季度盈利数据

    if lastQuarter <= 0:
        lastQuarter = 4
        currentYear = currentYear - 1

    print("use %s year %s quarter balance data" % (currentYear, lastQuarter))

    for index, stock in stocks.iterrows():
        code = stock['symbol']
        area = "sz" if stock['ts_code'].find("SZ") > 0 else 'sh'
        code = area + "." + code

        for quarter in range(lastQuarter, 0, -1):  # 最新盈利数据

            balance = getBalanceData(code, currentYear, quarter)

            if balance is not None:
                try:
                    ratio = float(balance['currentRatio'])
                except Exception:
                    ratio = 0  # 未找到对应数据
            else:
                ratio = 0

            if ratio != 0:
                break

        print("%s ratio is: %s" % (code, ratio))

        if ratio == 0:
            print("=======%s ratio data is lost========" % code)

        if ratio != 0 and ratio < ratioLimit:
            stocks.drop(index, inplace=True)

    return stocks


if __name__ == '__main__':
    stocks = getAStocks(getLastWeekDay())

    ratioFilter(stocks, 1.5)

    print(stocks)
