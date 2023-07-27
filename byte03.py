"""
Write a function that rotates characters in a string in either direction:

- If n is positive, move n characters from beginning to end, 
e.g.: rotate('hello', 2) would return "llohe".

- If n is negative, move the last n characters to the start of the string, 
e.g.: rotate('hello', -2) would return "lohel".
"""

def rotate_characters(string:str,n:int):
    if n == 0:
        return string
    
    text_length = len(string)

    if abs(n) > text_length:
        n = n % text_length
    
    if n < 0:
        n += text_length
    
    return string[n:] + string[:n]


string = 'hello'
n = 3
print(rotate_characters(string,n))