"""
A small but interesting Bite: given a string with leading indent spacing, calculate the amount of space (literal space, not tab or newline) characters:

'string  ' -> 0 (we only care about leading spacing)
'  string' -> 2
'    string' -> 4
etc...
This can be done in many ways. Have fun!
"""

def leading_spaces_count(s):
    count = 0
    for char in s:
        if char == ' ':
            count += 1
        elif char != '\t' and char != '\n':
            break
    return count

print(leading_spaces_count('string  '))   # Output: 0
print(leading_spaces_count('  string'))    # Output: 2
print(leading_spaces_count('    string'))  # Output: 4