# coding:utf8

import baostock as bs
import pandas as pd



def getProfit(code,year,quarter):

    lg = bs.login()

    # 查询季频估值指标盈利能力
    profit_list = []
    index = []

    rs_profit = bs.query_profit_data(code=code, year=year, quarter=quarter)

    while (rs_profit.error_code == '0') & rs_profit.next():
        profit = rs_profit.get_row_data()
        profit_list.append(profit)
        index.append(profit[0])

    result_profit = pd.DataFrame(profit_list, columns=rs_profit.fields,index=index)

    bs.logout()

    return result_profit




if __name__ == "__main__":

    profit = getProfit('sh.600000',2019,3)
    print(profit)

    pass