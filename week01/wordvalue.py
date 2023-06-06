"""
This week you will write a script to calculate the (language) dictionary word that would 
have the most value in Scrabble.

Read in dictionary.txt (a copy of /usr/share/dict/words on my Mac) and 
calculate the word that has the most value in Scrabble based on LETTER_SCORES which is imported in wordvalue-template.py.
"""

from data import DICTIONARY, LETTER_SCORES
from test_wordvalue import *
def load_words():
    """Load dictionary into a list and return list."""
    with open("dictionary.txt","r") as file:
        dict_list = file.read().splitlines()
    return dict_list

def calc_word_value(word):
    """Calculate the value of the word entered into function using imported
    constant mapping LETTER_SCORES"""
    value = 0
    for letter in word.upper():
        value += LETTER_SCORES.get(letter, 0)
    return value

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list of words as arg,
    if none provided uses default dictionary"""
    if words is None:
        words = load_words()
    max_value = 0
    max_word = None
    for word in words:
        value = calc_word_value(word)
        if value > max_value:
            max_value = value
            max_word = word
    return max_word


if __name__ == "__main__":
    unittest.main() #run unittests to validate