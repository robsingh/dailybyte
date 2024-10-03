'''
Given an even length string, s, 
return whether or not the first half of s and the second half of s contain the same number of vowels.

Example:
s = "laptop", return true (there is one vowel in "lap" and one vowel in "top").

s = "computer", return false.
'''

def len_vowels(s:str) -> bool:
    # edge case : odd length strings cannot be split into two equal halves
    if len(s) % 2 != 0:
        return False
    
    vowels = 'aeiou'
    mid = len(s) // 2

    len_first = 0
    len_second = 0
    
    # traverse both halves simultaneously
    for i in range(mid):
        if s[i] in vowels:
            len_first += 1
        if s[i + mid] in vowels: # i + mid for second half
            len_second += 1

    return len_first == len_second


    '''
    # first approach
    for first in s[:mid]:
        if first in vowels:
            len_first += 1

    for second in s[mid:]:
        if second in vowels:
            len_second += 1


    return len_first == len_second
    '''
        

s = "computer"
print(len_vowels(s))