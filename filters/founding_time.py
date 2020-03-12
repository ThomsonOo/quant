# coding:utf8

from utils.timeutil import date2Timestamp,getTimeStamp,years2Timestamp

FOUNDING_TIME_FORMAT = "%Y%m%d"

def foundingTimeFilter(stocks, timeLimit):
    for code, stock in stocks.iterrows():
        if stock['timeToMarket'] <= 0:
            stocks.drop(code, inplace=True)
            continue
        foundingTime = stock['timeToMarket']
        foundingTime = date2Timestamp(foundingTime,FOUNDING_TIME_FORMAT)

        timeLimit = years2Timestamp(timeLimit)

        if foundingTime + timeLimit < getTimeStamp():
            stocks.drop(code, inplace=True)

    return stocks