'''
Given a string, s, return the total number of substring within s that contain the same character.
Note: You may assume that s only contains lowercase alphabetical characters.

Ex: Given the following string s…

s = "aabca", return 6 ("a" appears 3 times, "aa" appears 1 time, "b" appears 1 time, and "c" appears 1 time).
'''

def common_substring(s:str):
    total_count = 0
    i = 0

    while i < len(s):
        # Count the length of the group of the same character
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        
        # add the number of substrings from this group
        total_count += (count * (count + 1)) // 2
        i += 1

    return total_count






s = "aabca"
print(common_substring(s))