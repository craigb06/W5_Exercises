# Define known values
ship_info = {
'name': 'Craig Bowman',
'address': '2648 W 98th St',
'city': 'Chicago',
'state': 'Illinois',
'zip': 60805
}

# Print the address properly formatted for mailing
print(ship_info.get('name') +
      ship_info.get('address') +
      ship_info.get('city') +
      ship_info.get('state'[0:2]) +
      ship_info.get(str('zip')
      ))