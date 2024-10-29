# Define the known values
pay_rate = 27.50
hours_worked = 45

# Calculate the unknown
if hours_worked > 40:
    pay = 40 * pay_rate
    ot_pay = (hours_worked - 40) * (pay_rate * 1.5)
    print(f'gross pay is {ot_pay + pay}')
else:
    print(f'gross pay is {pay_rate * hours_worked}')


# Different values
pay_rate = 15.35
hours_worked = 50

# Calculate the unknown
if hours_worked > 40:
    pay = 40 * pay_rate
    ot_pay = (hours_worked - 40) * (pay_rate * 1.5)
    print(f'gross pay is {ot_pay + pay}')
else:
    print(f'gross pay is {pay_rate * hours_worked}')


# Different values
pay_rate = 37.75
hours_worked = 40
if hours_worked > 40:
    pay = 40 * pay_rate
    ot_pay = (hours_worked - 40) * (pay_rate * 1.5)
    print(f'gross pay is {ot_pay + pay}')
else:
    print(f'gross pay is {pay_rate * hours_worked}')