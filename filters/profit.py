# coding:utf8

from base.report import getReport
from utils.timeutil import getCurrentYear, getCurrentQuarter

from base.stock import getAStocks


# 持续盈利过滤
def profitFilter(stocks, years):
    currentYear = getCurrentYear()
    currentQuarter = getCurrentQuarter()

    for i in range(0, years):
        year = currentYear - i

        quarters = 4 if year != currentYear else currentQuarter - 1  # 当年只查询到上一季度，往年查4个季度

        for j in range(0, quarters):
            quarter = j + 1

            if quarter <= 0:
                break

            print("query %s year %s quarter reports..." % (year, quarter))
            reports = getReport(year, quarter)

            for code, stock in stocks.iterrows():
                notReport = True  # 未发财报

                notProfit = False  # 未盈利

                for index, report in reports.iterrows():
                    if report['code'] == str(code):
                        notReport = False
                        if report['net_profits'] < 0:
                            notProfit = True
                        break

                if notReport:
                    print(stock['name'], "%s year %s quarter has not report" % (year, quarter))

                if notProfit:
                    print(stock['name'], "%s year %s quarter has not profit" % (year, quarter))
                    stocks.drop(code, inplace=True)

    return stocks


if __name__ == '__main__':
    stocks = getAStocks()

    profitFilter(stocks, 5)
