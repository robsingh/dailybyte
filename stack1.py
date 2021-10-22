'''Deques are a generalization of stacks and queues. Deques support thread safe,
   memory efficient appends and pops from either side of deque with approximately O(1) 
   performance in either direction. Though 'list' supports similar operations, they 
   are optimized for fast fixed length operations and incur O(n) memory movment cost
   for pop(0) and insert(0,v) operations which change both the size and position of
   the underlying data representation. 
'''
"""Example: Deque"""
'''from collections import deque
d = deque("robin")
for elem in d:
    print(elem.upper())

d.append('s') #adding new element to the right side
d.appendleft('l') #adding new element to the left side
d.pop() #return and remove the rightmost element
d.popleft()
d[0] #peek at leftmost item
d[-1] #peek at rightmost item
d.extend('chek') #add multiple elements at once
d.rotate(1) #right rotation
d.rotate(-1) #left rotation
d.clear() # empty the deque'''

'''Design a stack that returns the minimum element in constant time.
   The stack should support common operations like push, pop, top, size,
   empty etc with no degradation in system performance.  '''

'''First approach: 
        Keep a variable to keep track of the minimum number.
        But this won't work, as we can't get the next min number
        after the min one is popped.'''

'''Second approach:
         Use two stacks. Main stack to store the actual elements, 
         & the other stack to store the required elements needed to
         determine the minimum number in constant time. '''

'''
Push - push the new element to the main stack and push it to the
       aux stack only if it is less than or equal to the current
       top element. 

Pop - remove the top element from the main stack and remove it 
      from aux stack if top element of both main and aux stack
      are the same.

Min - Top of aux stack always return the min element since we are
      pushing min element into the aux stack and removing the
      min element from aux stack only if it is removed from the
      main stack. 
'''

from collections import deque

class MinStack:
    def __init__(self):
        self.s = deque() #main stack to store elements
        self.aux = deque() #aux stack to store minimum elements

    def push(self,x):   #insert a given element on top of stack
        self.s.append(x) #push the given element to the main stack

        #if aux stack is empty, push the element to it
        if not self.aux:
            self.aux.append(x)

        else:    #push the given element to aux stack if it is less than or equal to the current minimum
            if self.aux[-1] <= x:
                self.aux.append(x) 

    
    def pop(self):         #removes the top element from the stack and returns it
        if self.empty():
            print("Stack UnderFlow")
            return -1

        #remove the top element from the main stack
        top = self.s.pop()

        #remove the top element from aux stack only if it is minimum
        if top == self.aux[-1]:
            self.aux.pop()
        return top #return the removed element

    def peek(self):        #returns the top element of the stack
        return self.s[-1]

    def len(self):         #returns the total number of elements in the stack
        return self.len(s)

    def empty(self):        #returns True if stack is empty, otherwise false
        return not self.s

    def min(self):         #returns min element from stack in constant time
        if not self.aux:
            print("Stack Underflow")
            return -1
        return self.aux[-1]


if __name__ == "__main__":
    s = MinStack()

    s.push(6)
    print(s.min())

    s.push(7)
    print(s.min())

    s.push(8)
    print(s.min())

    s.push(5)
    print(s.min())

    s.push(3)
    print(s.min())

    s.pop()
    print(s.min())

    s.push(10)
    print(s.min())

    s.pop()
    print(s.min())

    s.pop()
    print(s.min())









