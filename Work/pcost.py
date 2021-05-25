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
            
            print('Missing field encountered, skipping the corresponding line')

   return all_shares_price

if len(sys.argv) ==2:
   filename = sys.argv[1]
else:
   filename = 'Data/portfolio.csv'
Cost = portfolio_cost(filename)
print("total cost:" , Cost)

