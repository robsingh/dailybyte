"""
In this exercise you will analyze some basic car data. Here is the (fake) JSON data we created with Mockeroo - snippet below / full output here:

  [{"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},
   {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2002},
   {"id":3,"automaker":"Porsche","model":"Cayenne","year":2008},
   ... 997 car entries more ...
  ]
"""
import json
from collections import Counter

def load_json(car_data):
    with open(car_data, 'r') as file:
        data = json.load(file)
    return data

def most_prolific_automaker(car_data):
    """
    Func to find out which automaker produces the most new models for a particular year.
    """
    
    # count the occurrences of each automaker for each year
    automaker_counts = Counter((car['automaker'], car['year']) for car in load_json(car_data))

    # find the automaker with max counts
    most_prolific = max(automaker_counts, key=automaker_counts.get)

    return f"The most prolific automaker is {most_prolific[0]} with {automaker_counts[most_prolific]} new models in {most_prolific[1]}."



def get_models(car_data, automaker, year):
    """
    Filters the data set down to car models produced by a particular automaker and year.
    """
    data = load_json(car_data)
    models = [car['model'] for car in data if car['automaker'] == automaker and car['year'] == year]
    return models


car_data = 'cars.json'
print(most_prolific_automaker(car_data))
print(get_models(car_data, 'Dodge', 2000))
