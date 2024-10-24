# Define known values
x1 = 3
y1 = 6
x2 = 4
y2 = 8

# Calculate the unknown
import math
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the results
print(distance)

# Alternatively I could also use this code

# Calculate the unknown
import math
distance2 = math.hypot(x2 - x1, y2 - y1)

# Display the results
print(distance2)