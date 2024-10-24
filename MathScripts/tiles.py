# Define known values
room_length = 15
room_width = 20

# Calculate the unknown
import math
tiles_needed = room_length * room_width
boxes_needed = math.ceil(tiles_needed/12)
extra_tiles = math.ceil(tiles_needed * .10)
total_tiles = tiles_needed + extra_tiles
total_boxes = math.ceil(total_tiles/12)

# Display the results
print(tiles_needed)
print(boxes_needed)
print(extra_tiles)
print(total_tiles)
print('To tile a room with dimensions of ' + str(room_length) + ' by ' + str(room_width) + ' feet I need a total of ' + str(total_boxes) + ' boxes')