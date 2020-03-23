#coding=utf8

import csv
import pandas

def csv2DateFrame(filePath):
    data = []

    with open(filePath, 'r',encoding='gbk') as fin:
        reader = csv.reader(fin)
        for row in reader:
            data.append(row)

    df = pandas.DataFrame(data[1:], columns=data[0])

    return df