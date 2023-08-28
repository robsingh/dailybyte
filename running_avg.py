"""
Write a function that takes a sequence of items and returns the running average, so for example this:

running_mean([1, 2, 3])
returns:

[1, 1.5, 2]
You can assume all items are numeric so no type casting is needed.

Round the mean values to 2 decimals (4.33333 -> 4.33).
Bonus: use a function of itertools + make it a generator, but this is not required to get this working.
"""
"""
def runnning_mean(sequence):
    running_total = 0
    running_means = []

    for i,item in enumerate(sequence, start=1):
        running_total += item
        mean = round(running_total/i,2)
        running_means.append(mean)
    return running_means

sequence = [1,2,3]
print(runnning_mean(sequence))
"""

#using generator
 
from itertools import accumulate

def running_mean(sequence):
    total_accum = accumulate(sequence)
    count = 1

    for total in total_accum:
        mean = round(total/count,2)
        count += 1
        yield mean

input_sequence = [1,2,3]
result_gen = running_mean(input_sequence)

result_list = list(result_gen)
print(result_list)