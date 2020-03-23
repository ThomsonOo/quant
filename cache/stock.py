from base.stock import getAStocks
from utils.timeutil import getLastWeekDay

if __name__ == '__main__':

    lastWeekDay = getLastWeekDay()

    fileName = str(lastWeekDay) + "-" + "stock.csv"

    print("getting %s stocks list"%lastWeekDay)

    stocks = getAStocks(lastWeekDay)

    print('saving %s stocks to: %s'%(lastWeekDay,fileName))
    stocks.to_csv(fileName,encoding='gbk', index=False)


