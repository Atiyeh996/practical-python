# pcost.py
#
# Exercise 1.32

#Total_amount = 0
import csv
import sys

def portfolio_cost(filename):

   try:
      f = open(filename)
   except FileNotFoundError:
      print(f'{filename} is not a valid file')
      return

   Total_amount = 0

   f = open('Data/portfolio.csv', 'rt')
   headers = next(f).split(',')
   #Total_amount = 0

   for line in f :
      row = line.split(',')
      Total_amount = Total_amount + float(row[2])  * int(row[1])

   print("Total amount is", Total_amount)

   #return Total_amount


