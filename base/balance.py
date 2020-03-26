# coding:utf8

import baostock as bs
import pandas as pd


def getBalanceData(code, year, quarter):
    # lg = bs.login()

    # if lg.error_code == '0':

    balance_list = []
    rs_balance = bs.query_balance_data(code=code, year=year, quarter=quarter)
    while (rs_balance.error_code == '0') & rs_balance.next():
        balance_list.append(rs_balance.get_row_data())

    result_balance = pd.DataFrame(balance_list, columns=rs_balance.fields)

    # bs.logout()


    return result_balance

if __name__ == "__main__":
    pass
