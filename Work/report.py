# report.py
#import csv

import fileparse

def read_portfolio(filename):
    
    #portfolio = []
    #with open(filename) as f:
     #   rows = csv.reader(f)
      #  headers = next(rows)
      #  for row in rows:
       #     record = dict(zip(headers, row))
        #    stock = {
        #        'name' : record['name'],
        #        'shares' : int(record['shares']),
        #        'price' : float(record['price'])
        #    }
        
        #    portfolio.append(stock)

   # return portfolio
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float], has_header=True)


def read_prices(filename):
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices
'''
    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

def make_report_data(portfolio,prices):
    
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata):
    
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfoliofile,pricefile):        
   

    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    
    report = make_report_data(portfolio,prices)

    
    print_report(report)

portfolio_report('Data/portfolio.csv','Data/prices.csv')
