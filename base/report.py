# coding:utf8

import tushare


from config import DEBUG_REPORT_CACHE,DEBUG_CACHE_DIR
from utils.datautil import csv2DateFrame


def getReport(year, quarter):
    if DEBUG_REPORT_CACHE:

        fileName = "%s_%s_profit_data.csv" % (year, quarter)

        filePath = DEBUG_CACHE_DIR + fileName

        print("read cache report: ",filePath)

        reports = csv2DateFrame(filePath)

    else:
        reports = tushare.get_report_data(year, quarter)

    return reports
