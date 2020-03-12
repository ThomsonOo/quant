# coding:utf8

from base.report import getReport
from utils.timeutil import getCurrentYear, getCurrentQuarter

from base.stock import getStocks


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

            print "query %s year %s quarter reports..." % (year, quarter)
            reports = getReport(year, quarter)
            for index, report in reports.iterrows():
                for code, stock in stocks.iterrows():
                    if report['code'] == str(code):
                        print stock['name'], "%s year %s quarter profit is %s" % (year, quarter, report['net_profits'])
                        if report['net_profits'] < 0:
                            stocks.drop(code, inplace=True)
                        break
    return stocks


if __name__ == '__main__':
    stocks = getStocks()

    profitFilter(stocks, 5)

    # reports = getReport(2019,4)

    # for index,report in reports.iterrows():
    # print index,report['code']
    # if report['code'] == '601229':
    #     print report

    pass
