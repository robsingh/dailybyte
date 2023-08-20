"""
In this Bite you are presented with a function that copies the given items data structure.

There is a problem though, the tests fail. Can you fix it?

This can be done in a one liner. If you know which module to use it will be easy, if not you will learn something new today.

Regardless we want you to think about Python's mutability. Have fun!

"""

# original function that copies the data structure

def copy_items(items):
    items.copy()

# above function only creates a shallow copy of this data structure, this means it only copies the reference, not the values. 
# to fix this, we create a deep copy. this recursively copies all the objects in the data structure, creating fully new instances. 


import copy

def copy_items(items):
    return copy.deepcopy(items)

