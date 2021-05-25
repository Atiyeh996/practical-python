import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
headers
['name', 'shares', 'price']
for row in rows:
    print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
f.close()