"""
we let you rewrite a simple countdown for loop using recursion. See countdown_for below, it produces the following output:

$ python countdown.py
10
9
8
7
6
5
4
3
2
1
time is up
You will be tested on having the same output, making it work with another start value, and of course if you used recursion. Have fun!
"""

def countdown_for(num:int):
    if num <= 0:
        print('time is up')
    else:
        print(num)
        countdown_for(num-1)
    

num = 10
countdown_for(num)