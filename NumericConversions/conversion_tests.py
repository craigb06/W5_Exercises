# Description: This script tests various numeric 
#              conversion techniques 
# Author: Craig B. Newprogrammer

# Define known values

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Calculate the unknown

#int(a)     -- invalid literal for int() with base 10: ' 101.1 
int(b)
#int(c)     -- invalid literal for int() with base 10: '402 Stevens
#int(d)     -- invalid literal for int() with base 10: 'Number 5 

float(a)
float(b)
#float(c)   -- could not convert string to float: '402 Stevens
#float(d)   -- could not convert string to float: 'Number 5

int(float(a))

c2 = int(c[0:3])
d2 = int(d[-2])

a2 = a.strip()
d3 = d.strip()

#Display the results

print(a, float(a))
print(a, int(float(a)))
print(b, int(b))
print(b, float(b))
print(c2, int(c2))
print(d2, int(d2))
print(a2, float(a2))
print(d3, str(d3))
