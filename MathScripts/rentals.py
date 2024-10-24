# Define known values
tourists = 38
van = 250
passengers = 15

# Calculate the unknown
# How many vans do you need?
import math
vans_needed = math.ceil(tourists/passengers)

# How much will it cost to rent vans?
vans_cost = format(vans_needed * van, '.2f')

# What is the cost if you split it per person?
cost_per_person = format(float(vans_cost)/tourists, '.2f')

# Display the results
print(vans_needed)
print(vans_cost)
print(cost_per_person)
print('With ' + str(tourists) + ' tourists we need ' + str(vans_needed) + ' vans which will cost a total of $' + vans_cost + ' which brings it to $' + cost_per_person + ' per person')

# How much money did your script say you had to charge per person?  $19.74

# If you multiply that out, how much did you collect?  $750.12

# How much were the vans?  $750

# Why do you have leftover money?  
# I have money leftover because I have to round up when doing the equation to make sure the expenses for the van are covered,
# the format() method automatically rounds up to a fixed decimal place.