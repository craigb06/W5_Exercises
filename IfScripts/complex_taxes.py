# Define known values
pay_rate = 27.50
hours_worked = 45
filer = input('single or joint? ')
if hours_worked > 40:
    pay = 40 * pay_rate
    ot_pay = (hours_worked - 40) * (pay_rate * 1.5)
    gross_pay = (ot_pay + pay) * 52

# Calculate the unknown
if gross_pay < 12000 and filer == 'single':
    fed_tax = round((gross_pay * .05) / 52, 2)
elif gross_pay < 12000 and filer == 'joint':
    fed_tax = 0
elif gross_pay < 24999.99 and filer == 'single':
    fed_tax = round((gross_pay * .1) / 52, 2)
elif gross_pay < 24999.99 and filer == 'joint':
    fed_tax = round((gross_pay * .06) / 52, 2)
elif gross_pay < 74999.99 and filer == 'single':
    fed_tax = round((gross_pay * .15) / 52, 2)
elif gross_pay < 74999.99 and filer == 'joint':
    fed_tax = round((gross_pay * .11) / 52, 2)
else:
    fed_tax = round((gross_pay * .2) / 52, 2)

# Display the results
print(f'''
      You worked {hours_worked} hours this period
      Because you earn ${pay_rate} per hour, your gross weekly pay is ${pay + ot_pay}
      Your filing status is {filer}
      Your tax withholding for the week is ${fed_tax}
      Your net pay is {pay + ot_pay - fed_tax}
      ''')


# Same code copied with all values needing an input to test different values
# Define known values
pay_rate = float(input())
hours_worked = int(input())
filer = input('single or joint? ')
pay = round(40 * pay_rate, 2)
gross_pay = round(ot_pay + pay, 2) if hours_worked > 40 else round(hours_worked * pay_rate, 2)
ot_pay = round((hours_worked - 40) * (pay_rate * 1.5), 2)


# Calculate the unknown
if gross_pay < 12000 and filer == 'single':
    fed_tax = round((gross_pay * .05) / 52, 2)
elif gross_pay < 12000 and filer == 'joint':
    fed_tax = 0
elif gross_pay < 24999.99 and filer == 'single':
    fed_tax = round((gross_pay * .1) / 52, 2)
elif gross_pay < 24999.99 and filer == 'joint':
    fed_tax = round((gross_pay * .06) / 52, 2)
elif gross_pay < 74999.99 and filer == 'single':
    fed_tax = round((gross_pay * .15) / 52, 2)
elif gross_pay < 74999.99 and filer == 'joint':
    fed_tax = round((gross_pay * .11) / 52, 2)
else:
    fed_tax = round((gross_pay * .2) / 52, 2)

print(f'''
      You worked {hours_worked} hours this period
      Because you earn ${pay_rate} per hour, your gross weekly pay is ${gross_pay}
      Your filing status is {filer}
      Your tax withholding for the week is ${fed_tax}
      Your net pay is {gross_pay - fed_tax}
      ''')
