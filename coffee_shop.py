'''
You walk into a coffee shop that serves all of the given customers. 
At the ith minute, customers[i] customers are in the shop. 
The barista is stressed at the ith minute if stressed[i] = 1 and calm otherwise.
Customers that are in the shop while the barista is stressed are unhappy. 
Customers that are in the shop while the barista is not stressed are happy. 
The barista knows how to remain calm for a duration of minutes, but can only do so once. 
Return the maximum number of customers that can be happy.

Ex: Given the following customers, stressed, and duration…

customers = [3, 1, 2], stressed = [1, 0, 0], duration = 1, 
return 6 (the barista can remain calm for the first minute making all the customers happy 3 + 1 + 2 = 6).

Given the following customers, stressed, and duration…

customers = [5, 2, 4, 3], stressed = [1, 1, 0, 1], duration = 2, return 11 (5 + 2 + 4)
'''
'''
thought process revolves arounds finding the best window of duration minutes in the stressed array.
Main idea is to convert stressed[i] = 1 to stressed[i] = 0.
We can solve this problem using sliding window approach.
'''

from typing import List
def count_happy_customers(customers:List, stressed:List, duration:int) -> int:
    # validation to ensure input arrays have the same length
    if len(customers) != len(stressed):
        raise ValueError("The lengths of 'customers' and 'stressed' must be equal.")
    
    # step 1: Calculate base happiness
    base_happiness = sum(customers[i] for i in range(len(customers)) if stressed[i] == 0)

    # step 2 : Sliding window for potential gain
    potential_gain = 0
    current_gain = 0

    # initialize the first window
    for i in range(duration):
        if stressed[i] == 1:
            current_gain += customers[i]
    potential_gain = current_gain

    # slide the window across the array
    for i in range(duration, len(customers)):
        # remove the impact of leftmost element
        if stressed[i - duration] == 1:
            current_gain -= customers[i - duration]
        
        # add the impact of the rightmost element
        if stressed[i] == 1:
            current_gain += customers[i]
        
        # update the maximum potential gain
        potential_gain = max(potential_gain, current_gain)

    # step 3: combine results
    return base_happiness + potential_gain


customers = [3,1,2]
stressed = [1,0,0]
duration = 1

print(count_happy_customers(customers, stressed, duration))