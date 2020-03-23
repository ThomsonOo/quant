# coding=utf8

import time
import datetime

def date2Timestamp(date, f):
    date = time.strptime(str(date), f)
    timestamp = int(time.mktime(date))

    return timestamp


def getTimeStamp():
    now = int(time.time())
    return now


def years2Timestamp(years):
    times = years * 365 * 24 * 60 * 60
    return times


def getCurrentYear():
    return datetime.datetime.now().year


def getCurrentQuarter():
    now = datetime.datetime.now()
    quarter = now.month / 3 if now.month % 3 == 0 else now.month / 3 + 1
    return quarter

def getLastWeekDay():
    now = datetime.date.today()

    if now.isoweekday() == 1:
        dayStep = 3
    else:
        dayStep = 1

    lastWeekDay = now - datetime.timedelta(days=dayStep)

    return lastWeekDay
