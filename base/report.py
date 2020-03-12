# coding:utf8

import tushare


def getReport(year, quarter):
    reports = tushare.get_report_data(year, quarter)

    return reports
