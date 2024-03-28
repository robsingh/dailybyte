"""
Working with APIs is very common these days and lucky for us they increasingly return JSON (over XML). 
We saved OMDb responses for some cool movies into a file that the tests load in.

Parse this data answering some questions:

get_movie_data consumes a list of movie json files (1 movie per file), 
returning a list of movie dicts, so for each movie you convert the json file to a dict.

now you have the data structure, loop through the movies and return the movie:
with Comedy in Genres (get_single_comedy)
that had the most nominations (get_movie_most_nominations)
having the longest runtime (get_movie_longest_runtime)
"""

import json

def get_movie_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
        movies = [json.loads(entry) for entry in data.strip().split('\n')]
    return movies

def get_single_comedy(movies):
    comedy_movies = [movie['Title'] for movie in movies if 'Comedy' in movie['Genre']]
    if comedy_movies:
        return comedy_movies[0]
    else:
        return None

def get_movie_most_nominations(movies):
    max_nominations = 0
    most_nominated_movie = None

    for movie in movies:
        nominations = movie['Awards'].split('&')[1].strip().split()[0] # nominations count
        nominations = int(nominations) if nominations.isdigit() else 0 # converting to int
        if nominations > max_nominations:
            max_nominations = nominations
            most_nominated_movie = movie['Title']
    
    return most_nominated_movie


def get_movie_longest_runtime(movies):
    max_runtime = 0
    longest_movie = None

    for movie in movies:
        runtime = int(movie['Runtime'].split()[0])
        if runtime > max_runtime:
            max_runtime = runtime
            longest_movie = movie['Title']

    return longest_movie

file_path = 'movies_data.txt'
movies = get_movie_data(file_path)

single_comedy = get_single_comedy(movies)
most_nominated_movie = get_movie_most_nominations(movies)
longest_movie = get_movie_longest_runtime(movies)

print("Single Comedy Movie:")
print(single_comedy)

print("\nMovie with most nominations:")
print(most_nominated_movie)

print("\nLongest Movie:")
print(longest_movie)
