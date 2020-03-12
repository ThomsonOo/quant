# coding=utf8

import time
import datetime


def date2Timestamp(date, format):
    date = time.strptime(str(date), format)
    timestamp = int(time.mktime(date))

    return timestamp


def getTimeStamp():
    now = int(time.time())
    return now


def years2Timestamp(years):
    times = years * 365 * 24 * 60 * 60 * 1000
    return times


def getCurrentYear():
    return datetime.datetime.now().year


def getCurrentQuarter():
    now = datetime.datetime.now()
    quarter = now.month / 3 if now.month % 3 == 0 else now.month / 3 + 1
    return quarter
