# report.py
#
# Exercise 2.6

import csv 

dic = {}
a=[]
def read_portfolio(filename):

    with open(filename, 'rt') as f:
        portfolio={}
        a=[]
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio = {
                "name" : row[0],
                "shares" : int(row[1]),
                "price" : float(row[2])
            }
            a.append(portfolio)
        print(a,"\n")
        return a
a = read_portfolio('Data/portfolio.csv')



def read_prices(filename):
    
    dic = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                
                
                dict= print(row)
                #dic[row[0]] = float(row[1])
            except IndexError:
                pass
    
    #print(dic,"\n")
    #return dic


dict = read_prices('Data/prices.csv')

cost = 0
for d in a :
    cost += d["shares"]*d["price"]

print('Total cost', cost)

value = 0
for d in dict :
    value += d['shares']*dict[d['name']]
    #value += d['shares']
    #value += int(s[1])*dict[s[0]]


print("total_value" , value)
print('Gain=', value - cost )

