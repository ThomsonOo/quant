# coding:utf8

from utils.timeutil import date2Timestamp,getTimeStamp,years2Timestamp

FOUNDING_TIME_FORMAT = "%Y%m%d"

def foundingTimeFilter(stocks, timeLimit):
    timeLimit = years2Timestamp(timeLimit)

    for code, stock in stocks.iterrows():
        foundingTime = int(stock['list_date'])

        if foundingTime <= 0:
            stocks.drop(code, inplace=True)
            continue

        foundingTime = date2Timestamp(foundingTime,FOUNDING_TIME_FORMAT)

        if foundingTime + timeLimit >= getTimeStamp():
            stocks.drop(code, inplace=True)

    return stocks