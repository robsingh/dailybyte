"""
In this Bite you will use ElementTree to parse some Nolan movies we extracted from OMDb (https://www.omdbapi.com/).

Luckily most APIs switched to JSON, but sometimes XML is all there is, so at least learn to parse some! 
Complete the get_tree, get_movies and get_movie_longest_runtime functions below.

Have fun and remember:

Keep calm and code in Python!
"""

import requests
import xml.etree.ElementTree as ET

API_URL = "http://www.omdbapi.com/"

def get_movies(*titles):
    movies = []

    for title in titles:
        params = {
            "t": title,
            "apikey": "enter your API key"
        }

        response = requests.get(API_URL, params=params)

        try:
            tree = ET.ElementTree(ET.fromstring(response.text))
            movies.append(tree)
        except ET.ParseError as e:
            print(f"Error parsing XML for '{title}' : {e}")
    return movies


def get_movies_longest_runtime(*titles):
    movies = get_movies(*titles)
    longest_runtime = 0
    longest_runtime_movie = None

    for movie_tree in movies:
        root = movie_tree.getroot()
        runtime = root.findtext("Runtime")

        if runtime:
            runtime_minutes = int(runtime.split()[0])

            if runtime_minutes > longest_runtime:
                longest_runtime = runtime_minutes
                longest_runtime_movie = root.findtext("Title")
    return longest_runtime_movie

# if we have JSON format, not XML.

# import requests
# import json
# def get_movies(*titles):
#     movies = []

#     for title in titles:
#         params = {
#             "t": title,
#             "apikey": "API key"  # Replace with your actual OMDB API key
#         }
        
#         response = requests.get(API_URL, params=params)
        
#         try:
#             movie_data = json.loads(response.text)
#             movies.append(movie_data)
#         except json.JSONDecodeError as e:
#             print(f"Error decoding JSON for '{title}': {e}")

#     return movies

# def get_movie_longest_runtime(*titles):
#     movies = get_movies(*titles)
#     longest_runtime = 0
#     longest_runtime_movie = None

#     for movie_data in movies:
#         runtime = movie_data.get("Runtime", "")
#         runtime_minutes = int(runtime.split()[0]) if runtime else 0

#         if runtime_minutes > longest_runtime:
#             longest_runtime = runtime_minutes
#             longest_runtime_movie = movie_data.get("Title")

#     return longest_runtime_movie



if __name__ == "__main__":
    movie_titles = ["Inception", "Interstellar", 'The Dark Knight']
    longest_runtime_movie = get_movies_longest_runtime(*movie_titles)
    print(f"The movie with longest runtime is: {longest_runtime_movie}")