"""
Martin is preparing to pass an IQ test.

The most frequent task in this test is to find out which one of the given characters differs from the others. 
He observed that one char usually differs from the others in being alphanumeric or not.

Please help Martin! To check his answers, he needs a program to find the different one (the alphanumeric among non-alphanumerics or vice versa)
among the given characters.

Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based).

Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:

['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
"""
from typing import List
import string

def get_index_diff_char(chars:List):
    alpha = set(string.ascii_letters + string.digits)

    diff_char = None
    for i,char in enumerate(chars):
        if (char in alpha) != (chars[0] in alpha):
            diff_char = i
            break
    return diff_char



chars = ['.', '{', ' ^', '%', 'a']
print(get_index_diff_char(chars))

#another method


def is_alphanumeric(char):
    return char.isalnum() if isinstance(char, str) else False


def get_index(chars):
    alpha_count = 0
    non_alpha_count = 0
    alpha_index = -1
    non_alpha_index = -1

    for i,char in enumerate(chars):
        if is_alphanumeric(char):
            alpha_count += 1
            alpha_index = i
        else:
            non_alpha_count += 1
            non_alpha_index = i

    if alpha_count == 1:
        return alpha_index
    else:
        return non_alpha_index

chars_list = ['a', '1', '@', '.','b']
print(get_index(chars_list))