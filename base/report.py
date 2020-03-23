# coding:utf8

import tushare
import csv
import pandas

from config import DEBUG_REPORT_CACHE,DEBUG_CACHE_DIR



def csv2DateFrame(filePath):
    data = []

    with open(filePath, 'r') as fin:
        reader = csv.reader(fin)
        for row in reader:
            data.append(row)

    df = pandas.DataFrame(data[1:], columns=data[0])

    return df


def getReport(year, quarter):
    if DEBUG_REPORT_CACHE:

        fileName = "%s_%s_profit_data.csv" % (year, quarter)

        filePath = DEBUG_CACHE_DIR + fileName

        print "read cache report: ",filePath

        reports = csv2DateFrame(filePath)

    else:
        reports = tushare.get_report_data(year, quarter)

    return reports
