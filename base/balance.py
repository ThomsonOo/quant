# coding:utf8

import baostock as bs
import pandas as pd

from utils.datautil import csv2DateFrame
from config import DEBUG_BALANCE_CACHE, DEBUG_CACHE_DIR


def getBalanceData(code, year, quarter):
    if DEBUG_BALANCE_CACHE:

        fileName = "%s_%s_balance_data.csv" % (year, quarter)

        filePath = DEBUG_CACHE_DIR + fileName

        print("read cache balance: ", filePath)

        result_balance = csv2DateFrame(filePath)

        try:
            result_balance.index = result_balance['code']
            result_balance = result_balance.loc[code]
        except:
            result_balance = None
    else:
        lg = bs.login()

        if lg.error_code == '0':

            balance_list = []
            rs_balance = bs.query_balance_data(code=code, year=year, quarter=quarter)

            while (rs_balance.error_code == '0') & rs_balance.next():
                balance_list.append(rs_balance.get_row_data())

            result_balance = pd.DataFrame(balance_list, columns=rs_balance.fields)

        bs.logout()

    return result_balance


if __name__ == "__main__":
    pass
