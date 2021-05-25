# pcost.py
#
# Exercise 1.32

#Total_amount = 0
import csv
import sys

def portfolio_cost(filename):
   line_num = 0
   all_shares_price = 0

   with open(filename, 'rt') as f:
      lines = csv.reader(f)

      for line in lines:
         line_num +=1
         #skip header
         if line_num ==1:
            continue

         stock_name, shares_num, stock_price = line
         try:
            all_shares_price +=int(shares_num) * float(stock_price)
         except ValueError:
            "we can raise a warning instead using raise warning[msg]"
            print('Missing field encountered, skipping the corresponding line')

   return all_shares_price

if len(sys.argv) ==2:
   filename = sys.argv[1]
else:
   filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print("total cost:" , cost)

'''
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

'''
