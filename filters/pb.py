# coding:utf8


def pbFilter(stocks, pbLimit):
    for code, stock in stocks.iterrows():
        pe = float(stock['pbMRQ'])
        if pe <= 0 or pe > pbLimit:
            stocks.drop(code, inplace=True)
    return stocks



if __name__ == "__main__":
    pass