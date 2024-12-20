'''
Given an encoded string, 's', return its decoded representation.
The string 's' will be encoded as follows: N[letters], meaning that the letters should be repeated 'N' times in the decoded representation.
Note: You may assume 's' is always encoded correctly (i.e. correct formatting of brackets, 
only positive values outside the brackets, and always lowercase alphabetical characters inside the brackets).

Ex: Given the following string s

s = "3[a]2[b]1[c]", return "aaabbc" ("a" is repeated 3 times, "b" is repeated 2 times, and "c" is repeated 1 time).
'''
'''
approach:
1. We will use two stacks. One will save the number and other will save the character.
2. Push the characters in 'char' stack until ']' is encountered.
3. If closing bracket is found in string, pop the characters till opening bracket ']' is found, pop the integer from integer stack.
4. Repeat the characters from 'char' stack, integer.pop() number of times. 
'''

def decode(s:str):
    intStack = []
    charStack = []
    temp = ""
    result = ""
    i = 0

    while i < len(s):
        if (s[i].isdigit()):
            num = 0
            while i < len(s) and s[i].isdigit():
                 num = num * 10 + int(s[i])
                 i += 1
            intStack.append(num)
            
        elif s[i] == '[':
              charStack.append(s[i])
              i += 1

        elif s[i].isalpha():
             charStack.append(s[i])
             i += 1

        elif s[i] == ']':
             # decoding
             temp = []
             while charStack and charStack[-1] != '[':
                  temp.append(charStack.pop())
             charStack.pop()
             temp.reverse()

             repeat_count = intStack.pop()
             rep_string = ''.join(temp) * repeat_count

             charStack.append(rep_string)
             i += 1
        
        else:
             return f"check the input once again."
        
    return ''.join(charStack)



s = "3[a]2[b]1[c]"
print(decode(s))