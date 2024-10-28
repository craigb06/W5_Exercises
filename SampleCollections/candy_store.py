# Define known values
candy = ('Starburst', 'Skittles', 'Gummies')
flavors = ('Strawberry', 'Watermelon', 'Green Apple')

# Calculate the unknown
candy_combos = {flavors[0] +' '+ candy[0],
                flavors[1] +' '+ candy[2],
                flavors[2] +' '+ candy[1]}

# Display the results
print('Today\'s candy options include ' + str(candy_combos))

# The order of the items change with each output