# exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment = 1000.0
extra_payment_duration =11



while principal > 0:
    if months <= extra_payment_duration:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    months = months + 1

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment


print(f'Total paid &{total_paid:.2f}')
print (months)
#print('Months', months)

