"""
In this Bite you will convert Unix' wc command into Python. Your function takes a file (absolute path), reads it in and 
calculates the lines/words/chars. It returns a string of these numbers and the filename, like as a typical wc output, 
for example:

# Unix command
$ wc wc.py
      22      85     771 wc.py

# your script
$ python wc.py  wc.py
22	85	771 wc.py
Don't worry about the amount of white space between the columns, you can use tabs or spaces.

Unix files add an extra newline to the end so for content Hello\nworld Unix' wc would return 12 (not 11):

$ cat hello
hello
world
$ wc hello
       2       2      12 hello

As this is a Beginner Bite we can save you some head aches by suggesting you to use splitlines for the line counts!
Have fun and keep coding in Python!
"""

def wc(filename):
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.count('\n') + 1 # add 1 for the last line if it doesn't end with '\n'
        words = len(content.split())
        chars = len(content)
    return f"{lines}\t{words}\t{chars} {filename}"


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage wc.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    result = wc(filename)
    print(result)