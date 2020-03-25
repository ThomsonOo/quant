# coding:utf8

from utils.timeutil import getCurrentYear, getCurrentQuarter
from base.profit import getProfit
from base.stock import getAStocks

# 盈利在增长
def growFilter(stocks,years):
    currentYear = getCurrentYear()
    currentQuarter = getCurrentQuarter()

    lastQuarter = currentQuarter - 1 # 最近上个季度盈利数据

    if lastQuarter <= 0:
        lastQuarter = 4
        currentYear = currentYear -1

    print("use %s year %s quarter profit data"%(currentYear,lastQuarter))

    for index,stock in stocks.iterrows():
        code = stock['symbol']
        area = "sz" if stock['ts_code'].find("SZ") > 0 else 'sh'
        code = area + "." + code

        currentProfit = 0
        oldProfit = 0

        for quarter in range(lastQuarter,0,-1): # 最新盈利数据

            print("query %s %s year %s quarter profit:"%(code,currentYear,quarter))
            profit = getProfit(code, currentYear, quarter)

            if profit is not None:
                try:
                    currentProfit = float(profit['netProfit'])
                except Exception:
                    currentProfit = 0  # 未找到对应数据
            else:
                currentProfit = 0

            if currentProfit != 0:
                break



        for quarter in range(lastQuarter, 0,-1):  # 往期盈利数据

            print("query %s %s year %s quarter profit:" % (code, currentYear - years, quarter))
            profit = getProfit(code, currentYear - years, quarter)

            if profit is not None:
                try:
                    oldProfit = float(profit['netProfit'])
                except Exception:
                    oldProfit = 0  # 未找到对应数据
            else:
                oldProfit = 0

            if oldProfit != 0:
                break


        print("%s current profit is: %s,old profit is: %s"%(code,currentProfit,oldProfit))

        if currentProfit <= oldProfit:
            stocks.drop(index, inplace=True)

    return stocks


if __name__ == "__main__":
    stocks = getAStocks('2020-03-23')

    growFilter(stocks,5)
    pass