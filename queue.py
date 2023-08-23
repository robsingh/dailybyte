"""
How about writing a queue that holds the last 5 items?

Queue follows First-In-First-Out methodology, i.e., the data item stored first will be accessed first. 
A real-world example of queue can be a single-lane one-way road, where the vehicle enters first, exits first. 
More real-world examples can be seen as queues at the ticket windows and bus-stops.
Complete the my_queue function to return a queue-like data type that keeps the last n items.

Check the standard library to see how you can do this in the shortest/most efficient way.

Have fun!
"""

# def my_queue(nums,n):
#     return nums[-n:]

# nums = [1,2,3,4,5]
# n = 3
# print(my_queue(nums,n)) # 3,4,5

from collections import deque

def my_queue(n=5):
    return deque(maxlen=n)

q = my_queue()

q.append(1)
q.append(2)
q.append(3)

print(q)

q.append(4)
q.append(5)
q.append(6)

print(q)

