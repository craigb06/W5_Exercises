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