# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
#print("The total due is " + str(total_due))

# 2. Why is the str() function being used here?
# 2. The str() is being used here because 'total_due' is a float data type and string data types can only concatenate to other string data types

print('Food cost is ' + str(food_cost) + ' and tax is '+ str(tax))
#print('Tip is ' + str(tip))
print('Total due is ' + str(total_due))

# 5. Bonus Q  Note that you can’t simply copy and paste the above text into VSCode. Why is that?
# 5. When I copied and pasted I tried to run the statement anyways and got a syntax error for invalid character for the quotations marks, but when manually changing the quotations marks the statement ran with no error


print("Tip is " + format(tip, ".2f"))
