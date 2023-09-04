"""
Complete the function below simulating Unix' tail, for example:

$ tail -3 test_tail.py
# byte to str conversion and strip off last line's newline char
expected = [line.decode("utf-8") for line in lines]
assert tail(f.name, 10) == expected
Complete the function below which receives (absolute) filepath and n lines to filter from the end which is returned in a list.

For example, if we call it on a file - stored in filepath - with this content:

Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!
... and give it n of 2 (= calling it as: tail(filepath, 2)), it should return this:

['Keep calm and code in Python!',
 'Become a PyBites ninja!']
(note: newlines are stripped off)

Have fun and let us know if you have any questions ...
"""


def tail(filepath, n):
    result = []
    with open(filepath, 'rb') as file:
        lines = file.readlines()
        lines = [line.decode('utf-8').rstrip() for line in lines[-n:]]
        result.extend(lines)
    return result


filepath = 'myfile.txt'
n = 2
print(tail(filepath, n))