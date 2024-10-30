# Define known values
a = 10
b = 4
c = 32

# Calculate the unknown
print(min(a, b, c))
print(max(a, b, c))
 
# Display the results
if a > b and a > c:
    print(f'The max is {a}!')
elif b > a and b > c:
    print(f'The max is {b}!')
elif c > a and c > b:
    print(f'The max is {c}!')

if a < b and a < c:
    print(f'The min is {a}!')
elif b < a and b < c:
    print(f'The min is {b}!')
else:
    print(f'The min is {c}!')

# Testing the same code above with input values
# Define known values
a = int(input())
b = int(input())
c = int(input())

# Display the results
if a > b and a > c:
    print(f'The max is {a}!')
elif b > a and b > c:
    print(f'The max is {b}!')
elif c > a and c > b:
    print(f'The max is {c}!')

if a < b and a < c:
    print(f'The min is {a}!')
elif b < a and b < c:
    print(f'The min is {b}!')
else:
    print(f'The min is {c}!')
