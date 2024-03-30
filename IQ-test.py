"""
Martin is preparing to pass an IQ test.

The most frequent task in this test is to find out which one of the given characters differs from the others. 
He observed that one char usually differs from the others in being alphanumeric or not.

Please help Martin! To check his answers, he needs a program to find the different one 
(the alphanumeric among non-alphanumerics or vice versa) among the given characters.

Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based).

Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:

['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
"""

def get_index_different_char(chars:list) -> int:
    alpha_count = 0
    non_alpha_count = 0

    for i, char in enumerate(chars):
        #checking if character is alphanumeric
        if str(char).isalnum():
            alpha_count += 1
        else:
            non_alpha_count += 1

    if alpha_count != 1:
        #if there is more than one alphanumeric character, then the different character is non-alphanumeric
        for i,char in enumerate(chars):
            if not str(char).isalnum():
                return i
    else:
        # if there is only one alphanumeric character, then the different character is alphanumeric
        for i,char in enumerate(chars):
            if str(char).isalnum():
                return i


chars = ['.', '{', ' ^', '%', 'a']
print(get_index_different_char(chars))