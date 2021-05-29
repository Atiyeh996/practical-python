
# report.py


import csv 


a=[]
dict = {}
def read_portfolio(filename):

    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio = {
                "name" : row[0],
                "shares" : int(row[1]),
                "price" : float(row[2])
            }
            a.append(portfolio)

        
    return a


def read_prices(filename):
    
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try: 
                #dict = print(row)
                dict[row[0]] = float(row[1])
            except IndexError:
                pass
    
    
    return dict


def make_report(filename):
    list=[]

    for portfolio in a :
        current_price = a[portfolio['name']]
        change = current_price - portfolio['price']

        price = dict[portfolio['name']]
        change = price - portfolio['price']
        summary = (portfolio['name'], portfolio['shares'], current_price, change)
        list.append(summary)
    return list



def print_report(x,y):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in print_report:
        print('%10s %10d %10.2f %10.2f' % row)


def portfolio_report(portfolio_filename, prices_filename):


    a = read_portfolio('Data/portfolio.csv')
    dict = read_prices('Data/prices.csv')
    report = make_report(a,dict)
    print_report(report)

portfolio_report(portfolio_filename ='Data/portfolio.csv',prices_filename = 'Data/prices.csv')


