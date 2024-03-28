"""
In this Bite you are given a dict and a set. 
Write a dictionary comprehension that filters out the items in the set and returns the resulting dict, 
so if your dict is {1: 'bob', 2: 'julian', 3: 'tim'} and your set is {2, 3}, the resulting dict would be {1: 'bob'}.
"""

def dict_compre(a:dict, b:set) -> dict:
    result = {}
    for key,value in a.items():
        if key not in b:
            result[key] = value
    return result




a = {1:'bob', 2:'julian', 3:'tim'}
b = {2,3}
print(dict_compre(a,b))