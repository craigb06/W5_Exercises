# Define known values
ship_info = {
'name': 'Craig Bowman',
'address': '2648 W 98th St',
'city': 'Chicago',
'state': 'Illinois',
'zip': 60805
}

# Print the address properly formatted for mailing
print(f'''{ship_info.get('name')}
{ship_info.get('address')}
{ship_info.get('city')}, {ship_info.get('state')}
{ship_info.get('zip')}''')

# Remove the key:value pair for name
ship_info.pop('name')
print(ship_info)

# Add a new variable for full_name
full_name = ('Craig', 'Bowman')
(first_name, last_name) = full_name

# Use the update() method to add one more key:value pair
ship_info.update({'full name':'Mr' +' '+ first_name +' ' + last_name})

print(f'''{ship_info.get('full name')}
{ship_info.get('address')}
{ship_info.get('city')}, {ship_info.get('state')}
{ship_info.get('zip')}''')