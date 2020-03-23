#coding=utf8

from base.report import getReport
from utils.timeutil import getCurrentYear, getCurrentQuarter

if __name__ == "__main__":

    currentYear = getCurrentYear()
    currentQuarter = getCurrentQuarter()

    for i in range(0, 10):
        year = currentYear - i

        quarters = 4 if year != currentYear else currentQuarter - 1  # 当年只查询到上一季度，往年查4个季度

        for j in range(0, quarters):
            quarter = j + 1

            if quarter <= 0:
                break

            print "query %s year %s quarter reports..." % (year, quarter)
            reports = getReport(year, quarter)

            fileName = "%s_%s_profit_data.csv"%(year,quarter)

            print "save %s year %s quarter reports to: %s"%(year,quarter,fileName)

            reports.to_csv(fileName, encoding="gbk", index=False)

