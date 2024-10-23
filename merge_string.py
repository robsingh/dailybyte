'''
Given two strings, s and t, merge the two strings together alternating characters starting with s.
Note: If one string is longer than the other, append the remaining characters of the longer string 
at the end of the merged string.

Example:
s = "abc", t = "def", return "adbecf"
'''


def merge_strings(s:str,t:str) -> str:
    result = []
    i, j = 0,0

    # Loop through both strings and alternate characters
    while i < len(s) and j < len(t):
        result.append(s[i])
        result.append(t[j])
        i += 1
        j += 1

    # Append the remaining characters from the longer string
    result.append(s[i:])
    result.append(t[j:])

    return ''.join(result)


s = "abc"
t = "def"
print(merge_strings(s,t))