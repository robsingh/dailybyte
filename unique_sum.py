'''
Given an array of integers, nums, return the sum of all uniquely occurring elements.

Ex: Given the following nums

nums = [1, 3, 5, 5, 2], return 6 (1 + 3 + 2).

nums = [4, 4, 2, 3, 3, 2], return 0.
'''

def unique_elements(nums):
    counts = {}

    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # the reason we use parentheses or no brackets in this case is that 
    # sum() can work directly with generator expression.
    # generator expression does not create a list, produces the numbers lazily, and is more memory efficient
    # whereas list will occupy memory.
    unique_sum = sum(num for num, count in counts.items() if count == 1)
    return unique_sum
    

nums = [1,3,5,5,2]
print(unique_elements(nums))