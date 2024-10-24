# Define known values
salary = 150000

# Calculate the unknown
taxes = (salary/12) * .23

# Display the results
print('Federal taxes withhold $' + format(taxes, '.2f') + ' every month')

# Another way to write this code would be

# Calculate the unknown
taxes2= (salary * .23)/12

# Display the results
print('Federal taxes withhold $' + format(taxes, '.2f') + ' every month')