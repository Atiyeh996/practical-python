#exercise 2.5
import csv

def read_portfolio(filename):
   
   a =[]
   #f = open(filename, 'rt')
   with open(filename, 'rt') as f:
      #rows = csv.reader(f)
      headers = next(f).split(',')

      for line in f:
        row = line.split(',')
        portfolio = {"names" :row[0],"shares": int(row[1]), "price":float(row[2])}
        a.append(portfolio)
      #print(a, end='')
      print(a)
   return(a)

   #f.close()  
read_portfolio('Data/portfolio.csv')  
