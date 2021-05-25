# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
   portfolio = ()
   a =[]
   f = open(filename, 'rt')
   
   headers = next(f).split(',')
   for line in f:
       row = line.split(",")
       portfolio = (row[0], int(row[1]), float(row[2]))
       a.append(portfolio)


   print(a, end='')

   f.close()  
   
read_portfolio('Data/portfolio.csv')
