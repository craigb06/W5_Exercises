# Define known values
fave_movies = ['Friday Night Lights', 'Any Given Sunday', 'Remember The Titans', 'Your Name', 'The Notebook']

# Calculate the unknown
fav_movie_len = len(fave_movies)

# Display the results
print('The list fave_movies includes my top ' + str(fav_movie_len) + ' favorite movies')
# or
print('The list fave_movies includes my top ' + str((len(fave_movies))) + ' favorite movies')

print('The list ' + str(fave_movies) + ' includes my top ' + str((len(fave_movies))) + ' favorite movies')


# 4. Print a sorted list two ways
print(sorted(fave_movies))
print(fave_movies)


fave_movies.sort()
print(fave_movies)
# The .sort function sorts the list in alphabetical order 
# while the print(sorted()) function only displays an output of the sorted list but doesn't sort the list stored in the data


fave_movies.append('Insidious')
print(fave_movies)


print('The list fave_movies includes my top ' + str((len(fave_movies))) + ' favorite movies')
print('The list ' + str(fave_movies) + ' includes my top ' + str((len(fave_movies))) + ' favorite movies') 