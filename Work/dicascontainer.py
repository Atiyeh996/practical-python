import csv

def read_prices(filename):
    a = {}
    #with open(filename, 'rt') as f:
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            #row = line.split()
            try:
                #row = line.split(',')
                #a = [row[0] , row[1]]
                a[row[0]] = float(row[1])
                #print(a)
            except IndexError:
                #print("it is an empty line")
                pass
        print(a, end='')
    return (a)
read_prices('Data/prices.csv')

