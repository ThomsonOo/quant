# coding:utf8

import baostock as bs
import pandas as pd

from config import DEBUG_PROFIT_CACHE, DEBUG_CACHE_DIR
from utils.datautil import csv2DateFrame


def getProfit(code, year, quarter):

    if DEBUG_PROFIT_CACHE:

        fileName = "%s_%s_profit_data.csv" % (year, quarter)

        filePath = DEBUG_CACHE_DIR + fileName

        print("read cache profit: ", filePath)

        result_profit = csv2DateFrame(filePath)

        try:
            result_profit.index = result_profit['code']
            result_profit = result_profit.loc[code]
        except:
            result_profit = None

    else:

        lg = bs.login()

        if lg.error_code == '0':
            # 查询季频估值指标盈利能力
            profit_list = []

            rs_profit = bs.query_profit_data(code=code, year=year, quarter=quarter)

            while (rs_profit.error_code == '0') & rs_profit.next():
                profit_list.append(rs_profit.get_row_data())

            result_profit = pd.DataFrame(profit_list, columns=rs_profit.fields).loc[0]

        bs.logout()

    return result_profit


if __name__ == "__main__":
    profit = getProfit('sh.600000', 2019, 3)
    print(profit['netProfit'])

    pass
