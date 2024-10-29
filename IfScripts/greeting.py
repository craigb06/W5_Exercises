# Define known values
from datetime import datetime

# Calculate the unknown
now = datetime.now()
current_time = now.strftime("%H:%M")
print(current_time)

# Display the results
if current_time <'10:00':
    print('Good morning!')
elif current_time < '17:00':
    print('Good day!')
elif current_time >= '17:00':
    print('Good evening!')

# Updated script with additional condition

current_time = '02:00'

if current_time >='23:00' or current_time < '04:00':
    print('What are you doing up so late?')
elif current_time <'10:00':
    print('Good morning!')
elif current_time < '17:00':
    print('Good day!')
elif current_time >= '17:00':
    print('Good evening!')
