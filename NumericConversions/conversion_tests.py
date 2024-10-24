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
b1 = int(b)
#int(c)     -- invalid literal for int() with base 10: '402 Stevens
#int(d)     -- invalid literal for int() with base 10: 'Number 5 

a1 = float(a)
b2 = float(b)
#float(c)   -- could not convert string to float: '402 Stevens
#float(d)   -- could not convert string to float: 'Number 5

a2 = int(float(a))

c2 = int(c[0:3])
d2 = int(d[-2])

a3 = a.strip()
d3 = d.strip()

#Display the results

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(a1, type(a1))
print(a2, type(a2))
print(b1, type(b1))
print(b2, type(b2))
print(c2, type(c2))
print(d2, type(d2))
print(a3, type(a3))
print(d3, type(d3))
