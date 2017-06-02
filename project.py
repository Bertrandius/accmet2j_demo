'''
    This script picks a random movie from a user-specified list of movies.
'''
from random import shuffle

def input_list(n_items):
    '''This function asks for a given number of items and returns a list of these items. '''
    items = []
    for i in range(n_items):
        user_input = input("What is your %dst? " % (i + 1))
        items.append(user_input)
    return items

# Ask the user for a specified number of movies
n_movies = int(input("How many movies do you want to choose between? "))
movies = input_list(n_movies)
shuffle(movies)

# Print the first element of the shuffled list of movies
print(movies[0])
