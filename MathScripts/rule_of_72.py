# Define known values
savings = 300000
return_rate = 15

# Calculate unknown values
years_to_double = 72/return_rate
savings_double = savings * 2

# Display the results
print('At a ' + str(return_rate) + '% ' + 'interest rate, your savings account will be worth ' + format(savings_double, '.2f') + ' in ' + format(years_to_double, '.1f') + ' years')