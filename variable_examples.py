customerID = 5
# I assumed this type of value should be an integer based on the datasets I've seen thusfar

customer_first_name = 'Johnny'
# names are always strings type values

customer_middle_name = 'Jon'
# names are always strings type values

customer_last_name = 'James'
# names are always strings type values

gender = 'Male'
# gender is also a string type value

DOB = '10-15-1992'
# originally I entered the date as a number without quotations but best practice would be to always store dates as strings

DLnumber = 'D12345678'
# driver license number is stored as a string because of the possibility that the "number" would have a letter in it

auto_policy = 'A87654321'
# originally I created a fake number storing it as a string for the sames reason I stored the DL number as a string
# after collaborating with my peer Hassan, he came up with an idea to combine other sting values to create a unique auto policy number

auto_policy_number = (customer_middle_name + DOB + DLnumber)
# not everyone has a middle name but for the sake of this exercise this is the formmula I came with for auto policy number

print (auto_policy_number)

my_first_name = 'Craig'

my_middle_name = 'Anthony'

my_last_name = 'Bowman'

my_city = 'Chicago'

my_state = 'Illinois'

# Lab 2

# What is the full list of reserved words that can't be used for variable names?

''' False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global,
if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield'''



'''Pick 5 of these words and review the explanation for how it is used as a keyword in 
Python. Add these 5 definitions as comments to your exercise document. Put ^^
around any terms that you are not familiar with'''

# 1. ^raise^ - The raise statement is used to raise an error. These errors are visible in the traceback and they cancel the execution of the program if not handled properly.

# 2. ^elif^ - Shorthand for else if, checks if some other condition holds when the condition in the if statement is false

# 3. ^lambda^ - A lambda function in Python is an anonymous function. It can take any number of arguments but only have a single expression.

# 4. ^nonlocal^ - This keyword is used in functions inside functions to create anonymous functions.

# 5. ^global^ - Accessing a global variable is simple as any other variable but to modify a global variable, you need to use the global keyword.

    
