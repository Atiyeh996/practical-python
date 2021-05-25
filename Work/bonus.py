#exercise 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment = 1000.0
end_duration = 310

while principal > 0:
    months = months +1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if months == 1 + end_duration:
       principal = principal - extra_payment

       total_paid = total_paid + extra_payment 
print(total_paid)

#print('Total paid', round(total_paid, 2))
