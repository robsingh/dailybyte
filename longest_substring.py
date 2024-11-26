'''
Given a string 's' and an integer 'k', return the length of the longest substring in 's' you can create that contains a single capital 
letter. 
You may apply 'k' operations to 's' where a single operation consists of selecting one capital letter and modifying it to be 
another capital letter.
Note: s will only contain uppercase alphabetical characters.

Ex: Given the following s and k…

s = "BBAA", k = 2, return 4 (both B's can be changed to A's or both A's can be changed to B's).
'''

'''
Input: string 's' containing only uppercase letters.
       integer 'k' represents the max number of changes you can make.

Output: length of longest substring that can be created, all characters in the substring are the same.
'''

def longestSubstring(s:str, k:int):
    left = 0
    max_length = 0
    max_freq = 0
    freq = {}

    for right in range(len(s)):
        # add the current character to the frequency map
        freq[s[right]] = freq.get(s[right], 0) + 1

        # track the most frequent character in the window
        max_freq = max(max_freq, freq[s[right]])

        # calculate the number of changes needed
        window_length = right - left + 1
        changes_needed = window_length - max_freq

        # if changes exceed 'k', shrink the window
        if changes_needed > k:
            freq[s[left]] -= 1
            left += 1
        
        # update the max length
        max_length = max(max_length, right - left + 1)

    return max_length


s = "BBAA"
k = 2
print(longestSubstring(s, k))