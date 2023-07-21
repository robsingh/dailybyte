"""
In this Bite you will work with a list of names.

1. Write a function that accepts a list of names and title cases them and removes duplicates.

2. Next, sort the list in alphabetical descending order by surname.

3. Finally, find the shortest first name.

You can assume that the names in the list are single strings composed of two words: one given name and one surname.

Python built-ins will be very useful for solving these problems in very concise ways. Get it sorted!

"""

from typing import List

def shortest_first(names: List):
    # title casing and removing duplicates
    title_case_unique = list(set(name.title() for name in names))

    # sorting the surnames in descending order
    sorted_names = sorted(title_case_unique, key=lambda name:name.split()[-1], reverse=True)
    
    # shortest first name
    first_names = [name.split()[0] for name in sorted_names]
    shortest_name = min(first_names, key=len)

    return shortest_name



names = ["rob singh", "tomy harward", "jimyy liam", "timi cook", "robu singh"]
print(shortest_first(names))