"""
Sometimes you need to restructure a nested data structure. 
For example you can convert a dict in a list of (key, value) tuples via dict.items().

In this Bite a real world scenario where we wanted to plot some data from a Counter dict.

For plots you typically need 2 lists: X + Y axis or labels + values. 
So we needed an easy way to transpose data structures.

Complete the transpose function to do just that. 
It has to work for both dicts and lists of (named)tuples.
"""

from collections import namedtuple

def transpose(data):
    if isinstance(data, dict):
        return list(data.items())
    elif isinstance(data, list) and isinstance(data[0], tuple) and hasattr(data[0], '_fields'):
        return [tuple(zip(*data))]
    else:
        raise ValueError("Unsupported data type!")


# transposing a dictionary
data_dict = {'a':1, 'b':2, 'c':3}
transposed_dict = transpose(data=data_dict)
print(f"Transposed Dictionary: {transposed_dict}")

# transposing a list of named tuples
Point = namedtuple('Point', ['x', 'y'])
data_tuples = [Point(x=1, y=2), Point(x=3, y=4), Point(x=5, y=6)]
transposed_tuples = transpose(data=data_tuples)
print(f"Transposed Tuples: {transposed_tuples}")