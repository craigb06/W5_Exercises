# Define known values
home = 1000000
car1 = 20000
car2 = 50000
stocks = 1000000
student_loan = 150000
mortgage = 4500 * 12 * 30

# Calculate the unknown
assets = home + car1 + car2 + stocks
debts = student_loan + mortgage
net_worth = assets - debts

# Display the results
print(assets)
print(debts)
print('Your net worth is ' + str(net_worth))