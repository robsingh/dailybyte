"""
Here is a list of words Jacob is trying to sort:

>>> words = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019".split()
>>> sorted(words)
['2019', 'Christmas', 'Happy', 'Holidays', "It's", 'Merry', 'PyBites', 'You', 'a', 'a', 'almost', 'and', 'and', 'wishes']

Hmm ... that year goes first. He actually wants words starting with a digit (first character) to go last!



Could you complete the function below to do this for him? So the result would be:

['a', 'a', 'almost', 'and', 'and', 'Christmas', 'Happy', 'Holidays', "It's", 'Merry', 'PyBites', 'wishes', 'You', '2019']
"""

words = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019".split()
sorted_list = sorted(words, key=str.casefold)
digits = []
sorted_alphabatic = []

for word in sorted_list:
    if word.isdigit():
        digits.append(word)
    else:
        sorted_alphabatic.append(word)

print(sorted_alphabatic + digits)


