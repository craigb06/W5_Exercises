# Define known values
radius = 4

# Calculate the unknown
import math
area = math.pi * (radius **2)

# Display the results
print('The area of a circle with radius ' + str(radius) + ' is ' + str(area) + ' inches')

# With rounding
print('The area of a circle with radius ' + str(radius) + ' is ' + str(round(area, 4)) + ' inches')