'''

In this Bite we are going to parse a csv movie dataset to identify the directors with the highest rated movies.

Write get_movies_by_director: use csv.DictReader to convert movie_metadata.csv into a (default)dict of lists of Movie namedtuples. 

Convert/filter the data:
Only extract director, title, year and rating, ignoring movies without all of these fields.
Type conversions: year -> int / rating -> float
Discard any movies older than 1960.
Here is an extract:

....
{ 'Woody Allen': [
    Movie(title='Midnight in Paris', year=2011, rating=7.7),
    Movie(title='The Curse of the Jade Scorpion', year=2001, rating=6.8),
    Movie(title='To Rome with Love', year=2012, rating=6.3),  ....
    ], ...
}
Write the calc_mean_score helper that takes a list of Movie namedtuples and calculates the mean rating,returning the score rounded to 1 decimal place.
Complete get_average_scores which takes the directors data structure returned by get_movies_by_director (see 1.) and returns a list of tuples (director, average_rating) ordered by highest score in descending order. Only take directors into account with >= MIN_MOVIES
'''
import csv
from collections import defaultdict, namedtuple

MIN_MOVIES = 1

Movie = namedtuple('Movie', 'title,year,rating')

def get_movies_by_director(csv_file):
    directors = defaultdict(list)
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                director = row['director_name']
                title = row['movie_title']
                year = int(row['title_year'])
                rating = float(row['imdb_score'])
                if year >= 1960:
                    directors[director].append(Movie(title, year, rating))
            except (ValueError, KeyError):
                continue
    return directors

def calc_mean_score(movies):
    if not movies:
        return 0.0
    total_score = sum(movie.rating for movie in movies)
    return round(total_score / len(movies), 1)


def get_average_scores(directors, min_movies=4):
    director_scores = []
    for director, movies in directors.items():
        if len(movies) >= min_movies:
            average_rating = calc_mean_score(movies)
            director_scores.append((director, average_rating))
    director_scores.sort(key=lambda x: x[1], reverse=True)
    return director_scores

directors = get_movies_by_director('movies_metadata.csv')
average_scores = get_average_scores(directors, MIN_MOVIES)
print(average_scores)




