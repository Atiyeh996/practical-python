
# report.py


import csv 

def read_portfolio(filename):
    a=[]
    with open(filename, 'rt') as f:
        #portfolio={}
        #a=[]
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio = {
                "name" : row[0],
                "shares" : int(row[1]),
                "price" : float(row[2])
            }
            a.append(portfolio)

        #print(a,"\n")
    return a
a = read_portfolio('Data/portfolio.csv')


def read_prices(filename):
    
    dict = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try: 
                #dict = print(row)
                dict[row[0]] = float(row[1])
            except IndexError:
                pass
    
    #print(dict,"\n")
    return dict


dict = read_prices('Data/prices.csv')


Cost = 0
for s in a:
    Cost += s["shares"]*s["price"]

print('cost', Cost)
'''
Value = 0.0
for s in a:
    Value += s["shares"]*dict[s["name"]]

print(Value)
print(Value - Cost)
'''
def make_report(a, dict):
    list=[]

    for portfolio in a:
        price = dict[portfolio['name']]
        change = price - portfolio['price']

    
    
    return list

report = make_report(a,dict)


headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
     

