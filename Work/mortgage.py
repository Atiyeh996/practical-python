#exercise 1.9
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
#extra_payment_duration = 11


while principal > 0:

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    months = months +1

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print(f'Total paid ${total_paid:.2f}')
print('Total months', months)        
