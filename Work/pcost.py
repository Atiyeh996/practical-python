# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
Total_amount = 0

for line in f :
   row = line.split(',')
   Total_amount = Total_amount + float(row[2])  * int(row[1])
print("Total amount is", Total_amount)

f.close()