# exercise 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment = 1000.0

while principal > 0:
    months = months +1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if months < 359:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    #print(months, round(total_paid,2), round(principal, 2))
    
print(f'Total paid $ {total_paid:.2f}')


