# report.py
#
# Exercise 2.6

import csv 

def read_prices(filename):
    
    dic = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                dic[row[0]] = float(row[1])
            except IndexError:
                pass
    
    print(dic)
    return dic


read_prices('Data/prices.csv')
