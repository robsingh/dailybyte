"""
Complete remove_punctuation which receives an input string and strips out all punctuation characters (!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~).

Return the resulting string. You can go full loop, list comprehension or maybe some nice stdlib functionality?
"""

import string

def remove_punctuation(input_string):
    chars = '(!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~).'
    result_string = ""

    for char in input_string:
        if char not in chars:
            result_string += char
    return result_string

# list comprehension
# result_string = "".join([char for char in input_string if char not in chars])

input_string = input("Enter the input string: ")
print(remove_punctuation(input_string))